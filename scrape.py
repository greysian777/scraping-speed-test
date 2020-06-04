import pycurl
from timer import timer
from requests import get
from typing import List
from bs4 import BeautifulSoup
import concurrent.futures
import io

LINKS_200 = open("./test_links.txt").read().splitlines()


def get_paragraf(link: str) -> str:
    r = get(link)
    soup = BeautifulSoup(r.content, "lxml")
    reader = soup.find("div", class_="read__content")
    return " ".join([p.text for p in reader.find_all("p") if "Baca juga" not in p.text])


def pycurl_get(link, data=None):
    c = pycurl.Curl()
    c.setopt(pycurl.URL, link)
    if data is not None:
        c.setopt(c.WRITEDATA, data)
    c.perform()
    c.close()


buffer = io.BytesIO()


def get_paragraf_curl(link):
    pycurl_get(link, buffer)
    soup = BeautifulSoup(buffer.getvalue(), "lxml")
    reader = soup.find("div", class_="read__content")
    return " ".join(
        [p.text for p in reader.find_all("p") if "baca juga" not in p.text.lower()]
    )


def run(links: List) -> List[str]:
    return [get_paragraf(link) for link in links]


def run_thread(links: List) -> List[str]:
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as exe:
        results = list(exe.map(pycurl_get, links))
        exe.shutdown(wait=True)
    return results


def run_mp(links: List) -> List[str]:
    with concurrent.futures.ProcessPoolExecutor() as mp:
        result = mp.map(get_paragraf, links)
    return result


@timer(1, 3)
def main():
    hasil = run_thread(LINKS_200)
    return hasil
