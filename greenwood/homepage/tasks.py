from celery import shared_task
from listing.models import Listing
import re
import requests
from bs4 import BeautifulSoup
from random import shuffle
from time import sleep
import sqlite3
from random import choice,sample
import os
from greenwood.settings import BASE_DIR

PATH_TO_DB=os.path.join(BASE_DIR, 'Otomoto_cars.db')

@shared_task()
def test_task():
    return "Hi, I am workong"




@shared_task()
def select_listings_for_hp():
    all_marked=Listing.objects.filter(is_main=True)
    for l in all_marked:
        l.is_main=False
        print(f'cнял отметку {l.id}')
        l.save()

    all_entries = list(Listing.objects.all())
    random_items = sample(all_entries, 6)

    shuffle(all_entries)
    for l in random_items:
        l.is_main=True
        print(f'отметил {l.id}')
        l.save()


    return

@shared_task()
def select_listings_for_catalog():
    Listing.objects.all().delete()
    cann = sqlite3.connect(PATH_TO_DB)
    cursor = cann.cursor()
    elements = cursor.execute(f"""SELECT * FROM Listings""")
    elements = elements.fetchall()
    cann.commit()
    shuffle(elements)
    for i in range(0, 50):
        print(elements[i])
        element=elements[i]
        title=element[-1]
        price=element[1]

        print(price)
        year=element[2]
        fuel=element[3]
        city=element[5]
        odometr=element[6]
        volume=element[8]
        listing_link=element[0]
        mark=element[10]
        model=element[11]
        image_url=element[-2]
        l = Listing(title=title,price=price,year=year,fuel=fuel,city=city,odometr=odometr,volume=volume,
                listing_link=listing_link,model=f'{mark} {model}',image_url=image_url)
        print (l.title)
        l.save()

    return



def parser(link): #request+text via proxies
    proxies = ['54.38.218.215:6582', '125.17.80.226:8080', '54.38.155.89:6582', '151.232.72.12:80', '151.232.72.18:80',
               '151.232.72.20:80', '151.232.72.16:80', '103.147.134.218:8080', '182.71.200.50:80', '151.232.72.15:80',
               '188.166.237.61:3128', '147.135.7.120:3128', '59.120.117.244:80', '163.172.29.94:3838',
               '104.244.99.186:80', '142.44.221.126:8080', '128.199.214.87:3128', '88.99.10.251:1080',
               '185.61.92.207:43947', '195.189.60.97:3128', '201.75.0.51:53281', '151.232.72.22:80',
               '45.137.216.118:80', '95.174.67.50:18080', '151.232.72.23:80', '151.232.72.14:80', '83.97.23.90:18080',
               '103.146.177.39:80', '165.22.64.68:36918', '165.22.81.30:39686', '88.99.10.254:1080', '167.71.5.83:3128',
               '169.57.1.84:8123', '161.202.226.194:80', '105.27.238.161:80', '78.47.16.54:80', '151.232.72.19:80',
               '64.71.145.122:3128', '54.38.219.100:6582', '191.96.42.80:8080', '157.230.103.91:38609',
               '173.192.128.238:25', '88.198.24.108:8080', '81.201.60.130:80', '80.48.119.28:8080', '159.8.114.37:8123',
               '37.120.192.154:8080', '163.172.213.218:3838', '162.144.106.245:3838', '85.238.104.235:47408',
               '43.248.24.158:51166', '173.212.202.65:80', '20.185.176.102:80', '13.209.155.88:8080',
               '213.230.107.125:3128', '202.40.188.94:40486', '113.254.85.88:8193', '52.157.97.234:80',
               '131.108.61.46:3128', '152.0.201.164:999', '103.57.70.248:52000', '162.144.36.187:3838',
               '119.82.253.123:36169', '85.10.219.97:1080', '183.87.153.98:49602', '144.76.214.154:1080',
               '203.202.245.58:80', '104.45.188.43:3128', '148.251.153.6:1080', '185.134.23.198:80',
               '85.10.219.103:1080', '191.232.170.36:80', '94.141.233.66:53171', '54.38.218.209:6582',
               '54.38.218.214:6582', '176.56.107.140:50177', '61.228.35.49:8080', '110.138.205.217:8080',
               '54.38.155.95:6582', '88.99.10.255:1080']
    s = requests.Session()
    s.proxies = choice(proxies)
    r = s.get(link)
    sleep(1)
    return r.text


def find_listings(txt): #here i can find html of listings on web-pages
    soup = BeautifulSoup(txt,'html.parser')
    listings=soup.find_all('article')
    return listings


def find_data(listing,mark): #finding key data in listing, data is not always exist
    lisitng_link=re.findall("""href="(.+)" title""",str(listing))[0]
    price=listing.find_all(class_='offer-price__number')
    price=re.findall("""<span>(.+)</span>""",str(price))[0].replace(" ",'')
    price = int(price)
    params=listing.find_all(class_='ds-param')
    try:
        year=int(params[0].get_text().replace(" ",""))
    except:
        year=0
    try:
        fuel=params[3].get_text().replace("\n","")
    except:
        fuel = params[2].get_text().replace("\n", "")
    try:
        region=listing.find(class_='ds-location-region').get_text()[1:-1]
    except:
        region=''
    try:
        city=listing.find(class_='ds-location-city').get_text()
    except:
        city=''
    try:
        odometr=int(params[1].get_text().replace(" ","").replace("km",''))
    except:
        odometr=0
    model=listing.find(class_='offer-title').get_text().replace("\n","").replace(f'{mark} ','').lstrip().rstrip()
    try:
        m=re.findall("(.+) \d\..+",model)[0]
        model=m
    except:
        model=model
    try:
        title = listing.find(class_='offer-title').get_text().replace("\n", "").lstrip().rstrip()
    except:
        title='No title'
    # img_url=listing.find(class_='offer-item__photo  ds-photo-container')
    try:
        img_url=re.findall('data-srcset="(.+) 768w"',str(listing.find('img')))[0]
    except:
        img_url='Not found'
    try:
        subtitle=listing.find(class_='offer-item__subtitle ds-title-complement hidden-xs').get_text()
    except:
        subtitle='No subtitle'
    try:
        l_id=int(re.findall('data-ad-id="(\d+)"',str(listing))[0])
    except:
        l_id=404

    try:
        volume=int(params[2].get_text().replace(" ","").replace("cm3","").replace("\n",""))
    except:
        volume=1
    # print(lisitng_link,price,year,fuel,region,city,odometr,model,volume)
    data=[lisitng_link,price,year,fuel,region,city,odometr,title,volume,l_id,mark,model,img_url,subtitle]
    return data

def find_n_pages(link): #it checks how many pages haas each mark but no more than 500 because it is limit of otomoto.pl
    txt=parser(link)
    n=int(re.findall('<span class="counter">\((.+)\)</span>', txt)[0].replace(" ",''))//32+1

    if n>500:
        n=500
    return n


def format_data(data): # formating data for db
    new_data=""
    for i in data:
        if "'" in str(i):
            i=i.replace("'","")

        new_data+=f"'{i}',"
    return new_data[:-1]

@shared_task()
def create_data():

    delete_all_data()
    # it will find listing by marks(ex.GAZ).
    # link='https://www.otomoto.pl/osobowe/?search%5Bfilter_enum_damaged%5D=0&search%5Border%5D=created_at_first%3Adesc&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D=&page={}'
    link='https://www.otomoto.pl/osobowe/{}/?search%5Bfilter_enum_has_vin%5D=1&search%5Bfilter_enum_damaged%5D=0&search%5Border%5D=created_at%3Adesc&search%5Bbrand_program_id%5D%5B0%5D=&search%5Bcountry%5D=&page={}'
    marks=['Ferrari', 'Lotus' ,'McLaren', 'Trabant','Tesla']
    # List of marks upper

    for mark in marks:
        sleep(1)
        l=0
        n=find_n_pages(link.format(mark.replace(' ','-'),1))
        print(f'{n} pages in {mark}' )
        for p in range(1,n+1):
            page=link.format(mark.replace(' ','-'),p)
            cann = sqlite3.connect(PATH_TO_DB)
            cursor = cann.cursor()
            for listing in find_listings(parser(page)):
                sleep(2)
                try:
                    data=find_data(listing,mark)
                    data=format_data(data)

                    cursor.execute(
                        f"""INSERT INTO Listings VALUES({data})""")
                except Exception as e:
                    print(f'Error {e}\n{page}')
                    continue
            l += 1
            cann.commit()
    return 'пропарсил'


def delete_all_data():
    cann = sqlite3.connect()
    cursor = cann.cursor()
    cursor.execute(PATH_TO_DB)
    cann.commit()
    cann.close()

