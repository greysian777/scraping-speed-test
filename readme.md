# Problem statement

- speed scraping mengambil paragraf pada kompas
    - diukur dengan berapa page yang bisa dia scrape per detik

# Solutions

- Python

    Pake requests dan bs4

    - serial biasa
    - threading
    - multiprocessing
- Go

    Pake gocolly
    - serial biasa
    - async

## method

yang dihitung hanya durasi scraping aja, jadi importing dependencies, links, building, compiling nya tidak dihitung

## study case

- given a list of links (length:=200) in a txt, dimana links nya diambil dari indeks kompas
    - link diambil hanya di [kompas.com/money](http://kompas.com) kemudian di-random menggunakan dataframe.sample
- scrape all the links
- get paragraph
- turn into txt

# results

### python 3.7.3

min(32, os.cpu_count() + 4)

python serial: 83.7776300907135s

python threading: 27.289576053619385s

python multiprocessing: 18.571115970611572s

### Go 1.14.3 darwin/amd64
Parallelism = 2

Serial: 21.831870674s

Asyc: 10.51327985s