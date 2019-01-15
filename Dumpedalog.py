def tell_win(tname1,tdata1,tname2,tdata2,h2h):
    #win,h&a win,goal power,h&a goal power,h2h win team
    t1 = 0
    t2 = 0


    #win power
    if(tdata1[0]>tdata2[0]):
        t1 +=1
    if(tdata1[0]<tdata2[0]):
        t2 +=1
    if(tdata1[0]==tdata2[0]):
        t1 +=1
        t2 +=1

    #home and away win
    if(tdata1[1]>tdata2[1]):
        t1 +=1
    if(tdata1[1]<tdata2[1]):
        t2 +=1
    if(tdata1[1]==tdata2[1]):
        t1 +=1
        t2 +=1

    #home goal power and away goal power
    if(tdata1[2]>tdata2[2]):
        t1 +=1
    if(tdata1[2]<tdata2[2]):
        t2 +=1
    if(tdata1[2]==tdata2[2]):
        t1 +=1
        t2 +=1

    #home score and away score
    if(tdata1[3]>tdata2[3]):
        t1 +=1
    if(tdata1[3]<tdata2[3]):
        t2 +=1
    if(tdata1[3]==tdata2[3]):
        t1 +=1
        t2 +=1
    #defence check
    if(tdata1[4]>=42):
        t1 +=2
    if(tdata2[4]>=42):
        t2 +=2


    if(t1>t2):
        sc = round(t1/2)
        if(sc>3):
            return("1")
        else:
            return("1X")
    if(t1<t2):
        sc = round(t2/2)
        if(sc>3):
            return("2")
        else:
            return("2X")

    if(t1==t2):
        return("X")




def tell_gg(tname1,tdata1,tname2,tdata2):
    #goal power,home and away score ,home and away lowest scores
    t1 = 0
    t2 = 0
    if(tdata1[2] !=0):
        t1 +=1
        if(tdata1[1]>=67 and tdata1[0]>=67):
            t1 +=1
    if(tdata2[2] !=0):
        t2 +=1
        if(tdata2[1]>=67 and tdata2[0]>=67):
            t2 +=1
    if(t1==t2):
        return("GG")
    if(t1>=1 and t2>=1):
        return("GG")

    else:
        return("NG")




def check_win(data1,data2,h2h,team):
    #winp,awinp,hwinp,gp,hmsc,awsc,mhome,maway,overp,hover,aover,denf,conc
    team1,team2 = 0,0

    #check winpower
    if(data1[0]>=data2[0]):
        team1 +=1
    if(data2[0]>=data1[0]):
        team2 +=1


    #check home and away win
    if(data1[2]>=data2[1]):
        team1 +=1
    if(data2[1]>=data1[2]):
        team2 +=1

    #check defnce
    if(data1[11]>=data2[11]):
        team1 +=1
    if(data2[11]>=data1[11]):
        team2 +=1


    #check goal power
    if(data1[3]>=data2[3]):
        team1 +=1
    if(data2[3]>data1[3]):
        team2 +=1

    #check scored goals
    if(data1[6]>=data2[7]):
        team1 +=1
    if(data2[7]>=data1[6]):
        team2 +=1

    #check conceded goals
    if(data1[12]<data2[12]):
        team1 +=1
    if(data2[12]<data1[12]):
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
        return("CASTER")
    if(team1>=team2):
        if((team1-team2)>4):
            return("1")
        else:
            return("1X")
    if(team2>=team1):
        if((team2-team1)>4):
            return("2")
        else:
            return("2X")













#check win 2

def check_win(data1,data2,h2h,team):
    #winp,awinp,hwinp,gp,hmsc,awsc,mhome,maway,overp,hover,aover,denf,conc
    team1,team2 = 0,0

    #check winpower
    if(data1[0]>=25):
        team1 +=1
    if(data2[0]>=25):
        team2 +=1


    #check home and away win
    if(data1[2]>=50):
        team1 +=1
    if(data2[1]>=50):
        team2 +=1

    #check defnce
    if(data1[11]>=50):
        team1 +=1
    if(data2[11]>=50):
        team2 +=1


    #check goal power
    if(data1[3]>=67):
        team1 +=1
    if(data2[3]>=67):
        team2 +=1

    #check scored goals
    if(data1[6]>=1):
        team1 +=1
    if(data2[7]>=1):
        team2 +=1

    #check conceded goals
    if(data1[12]<=1):
        team1 +=1
    if(data2[12]<=1):
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
        return("CASTER")
    if(team1>=team2):
        if((team1-team2)>4):
            return("1")
        else:
            return("1X")
    if(team2>=team1):
        if((team2-team1)>4):
            return("2")
        else:
            return("2X")


###############################################


def org_games():
    #teams_data
    #clubs
    #winp,awinp,hwinp,gp,hmsc,awsc,mhome,maway,overp,hover,aover
    #(winT,pent,over2)
    w1,aw1,hw1,gp1,hs1,aws1,mh1,ma1,op1,hop1,aop1= check_team_powers(teams_data[9][0])
    w2,aw2,hw2,gp2,hs2,aws2,mh2,ma2,op2,hop2,aop2= check_team_powers(teams_data[9][1])
    h2hw,h2hp,h2ho = h2h_check(teams_data[9][2])
    #print(tell_over(clubs[9][0],[gp1,hs1,mh1],clubs[12][1],[gp2,aws2,mh2],[h2hp,h2ho]))
    #print(tell_gg(clubs[9][0],[gp1,hs1,mh1],clubs[9][1],[gp2,aws2,ma2]))
    #print(tell_win(clubs[9][0],[w1,hw1,gp1,hs1],clubs[12][1],[w2,aw2,gp2,aws2],[h2hp,h2ho]))
    #print(clubs[9][0],clubs[9][1])


    file = datetime.now().strftime('%Y-%m-%d')
    filename = "./output/"+file+".html"


    count = 0
    print('''<html>
    <head><title>PHOENIX PREDITION HELPER</title>
    <script src="./css/jquery.min.js"></script>
    <script src="./css/jquery.modal.js" type="text/javascript" charset="utf-8"></script>
    <link rel="stylesheet" href="css/jquery.modal.css" type="text/css" media="screen" />
    <link rel="stylesheet" type="text/css" href="./css/w3.css">

    </head>
    <body>''',file=fi)
    print('''<table
    class="w3-table-all w3-centered   w3-serif w3-animate-right " border=1.5  width=100%% >''',file=fi)







    #the looper man
    for i in teams_data:
        print('''<tr class="w3-black   w3-small">
        <td>TEAMS</td>
        <td>WIN</td>
        <td>GOAL GOAL (BTTS)</td>
        <td>OVER</td>
        <td>TEAMS STATS</td></tr>''',file=fi)

        #functions calls
        w1,aw1,hw1,gp1,hs1,aws1,mh1,ma1,op1,hop1,aop1=check_team_powers(i[0])
        w2,aw2,hw2,gp2,hs2,aws2,mh2,ma2,op2,hop2,aop2=check_team_powers(i[1])
        h2hw,h2hp,h2ho = h2h_check(i[2])
        over = tell_over(clubs[count][0],[gp1,hs1,mh1],clubs[count][1],[gp2,aws2,mh2],[h2hp,h2ho])
        gg= tell_gg(clubs[count][0],[gp1,hs1,mh1],clubs[count][1],[gp2,aws2,ma2])
        win = tell_win(clubs[count][0],[w1,hw1,gp1,hs1],clubs[count][1],[w2,aw2,gp2,aws2],[h2hp,h2ho])


        #url and html decoration
        link = '''<p><a href="#id%s" rel="modal:open">TEAMS STATS</a></p>'''%(count)



        print('''<tr  class='w3-striped w3-medium w3-white w3-hover-text-green  w3-hover-border-red'>''',file=fi)

        td = '''<td>%s vs %s </td><td>%s</td><td>%s</td><td>%s</td>
        <td>%s</td><'''%(clubs[count][0],clubs[count][1],win,gg,over,link)




        modal ='''
        <div id="id%s" style="display:none;">
        <p>gdgdhdh</p>
        </div>
        '''%(str(count))

        print(modal,file=fi)
        print(td,file=fi)
        print("</tr>",file=fi)




        count +=1

    print("</table></body></html>",file=fi)





    fi.close()
    print("DONE WRITTEN FILE TO re.Txt")
    return(0)











