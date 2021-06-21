
#datetime.py
import datetime

class Period:
    
    def __init__( self, start, end ):
        
        self.start = start
        self.end   = end
    
    def timeStrConvert( time_str ):  # "01.01.2021" str ---> to list [1, 1, 2021]
        a = "a"
        time_list = time_str.split(".")
        print()
        for i in time_list:
            i = i + a
            print( f"---> {i}" )
        print()
            
        
        return time_list
    
    def dateTime( date_list ):
        
        date = datetime.date(date_list[2], date_list[1], date_list[0])
        return date


    
    def  __str__( self ):
        return f"{self.start} .. {self.end}"      # e.g. "[01.01.2021 .. 02.01.2021]"   
