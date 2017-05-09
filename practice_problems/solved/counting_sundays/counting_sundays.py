def main():
        dayOfWeek = 1
        day = 1
        month = 1
        year = 1900
        firstSundays = 0;

        while year < 2001:
                dayOfWeek = (dayOfWeek%7)+1
                day += 1
                if day > daysIn(month, year):
                        day = 1
                        month = (month%12)+1
                        if month == 1:
                                year += 1
                        if dayOfWeek == 7 and year >= 1901:
                                firstSundays += 1
        print("{} Sundays fell on the first of the month during the twentieth century.".format(firstSundays))

def daysIn(month, year):
        if month == 2:
                if isLeap(year):
                        return 29
                else:
                        return 28
        else: 
                return {
                        1: 31,
                        3: 31,
                        4: 30,
                        5: 31,
                        6: 30,
                        7: 31,
                        8: 31,
                        9: 30,
                        10: 31,
                        11: 30,
                        12: 31
                }[month]

def isLeap(year):
        return (year%4 == 0 and year%100 != 0) or (year%400 == 0)

main()
