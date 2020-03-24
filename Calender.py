from dateutil.parser import parse

calender1=[["10:30","11:30"],["12:30","13:00"],["15:30","16:30"]]
calender2=[["11:30","12:30"],["14:00","15:00"],["15:30","17:00"]]
dailybound1 = ["8:00","17:00"]
dailybound2 = ["9:00","19:00"]
combined=[]
calender = []
avaliable_times=[]
time = 1

def mush(calender1,calender2,dailybound1,dailybound2,P):
    calender1.insert(0,["0:00",dailybound1[0]])
    calender1.append([dailybound1[1],"23:59"])
    calender2.insert(0,["0:00",dailybound2[0]])
    calender2.append([dailybound2[1],"23:59"])
    
    
    C= 0
    for j in range(len(calender1)):
        if greaterthan(calender1[j][0],calender2[j][0]) == -1:
            for i in range(len(calender1)-P):
                if greaterthan(calender1[i+P][1],calender2[j][1]) == -1:
                    calender.append(calender1[i+P])
                    C+=1
                elif greaterthan(calender1[i+P][1],calender2[j][1]) == 0:
                    calender.append(calender1[i+P])
            P = C
            calender.append(calender2[j])
        if greaterthan(calender1[j][0],calender2[j][0]) == 0:
            for i in range(len(calender1)-P):
                if greaterthan(calender1[i+P][1],calender2[j][1]) == -1:
                    calender.append(calender1[i+P])
                    C+=1         
            P = C
            calender.append(calender2[j])
        
                
    
    
def greaterthan(time1,time2):
    time1 = parse(time1)
    time2 = parse(time2)
    time1 = int(time1.hour) * 60 + int(time1.minute)
    time2 = int(time2.hour) * 60 + int(time2.minute)
    if time1 > time2:
        return 1
    if time2 > time1:
        return -1
    if time2 == time1:
        return 0

def optimize(calender):
    i = 0
    while i<(len(calender)-1):   
        if greaterthan(calender[i][1],calender[i+1][0]) == 1:
            if greaterthan(calender[i][1],calender[i+1][1]) == -1:
                calender[i][1] = calender[i+1][1]
                calender.pop(i+1)
                i -= 1
        elif greaterthan(calender[i][0],calender[i+1][0]) == 1:
            break
            calender.pop(i)
            i -= 1
        if greaterthan(calender[i][1],calender[i+1][0]) == 0:
            calender[i][1] = calender[i+1][1]
            calender.pop(i+1)
            i -= 1
        i += 1

def avaliable(calender, time):
    for i in range(len(calender)-1):
        time1 = parse(calender[i][1])
        time2 = parse(calender[i+1][0])
        time1 = int(time1.hour) * 60 + int(time1.minute)
        time2 = int(time2.hour) * 60 + int(time2.minute)
        if time2 - time1 >= time:
            if (calender[i][1], calender[i+1][0]) not in avaliable_times:
                avaliable_times.append((calender[i][1], calender[i+1][0]))
        
def computeAvaliableTimes(calender1,calender2,time,dailybound1,dailybound2):
    mush(calender1,calender2,dailybound1,dailybound2,0)
    optimize(calender)
    avaliable(calender, time)
    print(avaliable_times)

computeAvaliableTimes(calender1,calender2,time,dailybound1,dailybound2)
    
