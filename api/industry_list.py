import requests
import os
import datetime
import json

url = "https://www.swsresearch.com/institute-sw/api/download_center/trade_classification/?page=1&page_size=1000"
dirname = os.path.dirname(os.path.realpath(__file__)) + "\\api_data\\"
str_today = datetime.datetime.now().strftime('%Y-%m-%d')
file_name = dirname + "industry"+str_today

def list_industry():
    payload={}
    headers = {
      'Accept': '*/*',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
      'Cookie': 'i18next=zh-CN',
      'Pragma': 'no-cache',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
      'X-Access-Token': 'null',
      'clientType': '4',
      'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'token': ''
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)
    if int(response.status_code) == 200:
        data = json.loads(response.text)
        data = data['data']['results']
        print(dirname+str_today)
        with open(file_name,'w',encoding='utf-8') as f:
            # leave out the '[]'
            str_data = json.dumps(data)
            f.write(str_data[1:len(str_data)-1])
            f.close()

if __name__ == "__main__":
    list_industry()
