from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from pandas import Series, DataFrame
import numpy as np
import pandas as pd
import re
import time
import csv

"""
네이버 뉴스 크롤링 코드입니다.
https://entertain.naver.com/ranking
페이지를 기준으로 크롤링 하였습니다.
"""


def naver_crwalling(url):
    # 크롬 open
    driver_path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    for x in range(1, 31):
        # 네이버 정치뉴스 메인 페이지(댓글많은순)
        url_page = url
        driver.get(url_page)
        time.sleep(0.3)
        # 1~30 링크 클릭

        driver.find_element_by_css_selector(
            '#wrap > table > tbody > tr > td.content > div > div.ranking > ol > li.ranking_item.is_num{0} > div.ranking_text > div.ranking_headline > a'.format(x)).click()
        time.sleep(7)
        # 댓글창 클릭
        try:
            driver.find_element_by_css_selector(
                '#cbox_module > div.u_cbox_wrap > div.u_cbox_view_comment > a > span.u_cbox_in_view_comment').click()
        except:
            driver.find_element_by_css_selector(
                '#cbox_module > div > div > a').click()
        time.sleep(0.3)
        # 댓글 끝까지 로드
        while(1):
            time.sleep(0.3)
            try:
                driver.find_element_by_css_selector(
                    '#cbox_module > div > div.u_cbox_paginate > a > span > span > span.u_cbox_page_more').click()
            except:
                break
        # 페이지 추출 및 리스트에 추가
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        temp = soup.find_all('span', 'u_cbox_contents')
        print(len(temp))

        f = open('naver_comments_200827.csv', 'a',
                 encoding='utf-8-sig', newline='')
        wr = csv.writer(f)
        for i in range(len(temp)):
            wr.writerow([temp[i].get_text()])
        f.close()
    print('----한페이지 끝!-----')


naver_crwalling(
    'https://news.naver.com/main/ranking/popularMemo.nhn?rankingType=popular_memo&sectionId=100&date=20200827')
