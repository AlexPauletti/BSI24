year = 1980
month = 7
date = 2

Days_in_Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def isBisextile(year):
    return True if year%4 == 0 else False

if isBisextile(year):
   Days_in_Month[1] = 29

days = int(input("Enter number of days:\n"))

while days > 0:

   if isBisextile(year):
       Days_in_Month[1] = 29
   else:
       Days_in_Month[1] = 28

   date += 1

   if date > int(Days_in_Month[month-1]):
       month += 1
       if month > 12:
           year += 1
           month = 1
       date = 1
   days -= 1


print("{}/{}/{}".format(date, month, year))