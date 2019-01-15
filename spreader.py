#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      embassy
#
# Created:     23/09/2017
# Copyright:   (c) embassy 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from fetch_event import *
from func import *
from engine import *
from datetime import *

#winp,awinp,hwinp,gp,hmsc,awsc,mhome,maway,overp,hover,aover
#(winT,pent,over2)


clubs = [] #list for teams
teams_data = [] #list for teams datas

rlist = []   #list for random games


def load_teams_back():
    temp = []
    file = open("./data/vmatch.txt","rb")
    temp = pickle.load(file)
    for i in temp:
        clubs.append([i[0],i[2]])
    file.close()
    return 0;

def teams_back():
    global teams_data
    file = open("./data/teams_data.txt","rb")
    teams_data = pickle.load(file)
    file.close()
    return 0;



load_teams_back()
teams_back()




def write_it():
    file = datetime.now().strftime('%Y-%m-%d')
    filename = "./output/"+file+"-prediction-"+".html"
    filenamed = "./output/"+file+"-prediction-DRAW"+".html"
    #filenameo1 = "./output/"+file+"-prediction-OV1.5"+".html"
    #filenameo2 = "./output/"+file+"-prediction-Ov2.5"+".html"
    fi = open(filename,"wt")
    fi1 = open(filenamed,"wt")
    #fi2 = open(filenameo1,"wt")
    #fi3= open(filenameo2,"wt")
    ovm = "./output/overmarket.html"
    fi2 = open(ovm,"wt")
    print(len(clubs),"MATCHES TODAY")
    count = 0
    print('''<html>
    <head><title>PHOENIX PREDITION HELPER (BETBUG.COM.NG)</title>
    <link rel="stylesheet" type="text/css" href="w3.css">
    <link rel="stylesheet" type="text/css" href="css/font-awesome.min.css">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0"/>

    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-126105969-1"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'UA-126105969-1');
    </script>
    <script async="async" data-cfasync="false" src="//tharbadir.com/2?z=2075496"></script>

    </head>
    <body >


    ''',file=fi)
    print('<div class="" style="overflow-x:auto;height:100%">',file=fi)
    print('''<table
    class="w3-table-all w3-centered w3-serif w3-hide-small w3-hide-medium " border=1.5  width=95%% cellpadding=1 cellspacing=1>''',file=fi)
    #return(winp,awinp,hwinp,gp,hmsc,awsc,mhome,maway,overp,hover,aover,denf,hdraw,adraw,conc)
    #(winT,pent,over2)


    for i in teams_data:

        w1,aw1,hw1,gp1,hs1,aws1,mh1,ma1,op1,hop1,aop1,denf1,hdraw1,adraw1,con1=check_team_powers(i[0])
        w2,aw2,hw2,gp2,hs2,aws2,mh2,ma2,op2,hop2,aop2,denf2,hdraw2,adraw2,con2=check_team_powers(i[1])
        h2hw,h2hp,h2ho = h2h_check(i[2])
        #over = tell_over(clubs[count][0],[gp1,hs1,mh1],clubs[count][1],[gp2,aws2,mh2],[h2hp,h2ho])
        over = tell_over(i[0],i[1])
        gg = check_gg(check_team_powers(i[0]),check_team_powers(i[1]))
        #data1,data2,h2h,team
        win = check_win(check_team_powers(i[0]),check_team_powers(i[1]),h2h_check(i[2]),clubs[count])
        #print(clubs[count])
        sure = sure_games(win,check_team_powers(i[0]),check_team_powers(i[1]))
        wi = wisebotman(check_team_powers(i[0]),check_team_powers(i[1]))
        if(gp1==gp2 and hs1==hs2 and aws1==aws2 and con1==con2):

            print("%s vs %s <br>"%(clubs[count][0],clubs[count][1]),file=fi1)
        #add for over 1.5


        if(wi==1 and (over !="UNder3.5" and over !="OV0.5")):
            print(clubs[count][0],"vs",clubs[count][1],"-->>",win,"-",over,"-",gg,"<br>",file=fi2)
        #large -
        print('''<tr align=center class="w3-black w3-tiny w3-hide-small w3-hide-medium ">
        <th>Teams<br>H-A</th><th>Outcomes<br> </th><th>WIN POWER<br>H-A</th><th>DEFENCE<br>H-A</th>
        <th>H/Strength<br>H-A</th><th>A/Strength<br>H-A</th><th>HOME DRAW<br>H-A</th><th>AWAY DRAW<br>H-A</th><th>Goal/Strength<br>H-A</th><th>HOME-SCORE<br>H-A</th>
        <th>AWAY-SCORE<br>H-A</th><th>L.est Home-GOAL<br>H-A</th><th>L.EST AWAY-GOAL<br>H-A</th><th>Mst.concealed-GOAL<br>H-A</th>
        <th>OVER 2.5 <br>H-A</th><th>H.Over 2.5<br>H-A</th><th>AW. Over2.5<br>H-A</th><th>H2H OUTCOME<br>H-A</th>
        <th>H2H To Win POWER<br>H-A</th><th>H2H Over 2.5<br>H-A</th>
        </tr>''',file=fi)




        #large
        print("<tr align=center class='w3-medium w3-white w3-hover-text-green w3-hover-border-red w3-hide-small w3-hide-medium'>",file=fi)
        print('''<td>%s vs %s </td><td>%s,%s,%s-%s</td><td>%s%%-%s%%</td><td>%s%%-%s%%</td>
        <td>%s%%-%s%%</td><td>%s%%-%s%%</td><td>%s%%-%s%%</td><td>%s%%-%s%%</td><td>%s%%-%s%%</td><td>%s%%-%s%%</td>
        <td>%s%%-%s%%</td><td>%s-%s</td><td>%s-%s</td><td>%s-%s</td>
        <td>%s%%-%s%%</td><td>%s%%-%s%%</td><td>%s%%-%s%%</td><td>%s</td>
        <td>%s%%</td><td>%s%%</td>'''
        %(clubs[count][0],clubs[count][1],win,over,gg,sure[0],w1,w2,denf1,denf2,hw1,hw2,aw1,aw2,hdraw1,hdraw2,adraw1,adraw2,gp1,gp2,hs1,hs2,
        aws1,aws2,mh1,mh2,ma1,ma2,con1,con2,op1,op2,hop1,hop2,aop1,aop2,h2hw,h2hp,h2ho),file=fi)

        print('''<div class=" w3-black w3-border w3-container w3-center w3-serif w3-xlarge w3-hide-large">
        <div class=" w3-center w3-serif " style="font-weight:bold;" >
        <h4 class="w3-white">Teams</h4><span>%s vs %s </span>
        <h4 class="w3-green " style="font-weight:bold;">Outcome(s)</h4><span>%s %s %s</span>
        <h4 class="w3-green " style="font-weight:bold;">confidence </h4><span class=" w3-serif">%s</span>
        <h4 class="w3-green " style="font-weight:bold;">WIN POWER </h4><span>%s%% &emsp; - &emsp; %s%%</span>
        <h4 class="w3-green " style="font-weight:bold;">DEFENCE </h4><span>%s%% &emsp; - &emsp; %s%%</span>
        <h4 class="w3-green " style="font-weight:bold;">Goal/Strength</h4><span>%s%% &emsp; - &emsp; %s%%</span>
        <h4 class="w3-green " style="font-weight:bold;">BEST PERFORMANCE </h4><span>%s &emsp; - &emsp; %s</span>

        </div></div>'''%(clubs[count][0],clubs[count][1],win,over,gg,sure[0],w1,w2,denf1,denf2,gp1,gp2,strong_at(hw1,aw1),strong_at(hw2,aw2)),file=fi)



        tdata ='''%s vs %s ---- %s,%s,%s'''%(clubs[count][0],clubs[count][1],win,over,gg)
        #print(tdata)
        if(sure[1]==1):
            rlist.append(tdata)
        count +=1

        print("</tr>",file=fi)
        #add for draw


    print("<tr></tr>",file=fi)
    print("</table></div></body></html>",file=fi)







    fi.close()
    fi2.close()
    print("DONE WRITTEN FILE TO ",fi.name)

    return(0)


write_it()











