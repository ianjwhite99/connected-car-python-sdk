import connectedcar

client = connectedcar.AuthClient(
    '9fb503e0-715b-47e8-adfd-ad4b7770f73b',
    None,
    None)  # Create client connection
access = client.get_user_access_token(
    '<username>', '<password>')  # Fetch client access token

user = connectedcar.User(access['access_token'])  # New User Object
vehicles = user.vehicles()  # Fetch list of user vehicles

for userVehicle in vehicles:  # For each user vehicle
    vehicle = connectedcar.Vehicle(
        userVehicle['vin'], access['access_token'])  # Create vehicle object
    print(vehicle.info())  # Return vehicle info
