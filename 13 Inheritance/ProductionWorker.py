from Employee import Employee as Parent
class ProductionWorker(Parent):
  def __init__(self, shift_number = 0, hourly_rate = 12.0):
    Parent.__init__(self)
    self.shift_number = int(shift_number)
    self.hourly_rate = float(hourly_rate)
  def get_shift_number(self):
    return self.shift_number
  def set_shift_number(self, shift_number):
    self.shift_number = int(shift_number)
  def get_hourly_rate(self):
    return self.hourly_rate
  def set_hourly_rate(self, hourly_rate):
    self.hourly_rate = float(hourly_rate)
