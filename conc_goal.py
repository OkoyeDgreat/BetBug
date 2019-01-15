#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      embassy
#
# Created:     08/10/2017
# Copyright:   (c) embassy 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from collections import Counter



def goal_conc(data):
    o0 = 0
    o1 = 0
    o2 = 0
    o3 = 0
    o4 = 0
    o5 = 0


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
        #checking for goals
        if(s==0):
            o0 +=1
        if(s==1):
            o1 +=1
        if(s==2):
            o2 +=1
        if(s==3):
            o3 +=1
        if(s==4):
            o4 +=1
        if(s>=5):
            o5 +=1


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

        #checking for goals
        if(h==0):
            o0 +=1
        if(h==1):
            o1 +=1
        if(h==2):
            o2 +=1
        if(h==3):
            o3 +=1
        if(h==4):
            o4 +=1
        if(h>=5):
            o5 +=1
    li = []
    for i in [o0,o1,o2,o3,o4,o5]:
        li.append(i)

    #check highest conce
    msc = 0
    psc = li[0]
    co = li.index(psc)

    for i in li:
        if(psc<i):
            psc = i
            co = li.index(i)


    #print(o0,o1,o2,o3,o4,o5)

    return co
