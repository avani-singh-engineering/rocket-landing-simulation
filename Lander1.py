mass_rocket = 70
mass_fuel = 30
thrust = 1500
velocity = 0
altitude = 0

while mass_fuel > 0:
    total_mass = mass_rocket + mass_fuel
    weight = total_mass * 9.8
    
    net_force = thrust - weight
    acceleration = net_force / total_mass
    
    velocity = velocity + acceleration
    altitude = altitude + velocity
    
    mass_fuel = mass_fuel - 2 
    
    print('Altitude',altitude,'m','speed',velocity,'m/s')
