from re import *
import pickle
from collections import Counter



def team_force(team,side):
    hw = 0
    hd = 0
    hl = 0
    aw = 0
    ad = 0
    al = 0
    hs = 0
    aws = 0
    avs  = []



    for i in team:
        h,a = i.split("-")
        h,a = int(h),int(a)

        #check home win
        if(side[team.index(i)]==1):
            if(h>a):
                hw +=1
                if(h !=0):
                    hs+=1
                    avs.append(h)
                else:
                    avs.append(h)
            if(h==a):
                hd +=1
                if(h !=0):
                    hs+=1
                    avs.append(h)
                else:
                    avs.append(h)
            if(h<a):
                hl +=1
                if(h !=0):
                    hs+=1
                    avs.append(h)
                else:
                    avs.append(h)



        #check away win
        if(side[team.index(i)]==2):
            if(a>h):
                aw +=1
                if(a !=0):
                    aws +=1
                    avs.append(a)
                else:
                    avs.append(a)
            if(a==h):
                ad +=1
                if(a !=0):
                    aws +=1
                    avs.append(a)
                else:
                    avs.append(a)
            if(a<h):
                al +=1
                if(a !=0):
                    aws +=1
                    avs.append(a)
                else:
                    avs.append(a)

    if(len(team)==0):
        return(0,0,0,0,"ERROR",0)
    hmp =round((hw/len(team))*100)
    awp = round((aw/len(team))*100)
    winp = round(((hw+aw)/len(team))*100)
    scp = round(((hs+aws)/len(team))*100)

    sms = "NONE"
    if(hs>aws):
        sms="HOME"
    else:
        sms = "AWAY"

    sus = Counter(avs)
    sus2 = 0
    ss = 0
    for i in sus:
        if(sus[i]>sus2):
            sus2 = sus[i]
            ss=i
        else:
            pass


    return(hmp,awp,winp,scp,sms,ss)












