# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 20:29:19 2021

@author: adeep
"""
#Importinag all the necessary libraries
import requests
import json
import pandas as pd

#print all the avilable inputs
print("Avilable series are: \n1)Mr. Robot (USA)\n2)Better Call Saul (AMC)\n3)Homeland (Showtime)\n4)Silicon Valley (HBO)\n5)The Walking Dead (AMC)\n6)South Park (Comedy Central)\n7)Game of Thrones (HBO)\n8)House of Cards (Netflix)\n9)The Big Bang Theory (CBS)\n10)Narcos (Netflix)\n11)Black Mirror (Netflix)\n12)Stranger Things (Netflix)\n13)Rick and Morty (Adult Swim)\n14)Westworld (HBO)")
url_series = ['mr-robot', 'better-call-saul', 'Homeland', 'silicon-valley', 'the-walking-dead', 'south-park', 'game-of-thrones', 'house-of-cards', 'big-bang-theory', 'narcos', 'black-mirror', 'stranger-things', 'rick-&-morty', 'westworld']


#get the URL of the series choosen by the use

series = int(input("please enter the index of the series you wanna know about:"))
if (series <= 14):
    finalurl = 'http://api.tvmaze.com/singlesearch/shows?q=' + url_series[series-1] + '&embed=episodes'
    r = requests.get(finalurl)
print("you selected:",url_series[series-1])
 

#after retreving the data convert the data form json to text
     
mytemp = {}
temp = 0
cols = ['season', 'number', 'name', 'airdate' , 'summary']  
text_json = json.loads(r.text)

#In the the text choose the nexessary threads
# Build a datafram from the text by choosing appropriate variables
for i in text_json['_embedded']['episodes']:
    season =i['season']
    number = i['number']
    name  = i['name']
    airdate = i['airdate']
    summary = i['summary'].replace("<p>","").replace("</p>","")
    temp +=1
    mytemp[temp] = [season, number, name, airdate , summary]
    mytemp_df = pd.DataFrame.from_dict(mytemp, orient = 'index', columns = cols)


#To find number of seasons avilable in a choosen series
length = len(mytemp_df['season'].unique())    
print("there are", length ,"seasons avilable")    

#to choose the series user is intrested in 
value = int(input("enter the season:"))
if(value< len(mytemp_df['season'].unique())):
    x = (mytemp_df['season'] == value).sum()
    print("there are", x ,"episodes")

#To select the series user is intrested in
ep = int(input("enter the episode:"))
if (value & ep <= x):
    output = (mytemp_df[(mytemp_df['season'] == value) & (mytemp_df['number'] == ep)])
    print(output['name'])
    print(output['summary'])
else:
    print("data could not be found")