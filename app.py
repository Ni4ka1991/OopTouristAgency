#!/usr/bin/env python3

from money import Money
from dateTime import Period
#import datetime

#tour = TourBuilder("Italy","The best parst of Italy",[Tourist("John Doe", 21), Tourist("Jane Doe", 30), Tourist("Jenny", 6)],Period("01.01.2021","02.01.2021")).withEnsurance().withGuide().build()


price_1 = Money(300, "MDL")
print(price_1)


new_period = Period( "25.06.2021", "27.06.2021" )
print( new_period )

date_list = Period.timeStrConvert( "21.01.2021" )
print(date_list)
print(date_list[0])
print(type(date_list[0]))


#date = Period.dateTime( 2021, 12, 5 )
#print(date)



#print(datetime.date( 2021, 6, 25 ))
