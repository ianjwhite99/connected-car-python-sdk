![Sync Connect Python SDK Logo](https://user-images.githubusercontent.com/35158392/111222780-4bf1bb80-85aa-11eb-8be2-271ae5f32936.png)

The Sync Connect Python SDK is an open-source, python package that provides the ability to send commands to your Ford Sync Connect connected vehicle.
# Installation [![PyPI version](https://badge.fury.io/py/syncconnect.svg)](https://badge.fury.io/py/syncconnect)
```sh
python3 -m pip install syncconnect
```

Requirements
- To make requests to a vehicle, the end user must have signed up for an account using [Ford Pass](https://owner.ford.com/fordpass/fordpass-sync-connect.html). These credentials will be used to authenticate your requests.
# Getting Started

Import the Sync Connect SDK
```python
import syncconnect
```


Create a new syncconnect `client`
- Note the default Sync Connect client_id is 
`9fb503e0-715b-47e8-adfd-ad4b7770f73b`

```python
client = syncconnect.AuthClient('9fb503e0-715b-47e8-adfd-ad4b7770f73b', None, None)
```

Use `client.get_user_access_token()` to exchange your user credentials for an **access object**. To make any vehicle data request to the Ford Sync Connect API, you'll need to give the SDK a valid **access token**. 

```python
access = client.get_user_access_token('<username>', '<password>')
```

This access object will look like this:

```json
{
  "access_token": "...",
  "token_type": "Bearer",
  "expiration": "2021-03-01T18:04:25+00:00",
  "refresh_token": "...",
  "refresh_expiration": "2021-03-02T18:03:25+00:00",
  "expires_in": "..."
}
```

Access tokens will expire every 2 hours, so you'll need to constantly refresh them by calling `client.exchange_refresh_token()`

```python
refreshToken = client.exchange_refresh_token(access['refreshToke'])
```

With your access token in hand, use `syncconnect.User()` to get a User object representing the user.
```python
user = syncconnect.User(access['access_token'])
```

Use `user.vehicles()` to return an array of all the vehicles associated with a users account. The response will include the **vehicle vin**.
```python
vehicleList = [] # Array of vehicles

for userVehicle in vehicles: # For each user vehicle
    vehicleList.insert(0, userVehicle['vin'])
    break
```

Now with a **vehicle vin** in hand, use `syncconnect.Vehicle()` to get a Vehicle object representing the user's vehicle.
```python
currentVehicle = syncconnect.Vehicle(vehicleList[0], access['access_token'])
```

Now you can ask the car to do things, or ask it for some data! For example:
```python
currentVehicle.start()
```

# Examples & Documentation
* For more examples on what you can do with Sync Connected car, see the [examples](/examples) folder or take a peek at the [documentation](https://ianjwhite99.github.io/sync-connect-sdk/).
