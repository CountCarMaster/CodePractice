from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import xlwt
import sqlite3

#爬取的特征
findLink = re.compile(r'<a href="(.*?)">')
findTitle = re.compile(r'<span class="title">(.*)</span>')
findImg = re.compile(r'<img.*src="(.*?)" .*/>')

def askURL(url):
    #伪装自己
    headRes = {
        "User-Agent": "Mozilla / 5.0(Macintosh; Intel Mac OS X 10_15_7) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 97.0.4692.71Safari / 537.36"
    }
    request = urllib.request.Request(url, headers=headRes)
    html = "" #在try外面定义，要不然就没了
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    #        print(html)
    # 看看有没有问题，有的话就返回错误码以及错误原因
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def getData(baseurl):
    data = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            item = str(item)
            a = {}
            link = re.findall(findLink, item)[0]
            a['link'] = link
            title = re.findall(findTitle, item)
            if len(title) == 2:
                a['ChineseTitle'] = title[0]
                otitle = title[1].replace("/", "")
                otitle = otitle.replace("\xa0", "")
                a['ForeignTitle'] = otitle
            else:
                a['ChineseTitle'] = title[0]
                a['ForeignTitle'] = ' '
            img = re.findall(findImg, item)
            a['Img'] = img
            data.append(a)
    return data

def saveData(data, savepath):
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("豆瓣电影top250", cell_overwrite_ok=True)
    sheet.write(0, 0, "Link")
    sheet.write(0, 1, "Chinese Title")
    sheet.write(0, 2, "Foreign Title")
    sheet.write(0, 3, "Image Link")
    for i in range(0, 250):
        dat = data[i]
        num = 0
        for j in dat.values():
            sheet.write(i + 1, num, j)
            num = num + 1
    book.save(savepath)

def main():
    baseurl = "https://movie.douban.com/top250?start="
    data = getData(baseurl)
    savepath = "top250.xls"
    saveData(data, savepath)

if __name__ == '__main__':
    main()
