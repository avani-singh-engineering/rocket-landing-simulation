altitude = 200
velocity = 10
fuel = 150
gravity = 1.62
while altitude > 0:
  print('altitude:', altitude, 'velocity:', velocity)
  thrust=float(input('Enter thrust(0 to 4):'))
  fuel = fuel - thrust
  acceleration = gravity - thrust
  velocity = velocity + acceleration
  altitude = altitude - velocity
if velocity <= 5:
  print('Congratulations! You have landed safely!')
else:
  print('Oops! You have crashed - try again')
