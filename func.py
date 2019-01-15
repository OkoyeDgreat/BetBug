#-------------------------------------------------------------------------------
# Name:        mfunctions collection
# Purpose:      this is a module that is developed by embassy to be
#               ulitmate collection for micro and brain repleical
#               of human brain for betting
# Author:      embassy
#
# Created:     22/09/2017
# Copyright:   (c) embassy 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from conc_goal import *
from collections import Counter








def check_over_goal(data):
    hov2 = 0
    aov2 = 0
    for i in data[0:6]:
        h,s = i.split(":")
        if(len(str(h))>0):
            h = int(h)
        else:
            h = 0
        if(len(str(str(s)))>0):
            s = int(s)
        else:
            s = 0


        if(h+s>=3):
            hov2 +=1
        else:
            pass

    for i in data[6::]:
        h,s = i.split(":")
        if(len(str(h))>0):
            h = int(h)
        else:
            h = 0
        if(len(str(str(s)))>0):
            s = int(s)
        else:
            s = 0

        if(h+s>=3):
            aov2 +=1
        else:
            pass
    hm2 =round((hov2/6)*100)
    aw2 = round((aov2/6)*100)
    pv2 = round(((aov2+hov2)/12)*100)

    return(hm2,aw2,pv2)


def h2h_check(data):
    t1 = ''
    t2 = ''
    scores = []
    over2 = 0

    twin1 = 0
    twin2 = 0
    draw =  0
    dty = type(data)
    if(dty.__name__ !='list'):
        return("ER","ER","ER")

    if(len(data)<1):
        return("0","0","0")
    a = data[0].split(":")
    t1 = a[0]
    t2 = a[2]
    for i in data:
        i = i.split(":")
        if(i[0]==t1):
            if(int(i[1])>int(i[3])):
                twin1 +=1
                if(int(i[1])+int(i[3])>=3):
                    over2 +=1
            if(int(i[1])<int(i[3])):
                twin2 +=1
                if(int(i[1])+int(i[3])>=3):
                    over2 +=1
            if(int(i[1])==int(i[3])):
                draw +=1
                if(int(i[1])+int(i[3])>=3):
                    over2 +=1

    for i in data:
        i = i.split(":")
        if(i[2]==t1):
            if(int(i[3])>int(i[1])):
                twin1 +=1
                if(int(i[1])+int(i[3])>=3):
                    over2 +=1
            if(int(i[3])<int(i[1])):
                twin2 +=1
                if(int(i[1])+int(i[3])>=3):
                    over2 +=1
            if(int(i[3])==int(i[1])):
                draw +=1
                if(int(i[1])+int(i[3])>=3):
                    over2 +=1

    winT = ''
    pent = 0
    if(twin1>twin2 and twin1>draw):
        winT=t1
        pent = round((twin1/len(data))*100)

    if(twin2>twin1 and twin2>draw):
        winT=t2
        pent = round((twin2/len(data))*100)

    if(twin1<=draw and twin2<=draw):
        winT="DC/DRAW"
        pent = round(((draw)/len(data))*100)
    if((twin2==twin1 or twin1==twin2)  and (twin2>draw or twin1>draw)):
        winT="DC"
        pent = round(((twin1+twin2)/len(data))*100)

    over2 = round((over2/len(data))*100)




    return(winT,pent,over2)



def check_team_powers(data):
    den = 12
    a_win,h_win,a_draw,h_draw,h_lose,a_lose,goal_h,goal_h,goal_h,goal_h= 0,0,0,0,0,0,0,0,0,0
    goal_h = []
    goal_a = []
    goal = 0
    hdraw = 0
    adraw = 0
    power_side = "HOME"

    if(len(str(data))<6):
        return(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    #print(data)
    conc = goal_conc(data)

    #scrap for home games
    for i in data[0:6]:
        h_s,a_s = i.split(":")
        if(len(str(h_s))>0):
            h_s = int(h_s)
        else:
            h_s = 0
        if(len(str(str(a_s)))>0):
            a_s = int(a_s)
        else:
            a_s = 0

        if(h_s>a_s):
            h_win +=1
            goal_h.append(h_s)
            if(h_s !=0):
                goal +=1
            if(a_s !=0):
                den -=1
        if(h_s<a_s):
            h_lose +=1
            goal_h.append(h_s)
            if(h_s !=0):
                goal +=1
            if(a_s !=0):
                den -=1
        if(h_s==a_s):
            h_draw +=1
            goal_h.append(h_s)
            if(h_s !=0):
                goal +=1
            if(a_s !=0):
                den -=1

    #scrap for AWAY games
    for i in data[6::]:
        h_s,a_s = i.split(":")
        if(len(str(h_s))>0):
            h_s = int(h_s)
        else:
            h_s = 0
        if(len(str(str(a_s)))>0):
            a_s = int(a_s)
        else:
            a_s = 0

        if(a_s>h_s):
            a_win +=1
            goal_a.append(a_s)
            if(a_s !=0):
                goal +=1

            if(h_s !=0):
                den -=1
        if(a_s<h_s):
            a_lose +=1
            goal_a.append(a_s)
            if(a_s !=0):
                goal +=1
            if(h_s !=0):
                den -=1

        if(a_s==h_s):
            a_draw +=1
            goal_a.append(a_s)
            if(a_s !=0):
                goal +=1
            if(h_s !=0):
                den -=1

    #print(data)
    #calu hwin,away win, win_power
    hwinp = round((h_win)/6*100)
    adraw = round((a_draw)/6*100)
    hdraw = round((h_draw)/6*100)
    awinp = round((a_win)/6*100)
    winp =round(((h_win+a_win)/12)*100)
    #drawp = round((h_draw+a_draw)/12*100)
    gp  = round((goal)/12*100)

    hmsc = 0
    for i in goal_h:
        if(i !=0):
            hmsc +=1
    #home score pw
    hmsc = round((hmsc)/6*100)

    awsc = 0
    for i in goal_a:
        if(i !=0):
            awsc +=1
    #away score pw
    awsc = round((awsc)/6*100)

    #CHECK FOR MINI SCORE
    #sure home
    #print(Counter(goal_h))
    shms = Counter(goal_h)
    shms2 = 0
    mhome = 0

    for i in shms:
        if(shms[i]>shms2):
            shms2 = shms[i]
            mhome=i

        else:
            pass
    #print(mhome)


    #sure away
    #print(Counter(goal_a))
    shms = Counter(goal_a)
    shms2 = 0
    maway = 0
    for i in shms:

        if(shms[i]>shms2):
            shms2 = shms[i]
            maway=i
        else:
            pass
    hover,aover,overp = check_over_goal(data)

    #scrape defence power
    denf = round((den/12)*100)


    if(adraw<1):
        adraw = 0
    if(hdraw<0):
        hdraw = 0;






    #print((winp,awinp,hwinp,gp,hmsc,awsc,mhome,maway,overp,hover,aover,denf))
    return(winp,awinp,hwinp,gp,hmsc,awsc,mhome,maway,overp,hover,aover,denf,hdraw,adraw,conc)

'''
def check_gg(data1,data2):
    #0.winp,1.awinp,2.hwinp,3.gp,4.hmsc,5.awsc,6.mhome,7.maway,8.overp,9.hover,10.aover,11.denf,12.conc
    gg = 0


    if(data1[3]>=67 and data2[11]<33 and data1[4]>=67 and data2[12]>=1 and data1[6]>=1):
        gg +=1
    if(data2[3]>=67 and data1[11]<33 and data2[5]>=67 and data1[12]>=1 and data2[7]>=1):
        gg +=1

    if(gg==2):
        return("GG")
    if(gg<2):
        return("NG")
'''


def check_gg(data1,data2):

    #0.winp,1.awinp,2.hwinp,3.gp,4.hmsc,5.awsc,6.mhome,7.maway,8.overp,9.hover,10.aover,11.denf,12.conc
    #0winp,1awinp,2hwinp,3gp,4hmsc,5awsc,6mhome,7maway,8overp,9hover,10aover,11denf,12 hdraw,13 adraw,14conc
    gg = 0

    #check win
    if(data1[0] >=25 and data2[0]>=25):
        gg +=1
    else:
       return("")

    #check defence
    if(data1[11] <=25 and data2[11] <=25):
        gg +=1
    else:
        return("")

    #check home and away win
    if(data1[2] >=33 and data2[1]>=33):
        gg +=1
    else:
        pass

    #score
    if(data1[3] >=67 and data2[3]>=67):
        gg +=1
    else:
        gg -=1


    #home and away score
    if(data1[4] >=67 and data2[5]>=67):
        gg +=1
    else:
        gg -=1


    retu =round((gg/5)*100)

    n = "GG|"+str(retu)+"%"

    return n





def result_possible(data):
    pass



















