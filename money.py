class Money:
  _currencies = ("MDL","USD","EUR","RUB","RON")
  def __init__(self,amount,currency):
    self.amount = amount
    self.currency = currency
  
  def  __str__(self):
    return ???      # e.g. "100.00MDL"
