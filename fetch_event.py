#-------------------------------------------------------------------------------
# Name:        fetch_teams data
# Purpose:      to fetch data for two teams
#
# Author:      embassy
#
# Created:     17/09/2017
# Copyright:   (c) embassy 2017
# Licence:     <none>
#-------------------------------------------------------------------------------

from requests import *
from bs4 import BeautifulSoup
from threading import *
import queue
import pickle
import os
import re


teams = []
teams_data = []

def parit(obj):
    for i in obj:
        return i

def par(obj):
    st = parit(obj)
    if(st==None):
        return ""
    else:
        return st


def load_page(page):
    user = "UCWEB/2.0 (Java; U; MIDP-2.0; Nokia203/20.37) U2/1.0.0 UCBrowser/8.7.0.218 U2/1.0.0 Mobile"
    try:
        req = request("GET",page,headers={"User-Agent":user})
        return(req.status_code,req.content)
    except ConnectionError:
        return (11,0)

def download_match():
    fil = open("./data/teams.txt","wt",encoding='utf-8')
    stat,cont=load_page("http://www.livescore.cz/index.php")#tomorrow
    if(stat !=200):
        return(510)
    soup = BeautifulSoup(cont)
    main_div = soup.find("div",id="soccer_livescore")
    main_table = main_div.find("table",class_="tab main-live")
    match_rows = main_table.find_all("tr",class_="match")
    for i in match_rows:
        match = BeautifulSoup(str(i))
        state = par(match.find(class_="col-score").stripped_strings)
        home = par(match.find(class_="col-home").stripped_strings)
        home_url = "http://www.livescore.cz"+ match.find(class_="col-home").a.get("href")
        guest = par(match.find(class_="col-guest").stripped_strings)
        guest_url = "http://www.livescore.cz"+ match.find(class_="col-guest").a.get("href")
        print(str(state),",",str(home),",",str(home_url),",",str(guest),",",str(guest_url),file=fil)

    fil.close()

    return(0)


def load_team():
    tlist = []
    print("FILTERING DATA FOR VAILD EVENT.....")
    obj = open(os.path.realpath("./data/teams.txt"),"r")
    ob = obj.readlines()
    #print(ob)
    for i in ob:
        data = i.split(",")
        if(data[0].strip()=="-:-"):
            hm = data[1].strip()
            hm_url = data[2].strip()
            aw = data[3].strip()
            aw_url = (data[4].strip("\n")).strip()
            teams.append([hm,hm_url,aw,aw_url])

        else:
                pass

    obj.close()


    temp = open(os.path.realpath("./data/vmatch.txt"),"wb")
    pickle.dump(teams,temp)
    temp.close()
    return(0)

def cmate(data):
    try:
        a = BeautifulSoup(str(data)).find_all("td")
        tem = a[2]
        return(a)

    except IndexError:
        return(0)




def Pmathes(team,url):
    fil = open("temp.txt","wt")
    algame = []
    algame2 = []
    game = []
    game2 = []
    h = 0
    h2 = 0
    a = 0
    a2 = 0
    stat,cont=load_page(url)
    if(stat !=200):
        return(510)
    soup = BeautifulSoup(cont)
    main = soup.find_all("tr")
    for i in main:
        #print(i)
        t = cmate(i)
        if(t):
            algame.append([par(t[2].stripped_strings),par(t[3].stripped_strings),par(t[4].stripped_strings)])


        else:
            pass
    #pull home 6 games
    for i in algame:
        if(i[0]==team and i[1] !="-:-"):
            game.append(i[1])
            h +=1
        if(h==6):
            break

    #pull away 6 games
    for i in algame:
        if(i[2]==team and i[1] !="-:-"):
            game.append(i[1])
            a +=1
        if(a==6):
            break


    fil.close()
    return (game)

def H2H(team,url,team2):
    fil = open("temp.txt","wt")
    algame = []
    game = []
    h = 0
    a = 0
    stat,cont=load_page(url)
    if(stat !=200):
        return(510)
    soup = BeautifulSoup(cont)
    main = soup.find_all("tr")
    for i in main:
        #print(i)
        t = cmate(i)
        if(t):
            algame.append([par(t[2].stripped_strings),par(t[3].stripped_strings),par(t[4].stripped_strings)])


        else:
            pass
    #pull  H2H data
    for i in algame:
        #print(team2,i[2],file=fil)
        if((i[0]==team2 or i[2]==team2) and (i[1] !="-:-")):

            sh,sa = i[1].split(":")
            res = i[0]+":"+sh+":"+i[2]+":"+sa
            game.append(res)
            print(res.encode("ascii"),file=fil)

    fil.close()
    return (game)

def load_teams_back():
    global teams
    file = open("./data/vmatch.txt","rb")
    teams = pickle.load(file)
    file.close()
    return 0;


def team_datas():
    fil = open("temp.txt","wt")
    du = open("./data/teams_data.txt","wb")
    for datas in teams:
        #fetch home team1
        print("PROCESSING : ",datas[0],"-",datas[2]," data....")
        team1 = Pmathes(datas[0],datas[1])
        team2 = Pmathes(datas[2],datas[3])
        h2h = H2H(datas[0],datas[1],datas[2])
        teams_data.append([team1,team2,h2h])
        print("PROCESSING : ",datas[0],"-",datas[2]," data.... DONE")
    fil.close()
    pickle.dump(teams_data,du)
    du.close()














