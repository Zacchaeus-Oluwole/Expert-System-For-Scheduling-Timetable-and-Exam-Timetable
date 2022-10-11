import pandas as pd
import ast
from datetime import datetime,date, timedelta

presentday = datetime.now() # Get today's date or presentday = datetime.today()

def startingDay(oDate=str) -> int: #Function to find number of days between two given dates    
    Today = presentday.strftime('%Y%m%d') # strftime() is to format date according to # the need by converting them to string
    Year = int(Today[0:4])
    Month = int(Today[4:6])
    Day = int(Today[6:8])
    oYear = int(oDate[0:4])
    oMonth = int(oDate[4:6])
    oDay = int(oDate[6:8])

    d0 = date(Year,Month,Day)
    d1 = date(oYear,oMonth,oDay)
    
    delta = d1 - d0 #days between two given dates

    return delta.days #return difference between two dates

def examTimetable(data = str, startingDate = str, examsPerPeriod = int, divisor=0)-> str:

    data = pd.read_csv(data)
    data = data.drop(columns = ['Unnamed: 0'])
    numberList,daysList,dateList = [],[],[]

    timeTable =  { 
            'Number': numberList,
            "Days": daysList,
            'Date': dateList,
            "Morning\n\n08:00am 09:00am 10:00am 11:00am":[], 
            "Afternoon\n\n11:30am 12:30pm 01:30pm 02:30pm":[], 
            "Evening\n\n03:00pm 04:00pm 05:00pm 06:00pm":[]
        }
    

    datasInSet = set()
    for value in data['Courses']:
        listOfStrings = ast.literal_eval(value) #Convert the list in string to a list of strings
        for v in listOfStrings:
            datasInSet.add(v)
    counter = 0
    for value in datasInSet:
        counter += 1

    #   RE-ARRANGE
    testSetA = set()
    testSetB = set()
    testList = list()
    for eachData in datasInSet:
        testSetA.add(eachData[0:4])
        testSetB.add(eachData)
    for i in range(250):
        testList.append(' ')
    mul,bb,bba,bbb,bbc,h = 25,0,0,0,0,0
    for tSA in testSetA:
        for tSB in testSetB:
            if bb == counter:
                bb = 0
                bbc = 0
                h+=1
            if tSA == tSB[0:4]:
                if bba >= counter:
                    bbb+=1
                    testList[bbb] = tSB
                elif bba < counter:
                    testList[bba] = tSB
                bbc += 1
                bb = (bbc * mul)
                bba = bb + h

    columnNumber = (counter//examsPerPeriod)//3 + 1

    import calendar #Import Calendar
 
    def findDay(date) -> str:
        day = datetime.strptime(date, '%d %m %Y').weekday()
        return (calendar.day_name[day])

    startingDayNumber = startingDay(startingDate) - 1
    for value in range(0,columnNumber):

        startingDayNumber += value**0
        # Get nextDay
        nextDay = presentday + timedelta(startingDayNumber)
        date = nextDay.strftime('%d %m %Y')

        findday = findDay(date)

        if findday == 'Sunday':
            startingDayNumber += 1
        nextDayA = presentday + timedelta(startingDayNumber)
        dateA = nextDayA.strftime('%d %m %Y')
        finddayA = findDay(dateA)
        daysList.append(finddayA)
        dateList.append(dateA)

        numberList.append(value+1)
        timeTable['Morning\n\n08:00am 09:00am 10:00am 11:00am'].append(' ')
        timeTable['Afternoon\n\n11:30am 12:30pm 01:30pm 02:30pm'].append(' ')
        timeTable['Evening\n\n03:00pm 04:00pm 05:00pm 06:00pm'].append(' ')

    timeTableData = pd.DataFrame(timeTable)

    scn,ecn,srn,ern,addingOneC,addingOneR,divisorCounter,examCounter,addingOneR,dataInSring = 0,0,3,0,0,0,0,0,0,'' #Declaring Iterators and String variable
    
    # for eachData in datasInSet:
    for eachData in testList:
        dataInSring += eachData + ' '
        examCounter +=1
        divisorCounter += 1
        if divisorCounter == divisor:
            dataInSring+='\n'
            divisorCounter = 0
        
        timeTableData.iloc[scn:ecn+addingOneC,srn:ern+addingOneR] = dataInSring

        if examCounter == examsPerPeriod:
            addingOneC = 1
            addingOneR = 0
            ecn = scn + 1
            ern = srn + 1

            timeTableData.iloc[scn:ecn,srn:ern] = dataInSring
            
            scn +=1
            if scn == columnNumber:
                srn +=1
                scn = 0
            dataInSring = ''
            examCounter = 0
            continue
        
    return timeTableData

## --------- VENUE

def venue(data = str, period = str, venuesCapacity = dict) -> list:

    courseUnit = pd.read_csv(data)
    vCK, vCV = [],[]
    for vCKI, vCVI in venuesCapacity.items():
        vCK.append(vCKI)
        vCV.append(vCVI)


    cuC2List = courseUnit['Courses'].values.tolist()
    cuS2List = courseUnit['Students'].values.tolist()

    courseUShape = courseUnit.shape[0]

    monCourses = TimeTableFunc[period]
    mornList,ivC =  [],0
    cuStr = ''
    cStr = ''
    morningList = []
    turnZero = 0
    for i in monCourses:
        splitVal = i.split()
        for v in splitVal:
            mornList.append(v)
        sumValue = 0
        for i in mornList:
            cuI = 0

            for cu in range(courseUShape):
                cuC2ListVal = cuC2List[cuI]
                cuS2ListVal = cuS2List[cuI]
                cuI += 1
                if turnZero == 0:
                    cuStr += vCK[ivC] + '(' + cStr
                turnZero += 1
                if cuC2ListVal == i:
                    vCValue = vCV[ivC]
                    sumValue += cuS2ListVal
                    if sumValue > vCValue:
                        sumValue = 0
                        sumValue += cuS2ListVal
                        ivC += 1
                        turnZero = 0
                        cuStr += ' ) '
                        cStr = ' ' + cuC2ListVal
                    else:
                        cuStr += ' ' + cuC2ListVal
                    if ivC == int(len(vCK)):
                        ivC = 0

        cuStr += ' ) '
        morningList.append(cuStr)
        cuStr = ''
        cuStr += vCK[ivC] + '('
                    
        mornList = []
    return morningList

def venueData(uData=str, supervisors = list, venuesCapacity = dict) -> str:
    TimeTableFunc['Supervisors'] = ' '
    morningList = venue(data = uData, period='Morning\n\n08:00am 09:00am 10:00am 11:00am', venuesCapacity= venuesCapacity)
    afternoonList = venue(data = uData, period='Afternoon\n\n11:30am 12:30pm 01:30pm 02:30pm', venuesCapacity= venuesCapacity)
    eveningList = venue(data = uData, period='Evening\n\n03:00pm 04:00pm 05:00pm 06:00pm', venuesCapacity= venuesCapacity)

    #------ VENUE
    venC = 0
    venD = 0
    for i in morningList:
        venD = venC + 1
        TimeTableFunc.iloc[venC:venD,3:4] = i
        venC += 1
    avenC = 0
    avenD = 0
    for i in afternoonList:
        avenD = avenC + 1
        TimeTableFunc.iloc[avenC:avenD,4:5] = i
        avenC += 1
    evenC = 0
    evenD = 0
    for i in eveningList:
        evenD = evenC + 1
        TimeTableFunc.iloc[evenC:evenD,5:6] = i
        evenC += 1

    #------ SUPERVISORS
    sup = []
    supC = 0
    supD = 0

    for i in supervisors:
        supD = supC + 1
        sup.append(i)
        TimeTableFunc.iloc[supC:supD,6:7] = i
        supC += 1
        pass
    ClistC = 0
    for Cl in morningList:
        if ClistC >= len(sup):
            ClistC = 0

        supD = supC + 1
        TimeTableFunc.iloc[supC:supD,6:7] = sup[ClistC]
        supC += 1
        ClistC += 1

    return TimeTableFunc

supervisors = ['Prof. A','Prof. B','Prof. C','Prof. D', 'Prof. E']
venuesCapacity = {'ELT':85, 'ICT-A':120, 'BLock-A':150,'Block-B':190, 'Workshop':110}

TimeTableFunc = examTimetable(data='studentsData.csv', startingDate='20221015', examsPerPeriod=6, divisor=0)
TimeTableFunc.to_csv('examResult.csv')
print(TimeTableFunc.to_markdown(), '\n')

VenueData = venueData(uData='courseUnitData.csv', supervisors=supervisors, venuesCapacity = venuesCapacity)
VenueData.to_csv('venueResult.csv') #You can change the name of the file
print(VenueData.to_markdown())