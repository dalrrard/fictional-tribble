#! python3
# smbcDownload.py - Downloads every single smbc comic.

import requests
import os
import bs4
import mimetypes

url = 'http://www.smbc-comics.com/comic/password'
os.makedirs('smbc', exist_ok=True)
while True:
    # Download the page.
    print('Downloading page {}...'.format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Find the URL of the comic image.
    comicElem = soup.select('#cc-comicbody img')
    extension = ''
    if not comicElem:
        print('Could not find image')
    else:
        try:
            comicUrl = comicElem[0].get('src')
            # Download the image.
            print('Downloading image {}...'.format(comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
            content_type = res.headers['content-type']
            extension = mimetypes.guess_extension(content_type)
        except:
            # Skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = prevLink.get('href')
            continue

    # Save the image to ./smbc
    if extension:
        fileName = os.path.join('smbc', os.path.basename(url)) + extension
    else:
        fileName = os.path.join('smbc', os.path.basename(url))
    imageFile = open(fileName, 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev button's url
    try:
        prevLink = soup.select('a[rel="prev"]')[0]
        url = prevLink.get('href')
    except IndexError:
        break

print('Done.')
