from datetime import datetime, timedelta
current_date = datetime.now()
print(current_date)
one_day = timedelta(days=1)
yesterday = current_date - one_day
print('yesterady was : ' + str(yesterday))

print('today :' + str(current_date.year))

# print('when is your birthday (dd/mm/yy) :'  )
date = input("when is your birthday ? :")
dob = datetime.strptime(date,'%d/%m/%y')
try :
    print(str(dob))

except:
    