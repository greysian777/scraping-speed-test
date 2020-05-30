import requests
import time
from typing import Set, List
from bs4 import BeautifulSoup
import concurrent.futures

LINKS = set(open("./test_links.txt").read().splitlines())


def get_paragraf(link: str) -> str:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "lxml")
    reader = soup.find("div", {"class": "read__content"})
    return " ".join([p.text for p in reader.find_all("p") if "Baca juga" not in p.text])


def run(links: Set) -> List[str]:
    return [get_paragraf(link) for link in links]


def run_thread(links: Set) -> List[str]:
    with concurrent.futures.ThreadPoolExecutor() as exe:
        results = exe.map(get_paragraf, links)
    return results


def run_mp(links: Set) -> List[str]:
    with concurrent.futures.ProcessPoolExecutor() as mp:
        result = mp.map(get_paragraf, links)
    return result


if __name__ == "__main__":
    start = time.time()
    run_mp(LINKS)
    end = time.time() - start
    with open("timelog", "a") as f:
        f.writelines(f"python run {str(time.time())}: {end}s\n")
