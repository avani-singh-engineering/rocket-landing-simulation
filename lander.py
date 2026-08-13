altitude = 30
velocity = 10
fuel = 150
gravity = 1.62
while altitude > 0:
     print('altitude:', altitude, 'velocity:', velocity)
     thrust=float(input('Enter thrust(0 to 4):'))
     if thrust < 0:
        thrust = 0.0
     elif thrust > 4:
        thrust = 4.0
     if fuel <= 0
        print('Out of fuel')
     fuel = fuel - thrust
     acceleration = gravity - thrust
     velocity = velocity + acceleration
     altitude = altitude - velocity
if velocity <= 5:
  print('Congratulations! You have landed safely!')
else:
  print('Oops! You have crashed - try again')
