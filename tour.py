_destinations = ({ "name": "Greece", "price": Money(100,"EUR")},{ "name": "France", "price": Money(120,"EUR")}, { "name": "Italy", "price": Money(200,"EUR")}, { "name": "USA", "price": Money(300,"USD")})
class _Tour:
  def __init__(self,destination,name,tourists,period):
    self.destination = destination
    self.name = name
    self.tourists = tourists
    self.period = period  
    self.cost = self.calculateCost()
  def calculateCost(self):
    ???
    return ???
  
  class TourBuilder:
  def __init__(self,destination,name,tourists,period):
    self._tour = _Tour(destination,name,tourists,period)
  def withEnsurance(self):
    ???
    return self
  def withEnsurance(self):
    ???
    return self 
  def withGuide(self):
    ???
    return self        
  def build(self):
    return self._tour      
