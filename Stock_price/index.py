import requests
import bs4

url = "https://www.google.com/finance/markets/climate-leaders"
dic = {'Company':[],'price':[],'stoke':[],'percentage':[]}

resp = requests.get(url)
screaptdata = bs4.BeautifulSoup(resp.text,'html.parser')

companies = screaptdata.select('div.ZvmM7')
for company in companies:
    dic['Company'].append(company.string)

