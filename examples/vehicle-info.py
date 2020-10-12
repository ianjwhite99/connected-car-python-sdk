import syncconnect

client = syncconnect.AuthClient('<client-id>', None, None) # Create client connection
access = client.get_user_access_token('<username>', '<password>') # Fetch client access token

user = syncconnect.User(access['access_token']) # New User Object
vehicles = user.vehicles() # Fetch list of user vehicles

for userVehicle in vehicles: # For each user vehicle
    vehicle = syncconnect.Vehicle(userVehicle['vin'], access['access_token']) # Create vehicle object
    print(vehicle.info()) # Return vehicle info
