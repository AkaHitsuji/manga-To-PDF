import requests
import argparse
from bs4 import BeautifulSoup

def download_manga(args):
    base_url = args.u
    output_folder = args.f
    num_chapters = args.n
    start_chapter = args.s

    chapter_name = base_url.split("/")[3]

    manga_downloaded = False
    count = 0

    while(manga_downloaded!=True):
        chapter_url = base_url + '/' + str(start_chapter)
        chapter_downloaded = False
        page_num = 1
        while(chapter_downloaded!=True):
            if(page_num==1):
                page_url = chapter_url + '/'
            else:
                page_url = chapter_url + '/' + str(page_num)

            try:
                page = requests.get(page_url)
                page.raise_for_status()
                download_img(page, chapter_name, start_chapter, page_num)
            except requests.exceptions.RequestException as e:
                print(e)
                print('chapter ' + str(start_chapter) + ' downloaded')
                chapter_downloaded = True

            page_num += 1

        start_chapter += 1
        count += 1
        if count==num_chapters:
            manga_downloaded = True
            print('Manga finished downloading')


def download_img(page, chapter_name, start_chapter, page_num):
    soup = BeautifulSoup(page.text, 'html.parser')
    image_url = soup.find_all('img')[0]['src']

    # download image from image url
    try:
        r = requests.get(image_url)
        r.raise_for_status()
        img_data = requests.get(image_url).content

        image_title = chapter_name + '_' + str(start_chapter) + '_' + str(page_num) + '.jpg'
        with open(image_title, 'wb') as handler:
            handler.write(img_data)

        print('image '+str(page_num)+' downloaded')
    except requests.exceptions.RequestException as e:
        print(e)
        print("image was not downloaded")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', type=str, default='https://www.mangareader.net/fantasista',
                        help='URL of the manga')
    parser.add_argument('-s', type=int, default=1,
                        help='chapter number to start downloading from')
    parser.add_argument('-n', type=int, default=100,
                        help='number of chapters you want to download')
    parser.add_argument('-f', type=str, default='dn',
                        help='output folder')
    args = parser.parse_args()
    download_manga(args)


if __name__ == '__main__':
    main()
