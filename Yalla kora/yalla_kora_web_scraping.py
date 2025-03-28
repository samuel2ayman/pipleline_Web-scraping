import requests
from bs4 import BeautifulSoup
import csv
import sys
Day=int(input("enter day : "))
Month=int(input("enter month : "))
Year=input("enter year : ")
if Day > 31:
  print("Enter correct day number")
if Month>12:
  print("Enter correct month number")
match_details=[]
try:
    page=requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={Month}/{Day}/{Year}#")
except requests.exceptions.RequestException as e:
    # Handle the exception
    print(f"Request failed: {e}")

def main(page):
  src_code=page.content
  organized_code=BeautifulSoup(src_code,"html.parser")
  print(src_code)
  champions_list=organized_code.find_all("div",{'class':'matchCard'})
  def Get_match_info(champions_list):
     champion_title=champions_list.find("div",{'class':'title'}).find("h2").text.strip()
     all_matches=champions_list.find_all("div",{'class':'item finish liItem'}) + champions_list.find_all("div",{'class':'item future liItem'})+ champions_list.find_all("div",{'class':'item now liItem'}) 

     for i in range(len(all_matches)):
            team1=all_matches[i].find("div",{'class':'teamA'}).find("p").text.strip()
            team2=all_matches[i].find("div",{'class':'teamB'}).find("p").text.strip()
            time=all_matches[i].find("span",{'class':'time'}).text.strip()
            match_result=all_matches[i].find("div",{'class':'MResult'}).find_all("span",{'class':'score'})
            score=f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            match_details.append({"نوع البطوله":champion_title,"الفرق الاول":team1,"الفريق الثاني":team2,"النتيجه":score,"ميعاد المباره":time})
  for i in range(len(champions_list)):   
    Get_match_info(champions_list[i])
  if len(match_details)==0:
      print("No matches this day")
      sys.exit()

  hedders=match_details[0].keys()
  with open(r"C:\Users\samuel\Desktop\python screens\programs\web scraping program\output file.csv", "w",encoding="utf-8") as output_file:
    dict_writer=csv.DictWriter(output_file,hedders)
    dict_writer.writeheader()
    dict_writer.writerows(match_details)
    print("file created successfully for your first web scraping")

main(page)