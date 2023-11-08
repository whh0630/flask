import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


class lotto:
    def __init__(self):
        self.name = "lotto"
        self.updated_wg = 0
        self.last_wg = 0
        self.list = []

    def UpdateList(self):     
        try:
            with open("lotto.json", "r") as file:
                # self.list = json.load(file)
                self.list = json.load(file)
                # self.updated_wg = self.list[-1]['drwNo']
        except :
            print(' * ERROR - file is empty or error')

        self.GetLast()
        self.GetWinningAllNumbers() 

        print('Updated wg index : {}'.format(self.updated_wg))  
        print('Last wg index : {}'.format(self.last_wg))  

        # with open("lotto.json", 'w') as outfile:
        #    json.dump(self.list, outfile)

    def GetLast(self):     
        url = "https://www.dhlottery.co.kr/gameResult.do?method=byWin"
        req_result = requests.get(url)
        html = req_result.text
        # crawling the offical lotto site
        soup = BeautifulSoup(html, 'html.parser')
        no = soup.select('#dwrNoList > option:nth-child(1)')
        print(" --> data: {}".format(no))
        if len(no) == 0 :
            self.last_wg=1092
            print(" Can not crawling from site --> Set Last WG Number {}".format(self.last_wg))
        else:
            self.last_wg = int(no[0]['value'])
            print('Update last win game : {}'.format(self.last_wg))
        
        return self.last_wg

    def GetWinningNumbers(self, no):
        url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+str(no)
        req_result = requests.get(url)
        return req_result.json()

    def GetWinningAllNumbers(self):
        # check last win num
        if self.last_wg == 0 : 
            print('Last wg 0 error !')
            return

        if self.updated_wg == self.last_wg : print('This is currently the latest update.')

        # self.list = [] #for init list (test)
        # self.updated_wg = 0

        for i in range(self.last_wg) :  
        # for i in range(30) :

            if self.updated_wg > i :
                if self.updated_wg == (i+1) : print('Passed index 1~{}'.format((i+1)))
                # print('Passed index {}'.format(idx))
                continue
                
            idx = i + 1

            self.list.append(self.GetWinningNumbers(idx))
            print('Update object({}) in list '.format(idx))


lot = lotto()

