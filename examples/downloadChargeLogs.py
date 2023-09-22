import connectedcar
import json

# Input FordPass username, and password.
# IT IS RECOMMENDED TO USE A SECOND ACCOUNT (see README)
fp_username = ''
fp_password = ''

# Specify the file path where you want to save the JSON data
file_path = "charge_logs.json"

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

authorizedVehicle = connectedcar.Vehicle(
    vehicleList[0], access['access_token'])

# Get the charge logs as a dictionary
charge_logs = authorizedVehicle.get_chargeLogs()

# Serialize the charge_logs dictionary to a JSON string
charge_logs_json = json.dumps(charge_logs, indent=4)

# Write the JSON string to the file
with open(file_path, 'w') as json_file:
    json_file.write(charge_logs_json)

print(authorizedVehicle.get_chargeLogs())  # Get charge logs in json format
print(f"JSON data saved to {file_path}")
