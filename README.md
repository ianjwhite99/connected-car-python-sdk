#

![ConnectedCar Python SDK Logo](https://user-images.githubusercontent.com/35158392/147300580-29723aab-ffae-46d3-ae60-72af59065daa.png)

The ConnectedCar Python SDK is an open-source, python package that provides the ability to send commands to your Ford Sync Connect connected vehicle.

## Installation [![PyPI version](https://badge.fury.io/py/connectedcar.svg)](https://badge.fury.io/py/connectedcar)

```sh
python3 -m pip install connectedcar
```

Requirements

- To make requests to a vehicle, the end user must have signed up for an account using [Ford Pass](https://owner.ford.com/fordpass/fordpass-sync-connect.html). These credentials will be used to authenticate your requests.

## Getting Started

Import the ConnectedCar SDK

```python
import connectedcar
```

Create a new connectedcar `client`

- Note the default ConnectedCar client_id is
  `9fb503e0-715b-47e8-adfd-ad4b7770f73b`

```python
client = connectedcar.AuthClient('9fb503e0-715b-47e8-adfd-ad4b7770f73b', None, None, None, 'US') # Region argument is only required if you live outside the United States.
```

- Note: If your region is outside of the US you can pass different region parameters. Regions: (US, CA, EU, AU)

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
refreshToken = client.exchange_refresh_token(access['refresh_token'])
```

With your access token in hand, use `connectedcar.User()` to get a User object representing the user.

```python
user = connectedcar.User(access['access_token'], "US") # Region argument is only required if you live outside the United States.
```

Use `user.vehicles()` to return an array of all the vehicles associated with a users account. The response will include the **vehicle vin**.

```python
vehicles = user.vehicles()

vehicleList = [] # Array of vehicles

for userVehicle in vehicles: # For each user vehicle
    vehicleList.append(userVehicle['vin'])
```

Now with a **vehicle vin** in hand, use `connectedcar.Vehicle()` to get a Vehicle object representing the user's vehicle.

```python
currentVehicle = connectedcar.Vehicle(vehicleList[0], access['access_token'], "US") # Region argument is only required if you live outside the United States.
```

Now you can ask the car to do things, or ask it for some data! For example:

```python
currentVehicle.start()
```

## Examples & Documentation

For more examples on what you can do with Sync Connected car, see the [examples](/examples) folder or take a peek at the [documentation](https://ianjwhite99.github.io/connected-car-python-sdk/).

## Funding & Support

If you are interested in supporting the development of my projects check out my [patreon](https://www.patreon.com/ianjwhite99) or [buy me a coffee](https://www.buymeacoffee.com/ianjwhite9).

## Disclaimer

THIS CODEBASE IS NOT ENDORSED, AFFILIATED, OR ASSOCIATED WITH FORD, FOMOCO OR THE FORD MOTOR COMPANY.
