from application.salary import calculate_salary

from db.people import get_employees

import datetime

now = datetime.datetime.now()

if __name__ == '__main__':
    print (now.strftime("%d-%m-%Y %H:%M"))
    calculate_salary()
    get_employees()
