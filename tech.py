class Tech:
  def __init__(self,name,storage):
    self.name = name
    self.storage =  storage
class Phone(Tech):
  def __init__(self,name,storage,color):
    self.super().__init__(name,storage)
    self.color=color
  def __str__(self):
    return str(f"A {self.color} {self.name} with {str(self.storage)}GB of storage.")
  def __repr__(self):
    return f"Phone({self.name},{str(self.storage)},{self.color})"
class Laptop(Tech):
  def __init__(self,name,storage,size):
    self.super().__init__(name,storage)
    self.size = int(size)
  def __str__(self):
    return str(f'{str(self.size)}-inch {self.name} with {str(self.storage)}GB of storage.')
  def __repr__(self):
    return f"Laptop({self.name},{str(self.storage)},{str(self.size)})"
    
