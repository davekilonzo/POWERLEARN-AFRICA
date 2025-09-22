class Smartphone:
  def __init__(self, brand, model, storage):
    self.brand = brand
    self.model = model
    self.storage = storage
  def call(self, number):
    print(f"{self.brand} {self.model} is calling {number}...")
  def info(self):
    print(f"Smartphone: {self.brand} {self.model}, Storage:{self.storage}GB")
class Smartwatch(Smartphone):
  def __init__(self, brand, model, storage, strap_color):
    super().__init__(brand, model, storage)
    self.strap_color = strap_color
  
  def info(self):
    print(f"Smartwatch :{self.brand} {self.model}, Storage:{self.storage}GB")


phone1 = Smartphone("Samsung", "Galacy S23", 256)
watch1 = Smartwatch("Apple", "Watch Series 9", 64, "Black")

phone1.info()
phone1.call("0741646489")

watch1.info()
watch1.call("0741646489")