import pandas as pd
import random

def timetable(data = str):

    data = pd.read_csv(data)

    # Creating an empty timetable

    days = ['Mon','Tue','Wed','Thur','Fri']
    numberList,eight,nine,ten,eleven,twelve,one,two,three,four,five,six = [],[],[],[],[],[],[],[],[],[],[],[]
    daysC = 0
    daysList = []
    for i in range(5):
        numberList.append(i + 1)
        eight.append(' ') ,nine.append(' '),ten.append(' '),eleven.append(' '),twelve.append(' '),
        one.append(' '),two.append(' '),three.append(' '),four.append(' '),five.append(' '),six.append(' ')

        daysList.append(days[daysC])
        daysC += 1
        if daysC == 5:
            daysC = 0


    # A dictionary of lists
    dict = {'Number': numberList, "Days": daysList, "08:00am": eight, '09:00am':nine,"10:00am":ten, '11:00am':eleven,'12:00pm':twelve, '01:00pm':one, '02:00pm':two, '03:00pm':three, '04:00pm':four, '05:00pm':five, '06:00pm':six}

    df = pd.DataFrame(dict)

    # Convert the lists in string to list

    scn,n,k,y,c = 0,0,0,0,0
    choiceList,ncl = [0,1,2,3,4],[]

    for i in choiceList:
            if len(ncl) != 5:
                    choice = random.choices(choiceList, k=5)
                    for v in choice:
                            if v not in ncl:
                                    ncl.append(v)
            else:
                    break
    while True:
            for i in data['Courses']:
                    scn = ncl[c]
                    ecn = scn + 1
                    d = data.loc[data['Courses']== str(i)]
                    if list(d['Units'])[0]:
                            srn = random.randint(2,12)
                            if list(d['Units'])[0] == 2 and srn > 11:
                                    srn = srn - 1
                            elif list(d['Units'])[0] == 3 and srn > 10:
                                    srn = srn - 2
                            ern = srn + list(d['Units'])[0]
                            df.iloc[scn:ecn,srn:ern] = str(i)
                    k += 1
                    if k == 10:
                            y+=1
                            print(y)
                            print(df.to_markdown(), '\n')
                            df.to_csv('timetableResult.csv', mode='a')
                            df = pd.DataFrame(dict)
                            k=0
                    c += 1
                    if c == 5:
                            c = 0
            n +=1
            if n == 1:
                    break
timetable(data='courseUnitData.csv')