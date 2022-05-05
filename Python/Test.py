from Sensoren import sensor1, sensor2, sensor3

while True:
   print("Sensor 1:")
   print(sensor1.getRotData()["xAxis"])
   print(sensor1.getRotData()["yAxis"])
   print("Sensor 2:")
   print(sensor2.getRotData()["xAxis"])
   print(sensor2.getRotData()["yAxis"])
   print("Sensor 3:")
   print(sensor3.getRotData()["xAxis"])
   print(sensor3.getRotData()["yAxis"])



         
