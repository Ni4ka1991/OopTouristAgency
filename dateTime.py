
#datetime.py
import datetime

class Period:
    
    def __init__( self, start, end ):
        
        self.start = start
        self.end   = end
    
    def timeStrConvert( time_list ):  # "01.01.2021" str ---> to list of int [1, 1, 2021]

        time_list = self.split(".")
        
        for i in range(len(time_list)):
            time_list[i] = int(time_list[i])
        return time_list
    
    def dateTime( date_list ):
        
        date = datetime.date(date_list[2], date_list[1], date_list[0])
        return date

    def __ge__( self, other ):
        
        if isistance( other, time ):
            return self._cmp( other ) >= 0
        else:
            _cmperror( self, other )
    
    def  __str__( self ):
        return f"{self.start} .. {self.end}"      # e.g. "[01.01.2021 .. 02.01.2021]"   
