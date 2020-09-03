import csv
from news_headline import main__headline
from news_contents import main__contents

headline = main__headline()
contents = main__contents()

f = open('news_naver_20000.csv', 'w', encoding='utf-8-sig', newline='')
wr = csv.writer(f)

for i in range(1, 20001):
    wr.writerow([i, headline[i], contents[i]])
f.close()
