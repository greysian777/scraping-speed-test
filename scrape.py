from requests import get
#from tqdm import tqdm
#import time
from typing import List
from bs4 import BeautifulSoup
#import concurrent.futures
#import joblib

LINKS = open("./ALL.txt").read().splitlines()[: int(1e4)]


def get_paragraf(link: str) -> str:
    r = get(link)
    soup = BeautifulSoup(r.content, "lxml")
    reader = soup.find("div",class_="read__content")
    return " ".join([p.text for p in reader.find_all("p") if "Baca juga" not in p.text])


def run(links: List) -> List[str]:
    return [get_paragraf(link) for link in links]


def run_thread(links: List) -> List[str]:
    with concurrent.futures.ThreadPoolExecutor() as exe:
        results = exe.map(get_paragraf, links)
    return results


def run_mp(links: List) -> List[str]:
    with concurrent.futures.ProcessPoolExecutor() as mp:
        result = mp.map(get_paragraf, links)
    return result


if __name__ == "__main__":
    #start = time.time()
    print('getting links')
    # hasil = run_mp(LINKS[:200])
    hasil = run(LINKS[:200])
    print('finished scraping')
    with open('hasil.txt', 'w') as f: 
        for a in hasil: 
            f.writelines(f'{a}\n')
    #end = time.time() - start
    #with open("timelog", "a") as f:
        # f.writlines(f"python run: {end}s")
    """
    scrape_sizes = range(200, len(LINKS), 500)
    logs = []
    for size in tqdm(scrape_sizes):
        links = LINKS[:size]
         start = time.time()
        run_mp(links)
        end = time.time()-start   
        logs.append({
            'size': size,
            'time': end
        })
    joblib.dump(logs, 'timelog_python.pkl')
    """
