import requests
from bs4 import BeautifulSoup

req = None
html = None
soup = None
# req = requests.get('http://cs.hanyang.ac.kr/board/info_board.php')
# html = req.text
# soup = BeautifulSoup(html,'html.parser')

def init():
    global req, html, soup;

    req = requests.get('http://cs.hanyang.ac.kr/board/info_board.php', timeout=0.001)
    # print (type(req))
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

def sort(board_zip):
    board_zip.sort(key = lambda t : t[2],reverse=True)

def crawl():
    init()
    # print("hello")
    body = soup.select(
        '#content_box > div > table > tbody > tr'
    )
    # initialize lists
    number_list = []
    title_list = []
    date_list = []

    for tr in body:
        number = tr.select('td')[1].get_text(strip=True).encode('utf-8')
        title = tr.select('td')[2].get_text(strip=True).encode('utf-8')
        date = tr.select('td')[4].get_text(strip=True).encode('utf-8')
        date = int(date[:2] + date[3:5] + date[6:])

        number_list.append(number)
        title_list.append(title)
        date_list.append(date)

    board_zip = zip(number_list,title_list,date_list)
    sort(board_zip)

    return board_zip