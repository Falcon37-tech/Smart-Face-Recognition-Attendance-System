# For Attendance Logging

from datetime import datetime

def markAttendance(name, file_path='Attendance.csv'):
    """Mark attendance for a person if not already present."""
    with open(file_path,'r+') as f:
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S %p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'{name}, {time}, {date}\n')
