import connectedcar

# Input FordPass username, and password.
# IT IS RECOMMENDED TO USE A SECOND ACCOUNT (see README)
fp_username = ''
fp_password = ''

client = connectedcar.AuthClient(
    '9fb503e0-715b-47e8-adfd-ad4b7770f73b',
    None,
    None)  # Create client connection
access = client.get_user_access_token(
    fp_username, fp_password)  # Fetch client access token

user = connectedcar.User(access['access_token'])  # New User Object
vehicles = user.vehicles()  # Fetch list of user vehicles

vehicleList = []  # Stored list of user vehicles

for userVehicle in vehicles:  # For each user vehicle
    vehicleList.insert(0, userVehicle['VIN'])
    break

currentVehicle = connectedcar.Vehicle(
    vehicleList[0], access['access_token'])  # Create vehicle object
print(currentVehicle.start())  # Send start command
