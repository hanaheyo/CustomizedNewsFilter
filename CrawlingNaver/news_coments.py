import requests
from bs4 import BeautifulSoup


def crawling(soup):
    result = soup.find(
        'div', class_='_article_body_contents').get_text().replace('\n', '').replace('// flash ', '').replace('\\', '').replace('function _flash_removeCallback() {}', '').replace('\t', '').replace('   ', '').replace('오류를 우회하기 위한 함수 추가', '')
    return result


def get_href(soup):
    Href = []
    for i in soup.find(
            'ol', class_='ranking_list').find_all('div', class_='ranking_headline'):
        i = i.find('a')["href"]
        Href.append(i)
    return Href


def main__contents():
    list_href = []
    result = []

    url = "https://news.naver.com/main/ranking/popularMemo.nhn?rankingType=popular_memo&sectionId=100&date=20200901"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    list_href += get_href(soup)

    for href in list_href:
        href_req = requests.get(href)
        href_soup = BeautifulSoup(href_req.text, "html.parser")
        result.append(crawling(href_soup))

    # return result
    print(result)


if __name__ == "__main__":
    main__contents()
