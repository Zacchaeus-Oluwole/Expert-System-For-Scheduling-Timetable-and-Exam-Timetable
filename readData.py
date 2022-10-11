import pandas as pd

rData = pd.read_csv('timetableResult.csv')
data = pd.read_csv('studentsData.csv')
cuData = pd.read_csv('courseUnitData.csv')
eData = pd.read_csv('examResult.csv')
vData = pd.read_csv('venueResult.csv')


rData = rData.drop(columns = ['Unnamed: 0'])
data = data.drop(columns = ['Unnamed: 0'])
cuData = cuData.drop(columns = ['Unnamed: 0'])
eData = eData.drop(columns = ['Unnamed: 0'])
vData = vData.drop(columns = ['Unnamed: 0'])
# data

print(rData.to_markdown(), '\n') # Timetable
print(data.to_markdown(), '\n') #Courses
print(cuData.to_markdown(), '\n') # Unit of the courses
print(eData.to_markdown(), '\n') #Exam timetable
print(vData.to_markdown(), '\n') #Venue