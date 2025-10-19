#importing required libiraries
import requests
from bs4 import BeautifulSoup
import csv

# get the content of page as html
code=requests.get(r"https://wuzzuf.net/search/jobs/?a=spbg&q=data%20engineer")
src=code.content
page=BeautifulSoup(src,"html.parser")
print(page)
job_details=[]
links=[]

jobs=page.find_all("div",{"class":"css-1gatmva e1v1l3u10"})
print(len(jobs))

for i in range(len(jobs)):
    job_title=jobs[i].find("h2",{"class":"css-m604qf"}).find("a").text
    company_name=jobs[i].find("div",{"class":"css-d7j1kk"}).find("a").text.strip()
    address=jobs[i].find("span",{"class":"css-5wys0k"}).text.strip()
    posted=jobs[i].find("div",{"class":"css-d7j1kk"}).contents[3].text
    work_type=jobs[i].find("span",{"class":"css-o1vzmt eoyjyou0"}).text
    link=jobs[i].find("h2",{"class":"css-m604qf"}).find("a").get('href')
    job_details.append({"job title":job_title,"company name":company_name,"address":address,"posed from":posted,"work type":work_type,"job link":link})
    
    
hedders=job_details[0].keys()
with open(r"C:\Users\samuel\Desktop\python screens\programs\wazuf web scraping\wuzzuf.csv", "w") as output_file:
    dict_writer=csv.DictWriter(output_file,hedders)
    dict_writer.writeheader()
    dict_writer.writerows(job_details)
    print("file created successfully for your first web scraping")

