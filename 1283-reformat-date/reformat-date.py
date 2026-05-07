class Solution:
    def reformatDate(self, date: str) -> str:
        day, m, y = date.split(' ')
        Month = {"Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6, "Jul" : 7, 
                    "Aug" : 8, "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12}
        mon = Month[m]
        mon = str(mon)
        n = len(mon)
        if n==1:
            mon = '0'+mon
        day1 = day[0]
        day2 = day[1]
        if day2.isdigit():
            day = day1+day2
        else:
            day = '0'+day1
        ans = y+'-'+mon+'-'+day
        return ans
