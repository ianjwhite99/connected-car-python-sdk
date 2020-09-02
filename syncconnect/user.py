from .api import Api
from . import const

class User(object):

    def __init__(self, access_token):
        """ Initialize a new User object to directly make requests to Ford.
        
        Args:
            access_token (str): Ford access token
        """
        self.api = Api(access_token)

    def info(self):
        """ GET User.info
        
        Returns:
            Response: User information

        """

        response = self.api.get(const.API_URL, 'users')
        return response.json()

    def vehicles(self):
        """ GET User.vehicles
        
        Returns:
            Response: User vehicle list

        """
        
        response = self.api.get(const.VEHICLE_URL, 'dashboard/v1/users/vehicles?country=USA&language=EN&region=US&skipRecall=true')
        return response.json()

    def add_vehicle(self, vehicle_id):
        """ POST User.add_vehicle

        Args:
            vehicle_id (str): the vehicle identification number
        
        Returns:
            Response: response from the request to the Ford API

        """

        data = '{"countryCode": "USA", "nickName": "", "vin": "'+vehicle_id+'", "appBrand": "F", "appRegion": "NA"}'
        response = self.api.post(const.USER_URL, 'garage/mobile', data)
        return response.json()

    def delete_vehicle(self, vehicle_id):
        """ DELETE User.delete_vehicle

        Args:
            vehicle_id (str): the vehicle identification number
        
        Returns:
            Response: response from the request to the Ford API

        """

        response = self.api.delete(const.API_URL, 'users/vehicles/'+vehicle_id)
        return response.json()

    


