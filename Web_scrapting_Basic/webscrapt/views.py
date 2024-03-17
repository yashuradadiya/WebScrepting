from django.shortcuts import render
import requests
import bs4

# Create your views here.
def index(request):
    values=[]
    if request.method == "POST":
        web_url = request.POST['urls']
        tags = request.POST['tags']
        responce = requests.get(web_url)
        screpdata = bs4.BeautifulSoup(responce.text,'html.parser')
        values = screpdata.find_all(tags)
        # for data in screpdata.find_all('img'):
        #     values.append(data.get('src'))
        # print(values)
    return render(request,'index.html',{'data':values})