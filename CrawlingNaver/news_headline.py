import requests
from bs4 import BeautifulSoup


def crawling(soup):
    result = []
    headline = soup.find(
        'ol', class_='ranking_list').find_all('div', class_='ranking_headline')
    for text in headline:
        text = text.find('a').get_text().replace(
            '\n', '').replace('&apos;', '')
        result.append(text)
    return result


def main__headline():
    answer = []
    url = "https://news.naver.com/main/ranking/popularMemo.nhn?rankingType=popular_memo&sectionId=100&date=20200901"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    answer += crawling(soup)

    # return answer
    print(answer)


if __name__ == "__main__":
    main__headline()
