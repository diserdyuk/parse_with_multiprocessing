import requests
import csv
from multiprocessing import Pool
from time import sleep



def get_text(url):    # get text from web page
    r = requests.get(url)
    return r.text


def write_csv(d):    # write data to csv file
    with open('liveinternet2.csv', 'a') as f:
        order = ['name', 'url', 'descrip', 'view', 'percent']
        write = csv.DictWriter(f, fieldnames=order)
        write.writerow(d)


def get_page_text(t):    # get text from page & write data to csv
    text = t.strip().split('\n')[1:]    # delite all non use symbols, split string and non use 1st elem.list

    for eachstr in text:
        column = eachstr.strip().split('\t')    # decision str '\t' on elements of list
        name = column[0]
        url = column[1]
        descrip = column[2]
        view = column[3]
        percent = column[4]

        data = {'name': name,    # pack in dictionary
                'url': url,
                'descrip': descrip,
                'view': view,
                'percent': percent}

        write_csv(data)    # dictionary write to csv


def combine_func(d):    # combine func.get_text & get_page_text 
    text = get_text(d)    # get text 
    get_page_text(text)    # get elements list


def main():

    # 6999
    url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'
    urls = [url.format(str(i)) for i in range(1, 7000)]    # get urls page from 1 to 6999

    with Pool(20) as p:    # 20 process 
        p.map(combine_func, urls)



if __name__ == "__main__":
    main()