from datetime import date,time,datetime,timedelta

# t=date.today()

# print(t)
# print(t.day)
# print(t.month)
# print(t.year)
# print(t.weekday())

# year,month,day = list(map(int,input("Enter date in YYYY-MM-DD format: ").split('-')))

# print(date(year,month,day))


# tm = time(12,30,45)

# print(tm)
# print(tm.hour)
# print(tm.minute)
# print(tm.second)


# dt = datetime.now()
# print(dt)
# print(dt.strftime('%d-%m-%y'))
# print(dt.strftime('%d-%m-%Y'))
# print(dt.strftime('%d-%m-%Y %H:%M:%S'))
# print(dt.strftime('%d-%m-%Y %H:%M:%S %p'))
# print(dt.strftime('%d-%m-%Y %I:%M:%S %p'))
# print(dt.strftime('%d %b-%Y %I:%M:%S %p'))
# print(dt.strftime('%d %B-%Y %I:%M:%S %p'))
# print(dt.strftime('%a %d %B-%Y %I:%M:%S %p'))
# print(dt.strftime('%A %d %B-%Y %I:%M:%S %p'))
    



dt = datetime.now()
t= date.today()

t7 = t + timedelta(days=7)

min15 = dt + timedelta(minutes=15)
print(t7,"\n",min15)