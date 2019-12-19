class Employee:
  def __init__(self, employee_name = '', employee_number = 0):
    self.employee_name = employee_name
    self.employee_number = int(employee_number)
  def get_name(self):
    return self.employee_name
  def set_name(self, employee_name):
    self.employee_name = employee_name
  def get_number(self):
    return self.employee_number
  def set_number(self, employee_number):
    self.employee_number = int(employee_number)
