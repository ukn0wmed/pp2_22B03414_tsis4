import datetime

current_date = datetime.date.today()

fivedays_ago = current_date - datetime.timedelta(days=5)

tomorrow = current_date + datetime.timedelta(days=1)
yesterday = current_date - datetime.timedelta(days=1)

now = datetime.datetime.now()

# Можно еще дропнуть создав новую переменную и обозначить ее как now.replace(microseconds=0)

print("Five days ago was:", fivedays_ago.strftime('%d.%m.%Y'))

print("Tomorrow is:", tomorrow.strftime('%d.%m.%Y'))
print("Yesterday was:", yesterday.strftime('%d.%m.%Y'))
print("Today is:", current_date.strftime('%d.%m.%Y'))

print("Current time without microseconds:", now.strftime('%d.%m.%Y %H:%M:%S'))

date1 = datetime.datetime(2022, 2, 21, 12, 0, 0)  # год, месяц, день, час, минуты, секунды
date2 = datetime.datetime(2022, 2, 22, 6, 30, 0)

difference = (date2 - date1).total_seconds()

print("The difference between the two dates is", difference, "seconds.")
# print("The difference between the two dates is", round(difference), "seconds.")
