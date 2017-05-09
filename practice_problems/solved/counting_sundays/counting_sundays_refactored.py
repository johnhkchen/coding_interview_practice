class CountingSundaysSolver:
        def __init__(self):
                self.dayOfWeek = 1
                self.day = 1
                self.month = 1
                self.year = 1900
                while not self.isTwentiethCentury():
                        self.nextDay()
                self.solve()

        def solve(self):
                firstSundays = 0
                while self.isTwentiethCentury():
                        self.nextDay()
                        if self.isFirstOfMonth() and self.isSunday():
                                firstSundays += 1
                print("{} Sundays fell on the first of the month during the twentieth century.".format(firstSundays))


        def nextDay(self):
                self.dayOfWeek = (self.dayOfWeek%7)+1
                self.day += 1
                if self.day > self.daysThisMonth():
                        self.nextMonth()
        def nextMonth(self):
                self.day = 1
                if self.month < 12:
                        self.month += 1
                else:
                        self.nextYear()
        def nextYear(self):
                self.month = 1
                self.year += 1

        def daysThisMonth(self):
                if self.month == 2:
                        if self.isLeapYear():
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
                        }[self.month]

        def isTwentiethCentury(self):
                return self.year > 1900 and self.year <= 2000
        def isLeapYear(self):
                return (self.year%4 == 0 and self.year%100 != 0) or (self.year%400 == 0)
        def isFirstOfMonth(self):
                return self.day == 1
        def isSunday(self):
                return self.dayOfWeek == 7

CountingSundaysSolver()