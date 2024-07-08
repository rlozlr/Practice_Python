from car_game import racing as rc
from car_game import car

carGame = rc.CarRacing()
car01 = car.Car('Car01', 'White', 250)
car02 = car.Car('Car01', 'Black', 200)
car03 = car.Car('Car01', 'Yellow', 220)
car04 = car.Car('Car01', 'Red', 280)
car05 = car.Car('Car01', 'Blue', 150)

carGame.addCar(car01)
carGame.addCar(car02)
carGame.addCar(car03)
carGame.addCar(car04)
carGame.addCar(car05)

carGame.startRacing()
