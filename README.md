# Sync Connect Python SDK

## Overview

The Ford Sync Connect API lets you read vehicle data (location, odometer, fuel) and send commands (start, stop, lock, unlock) to connected vehicles using HTTP requests.

To make requests to a vehicle, the end user must connect their vehicle using their [Ford Pass Credentials](https://owner.ford.com/fordpass/fordpass-sync-connect.html).

## Installation
```
pip install syncconnect
```

## Overall Usage

* Import the sdk `import syncconnect`
* Create a new syncconnect `client` with `syncconnect.AuthClient(client_id, client_secret, redirect_uri, scope)`

* Use `client.get_user_access_token(username, password)` to exchange your user credentials for an **access object**. This access object will look like this:

```json
{
  "access_token": "...",
  "token_type": "Bearer",
  "expiration": "2018-05-02T18:04:25+00:00",
  "refresh_token": "...",
  "refresh_expiration": "2018-06-02T18:03:25+00:00",
  "expires_in": "..."
}
```

* To make any vehicle data request to the Ford Sync Connect API, you'll need to give the SDK a valid **access token**. Access tokens will expire every 2 hours, so you'll need to constantly refresh them by calling `client.exchange_refresh_token(refresh_token)`

* With your access token in hand, use `syncconnect.User(access_token)` to get a User object representing the user.

* Use `user.vehicles()` to return a list of all the vehicles associated with a users account. The response will include the **vehicle vin**.

* Now with a **vehicle vin** in hand, use `syncconnect.Vehicle(vehicle_id, access_token)` to get a Vehicle object representing the user's vehicle.

* Now you can ask the car to do things, or ask it for some data! For example:

```python
vehicle = syncconnect.Vehicle(vehicle_id, access_token)
vehicleInfo = vehicle.info()
```

* For a lot more examples on what you can do a Sync Connected car, see the [examples](/examples) folder or take a peek at the [documentation](/docs) after you clone the project.
