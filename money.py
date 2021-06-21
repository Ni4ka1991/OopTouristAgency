

class Money:
    
    def __init__( self, amount, currency ):
        self.amount = amount
        self.currency = currency
  
    def  __str__( self ):
        
        _currencies = ( "MDL","USD","EUR","RUB","RON" )
        
        if self.currency in _currencies:
            return f"\"{self.amount:.2f} {self.currency}\""      # e.g. "100.00MDL"
        else:
            raise ValueError("Enter another value")
