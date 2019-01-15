

#-------------------------------------------------------------------------------
# Name:        ENGINE.py
# Purpose:
#
# Author:      embassy(silento)
#
# Created:     21/09/2017
# Copyright:   (c) embassy 2017
# Licence:     <DONT COPY AND PASTE>
#-------------------------------------------------------------------------------
import time
import datetime
from random import *

def find_date(date):
    day = date[:4]
    mon = date[5:8]
    year = date[9:11]
    return(day.strip(),mon.strip(),year.strip())


def check_win(data1,data2,h2h,team):
    #winp,awinp,hwinp,gp,hmsc,awsc,mhome,maway,overp,hover,aover,denf,conc
    team1,team2 = 0,0

    #check winpower
    if(data1[0]>=50):
        team1 +=1
    if(data2[0]>=50):
        team2 +=1


    #check home and away win
    if(data1[2]>=50):
        team1 +=1
    if(data2[1]>=50):
        team2 +=1

    #check defnce
    if(data1[11]>=33):
        team1 +=1
    if(data2[11]>=33):
        team2 +=1


    #check goal power
    if(data1[3]>=67):
        team1 +=1
    if(data2[3]>=67):
        team2 +=1

    #check scored goals
    if(data1[6]>1):
        team1 +=1
    if(data2[7]>1):
        team2 +=1

    #check conceded goals
    if(data1[12]<1):
        team1 +=1
    if(data2[12]<1):
        team2 +=1
    #check h2h
    if(h2h[0]==team[0]):
        team1 +=3
    if(h2h[0]==team[1]):
        team2 +=3
    if(h2h[0]=="DC/DRAW"):

        team2 +=1
        team1 +=1
    #check win or loose

    if(team1 ==0 or team2==0):
        return("NODATA")
    if(team1>=team2):
        if((team1-team2)>5):
            return("1")
        else:
            return("1X")
    if(team2>=team1):
        if((team2-team1)>5):
            return("2")
        else:
            return("2X")

def tell_over(data,data1):

    hov0 = 0
    hov1 = 0
    hov2 = 0
    hov3 = 0
    hov4 = 0

    av = 0
    aov0 = 0
    aov1 = 0
    aov2 = 0
    aov3 = 0
    aov4 = 0

    #check home power

    if(type(data).__name__ !='list' or type(data1).__name__ !='list' ):
        return("XX")
    for i in data[0:3]:
        h,s = i.split(":")
        if(len(str(h))>0):
            h = int(h)
        else:
            h = 0

        if(h==1):
            hov0 +=1
        if(h==2):
            hov1 +=1
        if(h==3):
            hov2 +=1
        if(h>=4):
            hov3 +=1


    #check home power
    #print(data1)
    for i in data1[6:9]:
        h,s = i.split(":")
        if(len(str(s))>0):
            s = int(s)
        else:
            s = 0

        if(s==1):
            aov0 +=1
        if(s==2):
            aov1 +=1
        if(s==3):
            aov2 +=1
        if(s>=4):
            aov3 +=1

    v0 = hov0+aov0
    v1 = hov1+aov1
    v2 = hov2+aov2
    v3 = hov3+aov3
    v4 = hov4+aov4

    #check over
    cc = 0
    l,h = 0,max([v0,v1,v2,v3,v4])
    for i in [v4,v3,v2,v1,v0]:
        if(i !=0 and i==h):
            l = cc
        cc +=1

    tv = [v4,v3,v2,v1,v0]
    overman = ['OV2.5++','OV2.5','OV1.5++','OV1.5+','OV1.5']
    perp = round((tv[l]/3)*100)

    return (overman[l]+"|"+str(perp/2) +"%")


def tell_over1(tname1,tdata1,tname2,tdata2,h2h):
    #goalpower,h&a score,lowest score,h2h over2.5
    o1 = 0
    o2 = 0

    if(tdata1[2] !=0):
        o1 +=1
        if(tdata1[1]>=67 and tdata1[0]>=67):
            o1 +=1
    if(tdata2[2] !=0):
        o2 +=1
        if(tdata2[1]>=67 and tdata2[0]>=67):
            o2 +=1


    if((o1+o2)==4):
        return("OV2.5")
    if((o1+o2)==3):
        return("OV1.5")
    if((o1+o2)==2):
        return("OV0.5")
    if((o1+o2)>=5 ):
        return("OV3.5")
    if((o1+o2)<=1):
        return("UNder3.5")


def check_gg_pw(data1,data2):
    #win,denf1,hs1/aws2,gp1/gp2
    y = 0
    if(data1[0] != data2[0] or data2[0] != data1[0]):
        if(data1[1]<=25 and data2[1]<=25):

            y +=1
        if(data1[2]>=50 and data2[2]>=50):

            y +=1
        if(data1[3]>=50 and data2[1]>=50):
            y +=1
    if(y<2):
        return('''X''')
    if(y>=2):
        return('''&#x2714''')




def sure_games(win,data1,data2):
    #0.winp,1.awinp,2.hwinp,3.gp,4.hmsc,5.awsc,6.mhome,7.maway,8.overp,9.hover,10.aover,11.denf,12.conc
    ggs = check_gg_pw([data1[0],data1[11],data1[4],data1[3]],[data2[0],data2[11],data2[5],data2[3]])
    su = 0

    if(win=="1X" or win=="1"):
        #if((data1[0]>data2[0]) and (data1[11]>data2[11]) and (data1[2]>data2[1]) and (data1[4]>data2[5]) and (data1[3]>data2[3])):


        if((data1[11]>data2[11]) and ((data1[11]-data2[11])>=20)):#defence
            su +=1
            if((data1[0]>data2[0]) and ((data1[0]-data2[0])>=20)):#winpower
                su +=1
            if((data1[2]>data2[1]) and ((data1[2]-data2[1])>=20)):#home/away win power
                su +=1
            if((data1[12]<data2[12])):# conceal goal
                su +=1
            if(data1[3]>67):#score power
                su +=1
            if((data1[4]>67)): #home score
                su +=1
            if((data1[6]>=1)):
                su +=1

    if(win=="2X" or win=="2"):
        #0.winp,1.awinp,2.hwinp,3.gp,4.hmsc,5.awsc,6.mhome,7.maway,8.overp,9.hover,10.aover,11.denf,12.conc


        if((data2[11]>data1[11]) and ((data2[11]-data1[11])>=20)):#defence
            su +=1
            if((data2[0]>data1[0]) and ((data2[0]-data1[0])>=20)):#winpower
                su +=1
            if((data2[1]>data1[2]) and ((data2[1]-data1[2])>=20)):#home/away win power
                su +=1

            if((data2[12]<data1[12])):# conceal goal
                su +=1
            if(data1[3]>67):#score power
                su +=1
            if((data1[5]>67)): #home score
                su +=1
            if((data1[7]>=1)):
                su +=1



    if(su<5):
         return('''<span class="w3-text-red ">RISKY %s</span>'''%(ggs),0)
    if(su>=5 and su<7):
        return('''<span class="w3-text-green ">SAFE %s</span>'''%(ggs),0)
    if(su==7):
        return('''<span class="w3-text-green  ">SURE %s</span>'''%(ggs),0)
    else:
        return('''<span class="w3-text-red w3-serif ">RISKY %s</span>'''%(ggs),0)











def randit(data):
    file = open("tickeks.html","w")
    tn = round(len(data)/3)
    tick = []
    i = 0
    tem = []
    while(i<tn):

        for ii in range(3):
            p = randint(0,len(data)-1)
            p = data[p]
            tem.append(p)
        file.write("<h4>TICKEK START <br></h4>")

        file.write("<ul>")


        for u in tem:
            y ="<li> %s </li>"%(u)
            file.write(y)
        file.write("</ul>")
        file.write("<h4>TICKEK END <br><br></h4>")
        tem.clear()


        i+=1

    file.write("<h4>TICKEK START COMBO WIN <br></h4>")
    file.write("<ul>")
    for u in data:
        y ="<li> %s </li>"%(u)
        file.write(y)
    file.write("</ul>")
    file.write("<h4>TICKEK END <br><br></h4>")
    file.close()





def wisebotman(data1,data2):
    #winp,awinp,hwinp,gp,hmsc,awsc,mhome,maway,overp,hover,aover,denf,conc

    v1 = 0

    if(data2[11]<=25  and data1[11]<=25):
        v1 +=1
    if(data2[3]>=58  and data1[3]>=58):
        v1 +=1







    if(v1==2):
        return(1)
    if(v1!=2):
        return(0)




def strong_at(hm,aw):
    if(hm>=aw):
        return "HOME"
    else:
        return "AWAY"





















