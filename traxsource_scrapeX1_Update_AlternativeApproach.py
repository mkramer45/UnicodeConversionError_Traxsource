import bs4
import requests
from bs4 import BeautifulSoup
import sqlite3
from urllib2 import urlopen
import re


my_url = 'https://www.traxsource.com/genre/20/techno/top'

# get the html
html = urlopen(my_url)

BeautifulSoup(html_text,from_encoding="utf-8")

# html parsing
page_soup = BeautifulSoup(html, "html.parser")

# get each track in the charts
tracks = page_soup.findAll('div', class_=re.compile("trk-row play-trk"))


conn = sqlite3.connect('Beatscrape.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS TrxSrcTrax(Artist TEXT, Song TEXT, Label TEXT, Genre TEXT, Price DECIMAL, Position TEXT, Websource TEXT)')

for track in tracks:

    # get the name of the song
    song = track.find('div', class_='trk-cell title')
    songx = song.text.strip()

    # get the name(s) of the artist
    artist = track.find('div', class_='trk-cell artists')
    artistx = artist.text.strip()

    genre = track.find('div', class_='trk-cell genre')
    genrex = genre.text.strip()

    label = track.find('div', class_='trk-cell label')
    labelx = label.text.strip()

    released = track.find('div', class_='trk-cell r-date')
    releasedx = released.text.strip()

    price = track.find('div', class_='buy-cont')
    pricex = price.text.strip()

    position = track.find('div', class_='trk-cell tnum-pos')
    positionx = position.text.strip()
    positiondecode = positionx.encode('ascii', 'ignore').decode('ascii')

    web_source = 'Traxsource'


    conn = sqlite3.connect('Beatscrape.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO TrxSrcTrax VALUES (?, ?, ?, ?, ?, ?, ?)", (str(artistx), str(songx), str(labelx), str(genrex), str(pricex), str(positiondecode), str(web_source)))
    conn.commit()
    cursor.close()
    conn.close()