import unittest
import responses
import syncconnect
from syncconnect import const

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = syncconnect.User('access_token')

    @responses.activate
    def test_get_user_info(self):
        data = {
            'httpStatus': 200, 
            'status': 200, 
            'requestStatus': 'CURRENT', 
            'error': None, 'lastRequested': 
            '2021-03-17T05:15:19.178Z', 
            'version': '1.0.1', 
            'profile': {
                'httpStatus': 200, 
                'status': 200, 
                'requestStatus': 'CURRENT', 
                'error': None, 
                'lastRequested': '2021-02-15T05:15:19.178Z', 
                'version': '1.0.1', 
                'userId': 'johndoe@gmail.com', 
                'userGuid': '1f1c8eca-ff55-4a5a-86c8-726eb654b9cb',
            }
        }
        responses.add('GET', const.API_URL + '/users', json=data)
        actual = self.user.info()
        
        self.assertEqual("1f1c8eca-ff55-4a5a-86c8-726eb654b9cb",
                         actual['profile']['userGuid'])

    @responses.activate
    def test_get_user_vehicles(self):
        data = {
            'nickName': '', 
            'vin': '1FTEW1EP6KKC17890', 
            'vehicleType': '2019 F-150', 
            'color': 'RACE RED', 
            'modelName': 'F-150', 
            'modelCode': 'VLFC', 
            'modelYear': '2019', 
            'tcuEnabled': 1, 
            'localMarketValue': 'F-150',
            'territoryDescription': 'USA', 
            'vehicleAuthorizationStatus': {
                'requestStatus': 'CURRENT', 
                'error': None, 
                'lastRequested': '2021-02-15T05:12:55.041Z', 
                'value': {
                    'authorization': 'AUTHORIZED'
                }
            }, 
            'recallInfo': None
        }
        responses.add('GET', const.VEHICLE_URL + '/dashboard/v1/users/vehicles', json=data)
        actual = self.user.vehicles()
        self.assertEqual("1FTEW1EP6KKC17890", actual['vin'])

    @responses.activate
    def test_add_user_vehicles(self):
        data = {
            "countryCode": "USA", 
            "nickName": "",
            "vin": "1FTEW1EP6KKC17891", 
            "appBrand": "F", 
            "appRegion": "NA"
        }
        responses.add('POST', const.USER_URL + '/garage/mobile', json=data)
        actual = self.user.add_vehicle("1FTEW1EP6KKC17891")

        self.assertEqual("1FTEW1EP6KKC17891", actual['vin'])

    @responses.activate
    def test_delete_user_vehicles(self):
        vin = "1FTEW1EP6KKC17891"
        responses.add('DELETE', const.API_URL + '/users/vehicles/' + vin, json={})
        actual = self.user.delete_vehicle("1FTEW1EP6KKC17891")
        self.assertEqual({}, actual)
