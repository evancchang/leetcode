class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        date_list = date.split('-')
        year, month, day = int(date_list[0]), int(date_list[1]), int(date_list[2])
        
        if not year % 400 or (not year % 4 and year % 100):
            days[1] += 1
            
        return sum(days[:month-1]) + day
