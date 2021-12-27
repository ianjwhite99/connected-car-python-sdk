from .api import Api
from . import const


class Vehicle(object):

    def __init__(self, vehicle_id, access_token, region="US"):
        """ Initialize a new Vehicle object to directly make requests to Ford.

        Args:
            vehicle_id (str): Vehicle identification number
            access_token (str): Sync Connect access token
        """
        self.access_token = access_token
        self.vehicle_id = vehicle_id
        self.api = Api(access_token, region)

    def status(self):
        """ GET Vehicle.status

        Returns:
            Response: Current vehicle status

        Raises:
            SyncException

        """

        response = self.api.get(
            const.API_URL,
            'vehicles/v4/' +
            self.vehicle_id +
            '/status?lrdt=01-01-1970%2000:00:00')
        return response.json()

    def refresh_status(self):
        """ PUT Vehicle.refresh_status

        Returns:
            Response: Send request to refresh data from the cars module

        Raises:
            SyncException

        """

        response = self.api.put(
            const.API_URL,
            'vehicles/v2/' +
            self.vehicle_id +
            '/status', None)
        return response.json()

    def send_auth(self):
        """ POST Vehicle.send_auth

        Returns:
            Response: Send vehicle authorization

        Raises:
            SyncException

        """

        response = self.api.post(
            const.API_URL, 'vehicles/v2/' + self.vehicle_id + '/drivers', None)
        return response.json()

    def auth_status(self):
        """ GET Vehicle.auth_status

        Returns:
            Response: Vehicle authorization status

        Raises:
            SyncException

        """

        response = self.api.get(
            const.API_URL,
            'vehicles/' +
            self.vehicle_id +
            '/authstatus?lrdt=01-01-1970%2000:00:00')
        return response.json()

    def details(self):
        """ GET Vehicle.detials

        Returns:
            Response: Vehicle details

        Raises:
            SyncException

        """

        response = self.api.get(
            const.API_URL,
            'users/vehicles/' +
            self.vehicle_id +
            '/detail?lrdt=01-01-1970%2000:00:00')
        return response.json()

    def maintenance_schedule(self):
        """ GET Vehicle.maintenance_schedule

        Returns:
            Response: Vehicle maintenance schedule

        Raises:
            SyncException

        """

        response = self.api.get(
            const.USER_URL,
            'vehiclemaintenance/v1/maintenance-schedule?vin=' +
            self.vehicle_id +
            '&language=EN&country=USA')
        return response.json()

    def capability(self):
        """ GET Vehicle.capability

        Returns:
            Response: Vehicle capabilities

        Raises:
            SyncException

        """

        response = self.api.get(
            const.USER_URL, 'capability/v1/vehicles/' + self.vehicle_id)
        return response.json()

    def vin(self):
        """ GET Vehicle.vin

        Returns:
            Response: Vehicle vin

        Raises:
            SyncException

        """

        json = self.status()
        return {"data": json['vehiclestatus']['vin']}

    def odometer(self):
        """ GET Vehicle.odometer

        Returns:
            Response: Vehicle odometer

        Raises:
            SyncException

        """

        json = self.status()
        return {"data": json['vehiclestatus']['odometer']}

    def fuel(self):
        """ GET Vehicle.fuel

        Returns:
            Response: Vehicle fuel level

        Raises:
            SyncException

        """

        json = self.status()
        return {"data": json['vehiclestatus']['fuel']}

    def oil(self):
        """ GET Vehicle.oil

        Returns:
            Response: Vehicle oil life

        Raises:
            SyncException

        """

        json = self.status()
        return {"data": json['vehiclestatus']['oil']}

    def tire_pressure(self):
        """ GET Vehicle.tire_pressure

        Returns:
            Response: Vehicle tire pressure

        Raises:
            SyncException

        """

        json = self.status()
        return {"data": json['vehiclestatus']['TPMS']}

    def battery(self):
        """ GET Vehicle.battery

        Returns:
            Response: Vehicle battery status

        Raises:
            SyncException

        """

        json = self.status()
        return {"data": json['vehiclestatus']['battery']}

    def location(self):
        """ GET Vehicle.location

        Returns:
            Response: Vehicle location

        Raises:
            SyncException

        """

        json = self.status()
        return {"data": json['vehiclestatus']['gps']}

    def window_positions(self):
        """ GET Vehicle.window_position

        Returns:
            Response: Vehicle window positions

        Raises:
            SyncException

        """

        json = self.status()
        return {"data": json['vehiclestatus']['windowPosition']}

    def door_status(self):
        """ GET Vehicle.door_status

        Returns:
            Response: Vehicle doors status

        Raises:
            SyncException

        """

        json = self.status()
        return {"data": json['vehiclestatus']['doorStatus']}

    def lock_status(self):
        """ GET Vehicle.lock_Status

        Returns:
            Response: Vehicle lock status

        Raises:
            SyncException

        """

        json = self.status()
        return {"data": json['vehiclestatus']['lockStatus']}

    def alarm_status(self):
        """ GET Vehicle.alarm_status

        Returns:
            Response: Vehicle alarm status

        Raises:
            SyncException

        """

        json = self.status()
        return {"data": json['vehiclestatus']['alarm']}

    def ignition_status(self):
        """ GET Vehicle.ignition_status

        Returns:
            Response: Vehicle ignition status

        Raises:
            SyncException

        """

        json = self.status()
        return {"data": json['vehiclestatus']['ignitionStatus']}

    def wakeup(self):
        """ GET Vehicle.wakeup

        Returns:
            Response: response from the request to the Ford API

        Raises:
            SyncException

        """

        response = self.api.action(
            'GET',
            const.USER_URL,
            'dashboard/v1/users/vehicles?language=EN&wakeupVin=' +
            self.vehicle_id +
            '&skipRecall=true&country=USA&region=US')
        return response.json()

    def start(self):
        """ PUT/GET Vehicle.start

        Returns:
            Response: response from the request to the Ford API

        Raises:
            SyncException

        """

        job_id = self.api.action(
            'PUT',
            const.API_URL,
            'vehicles/v2/' +
            self.vehicle_id +
            '/engine/start').json()['commandId']
        response = self.api.action(
            'GET',
            const.API_URL,
            'vehicles/' +
            self.vehicle_id +
            '/engine/start/' +
            job_id)
        return response.json()

    def stop(self):
        """ DELETE/GET Vehicle.stop

        Returns:
            Response: response from the request to the Ford API

        Raises:
            SyncException

        """

        job_id = self.api.action(
            'DELETE',
            const.API_URL,
            'vehicles/v2/' +
            self.vehicle_id +
            '/engine/start').json()['commandId']
        response = self.api.action(
            'GET',
            const.API_URL,
            'vehicles/' +
            self.vehicle_id +
            '/engine/start/' +
            job_id)
        return response.json()

    def lock(self):
        """ PUT/GET Vehicle.lock

        Returns:
            Response: response from the request to the Ford API

        Raises:
            SyncException

        """

        job_id = self.api.action(
            'PUT',
            const.API_URL,
            'vehicles/v2/' +
            self.vehicle_id +
            '/doors/lock').json()['commandId']
        response = self.api.action(
            'GET',
            const.API_URL,
            'vehicles/' +
            self.vehicle_id +
            '/doors/lock/' +
            job_id)
        return response.json()

    def unlock(self):
        """ DELETE/GET Vehicle.unlock

        Returns:
            Response: response from the request to the Ford API

        Raises:
            SyncException

        """

        job_id = self.api.action(
            'DELETE',
            const.API_URL,
            'vehicles/v2/' +
            self.vehicle_id +
            '/doors/lock').json()['commandId']
        response = self.api.action(
            'GET',
            const.API_URL,
            'vehicles/' +
            self.vehicle_id +
            '/doors/lock/' +
            job_id)
        return response.json()
