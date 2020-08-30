from .api import Api
from . import const

class User(object):

    def __init__(self, access_token):
        self.api = Api(access_token)

    def info(self):
        response = self.api.get(const.API_URL, 'users')
        return response.json()

    def vehicles(self):
        response = self.api.get(const.VEHICLE_URL, 'dashboard/v1/users/vehicles')
        return response.json()

    def add_vehicle(self, vehicle_id):
        data = '{"countryCode": "USA", "nickName": "", "vin": "'+vehicle_id+'", "appBrand": "F", "appRegion": "NA"}'
        response = self.api.post(const.USER_URL, 'garage/mobile', data)
        return response.json()

    def delete_vehicle(self, vehicle_id):
        response = self.api.delete(const.API_URL, 'users/vehicles/'+vehicle_id)
        return response.json()

    


