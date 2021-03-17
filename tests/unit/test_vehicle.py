import unittest
import responses
import syncconnect
from syncconnect import const

class TestVehicle(unittest.TestCase):

    def setUp(self):
        self.vin = '1FTEW1EP6KKC17890'
        self.vehicle = syncconnect.Vehicle(self.vin, 'access_token')

    @responses.activate
    def test_get_vehicle_info(self):
        data = {
            'requestStatus': 'CACHED', 
            'error': None, 
            'lastRequested': '2021-03-17T05:23:38.007Z', 
            'cachedOn': '2021-03-08T02:50:28', 
            'value': {
                'vin': '1FTEW1EP6KKC17890'
            }
        }
        responses.add('GET', const.VEHICLE_URL + '/vinlookup/v1/vins/'+self.vin+'/detail?country=USA&language=EN', json=data)
        actual = self.vehicle.info()

        self.assertEqual(self.vin, actual['value']['vin'])

    @responses.activate
    def test_get_vehicle_status(self):
        data = {
            'vehiclestatus': {
                'vin': '1FTEW1EP6KKC17890',
                'lockStatus': {
                    'value': 'UNLOCKED', 
                    'status': 'CURRENT', 
                    'timestamp': '03-16-2021 20:57:41'
                }
            }
        }
        responses.add('GET', const.API_URL + '/vehicles/v4/'+self.vin+'/status?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.status()

        self.assertEqual(self.vin, actual['vehiclestatus']['vin'])

    @responses.activate
    def test_get_vehicle_status(self):
        data = {
            '$id': '1', 
            'vehiclestatus': {
                '$id': '2', 
                'vin': '1FTEW1EP6KKC17890',
                'lockStatus': {
                    '$id': '3', 
                    'value': 'LOCKED'
                }
            }
        }
        responses.add('GET', const.API_URL + '/vehicles/v3/'+self.vin +
                      '/statusrefresh/ffe168a3-657f-4b74-9668-909c60e2379f', json=data)
        actual = self.vehicle.refresh_status()

        self.assertEqual('1FTEW1EP6KKC17890', actual['vehiclestatus']['vin'])

    # @responses.activate
    # def test_send_auth(self):
    #     responses.add('POST', const.API_URL + '/vehicles/v2/'+self.vin+'/drivers', json=None)
    #     actual = self.vehicle.send_auth()

    @responses.activate
    def test_auth_status(self):
        data = {
            '$id': '1', 
            'vehicleAuthorizationStatus': {
                '$id': '2', 
                'vin': '1FTEW1EP6KKC17890',
                'authorization': 'AUTHORIZED',
                'lastRefresh': '03-17-2021 05:41:29', 
                'lastModifiedDate': '03-17-2021 05:41:29'
            }, 
            'status': 200, 
            'version': '1.0.0'
        }
        responses.add('GET', const.API_URL + '/vehicles/'+self.vin+'/authstatus?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.auth_status()
        self.assertEqual(self.vin, actual['vehicleAuthorizationStatus']['vin'])

    @responses.activate
    def test_get_details(self):
        data = {
            'vehicle': {
                'vin': '1FTEW1EP6KKC17890',
                'nickName': ''
            }
        }
        responses.add('GET', const.API_URL + '/users/vehicles/'+self.vin+'/detail?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.details()
        self.assertEqual(self.vin, actual['vehicle']['vin'])

    @responses.activate
    def test_get_recalls(self):
        data = {
            'vehicle': {
                'vin': '1FTEW1EP6KKC17890',
                'nickName': ''
            }
        }
        responses.add('GET', const.API_URL + '/recall/v2/recalls?vin=' +
                      self.vin+'&language=EN&region=US&country=USA', json=data)
        actual = self.vehicle.recalls()
        self.assertEqual(self.vin, actual['vehicle']['vin'])

    @responses.activate
    def test_get_maintenance(self):
        data = {
            'vehicle': {
                'vin': '1FTEW1EP6KKC17890',
                'nickName': ''
            }
        }
        responses.add('GET', const.API_URL + '/vehiclemaintenance/v1/maintenance-schedule?vin=' +
                      self.vin+'&language=EN&country=USA', json=data)
        actual = self.vehicle.maintenance_schedule()
        self.assertEqual(self.vin, actual['vehicle']['vin'])

    @responses.activate
    def test_get_capability(self):
        data = {
            'vehicle': {
                'vin': '1FTEW1EP6KKC17890',
                'nickName': ''
            }
        }
        responses.add('GET', const.API_URL + '/capability/v1/vehicles/'+self.vin, json=data)
        actual = self.vehicle.capability()
        self.assertEqual(self.vin, actual['vehicle']['vin'])

    @responses.activate
    def test_get_vin(self):
        data = {
            'vehiclestatus': {
                'vin': '1FTEW1EP6KKC17890',
            }
        }
        responses.add('GET', const.API_URL + '/vehicles/v4/' +
                      self.vin+'/status?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.vin()
        self.assertEqual(self.vin, actual['data'])

    @responses.activate
    def test_get_odometer(self):
        data = {
            'vehiclestatus': {
                'odometer': {
                    'milage': 2000
                },
            }
        }
        responses.add('GET', const.API_URL + '/vehicles/v4/' +
                      self.vin + '/status?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.odometer()
        self.assertEqual(2000, actual['data']['milage'])

    @responses.activate
    def test_get_fuel(self):
        data = {
            'vehiclestatus': {
                'fuel': {
                    'level': 75
                },
            }
        }
        responses.add('GET', const.API_URL + '/vehicles/v4/' +
                      self.vin + '/status?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.fuel()
        self.assertEqual(75, actual['data']['level'])

    @responses.activate
    def test_get_oil(self):
        data = {
            'vehiclestatus': {
                'oil': {
                    'life': 95
                },
            }
        }
        responses.add('GET', const.API_URL + '/vehicles/v4/' +
                      self.vin + '/status?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.oil()
        self.assertEqual(95, actual['data']['life'])

    @responses.activate
    def test_get_tire_pressure(self):
        data = {
            'vehiclestatus': {
                'TPMS': {
                    'driver': 35,
                    'passenger': 33
                },
            }
        }
        responses.add('GET', const.API_URL + '/vehicles/v4/' +
                      self.vin + '/status?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.tire_pressure()
        self.assertEqual(35, actual['data']['driver'])
        self.assertEqual(33, actual['data']['passenger'])

    @responses.activate
    def test_get_battery(self):
        data = {
            'vehiclestatus': {
                'battery': 100,
            }
        }
        responses.add('GET', const.API_URL + '/vehicles/v4/' + self.vin + '/status?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.battery()
        self.assertEqual(100, actual['data'])

    @responses.activate
    def test_get_location(self):
        data = {
            'vehiclestatus': {
                'gps': {
                    'longitude': "42.3153",
                    'latitude': "-83.2103"
                }
            }
        }
        responses.add('GET', const.API_URL + '/vehicles/v4/' +
                      self.vin + '/status?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.location()
        self.assertEqual("42.3153", actual['data']['longitude'])
        self.assertEqual("-83.2103", actual['data']['latitude'])

    @responses.activate
    def test_get_window_position(self):
        data = {
            'vehiclestatus': {
                'windowPosition': {
                    'driver': "CLOSED",
                    'passenger': "CLOSED"
                }
            }
        }
        responses.add('GET', const.API_URL + '/vehicles/v4/' +
                      self.vin + '/status?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.window_positions()
        self.assertEqual("CLOSED", actual['data']['driver'])
        self.assertEqual("CLOSED", actual['data']['passenger'])

    @responses.activate
    def test_get_door_status(self):
        data = {
            'vehiclestatus': {
                'doorStatus': {
                    'driver': "CLOSED",
                    'passenger': "CLOSED"
                }
            }
        }
        responses.add('GET', const.API_URL + '/vehicles/v4/' + self.vin + '/status?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.door_status()
        self.assertEqual("CLOSED", actual['data']['driver'])
        self.assertEqual("CLOSED", actual['data']['passenger'])

    @responses.activate
    def test_get_lock_status(self):
        data = {
            'vehiclestatus': {
                'lockStatus': {
                    'driver': "LOCKED",
                    'passenger': "LOCKED"
                }
            }
        }
        responses.add('GET', const.API_URL + '/vehicles/v4/' +
                      self.vin + '/status?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.lock_status()
        self.assertEqual("LOCKED", actual['data']['driver'])
        self.assertEqual("LOCKED", actual['data']['passenger'])

    @responses.activate
    def test_get_lock_status(self):
        data = {
            'vehiclestatus': {
                'alarm': {
                    'status': "OFF"
                }
            }
        }
        responses.add('GET', const.API_URL + '/vehicles/v4/' +
                      self.vin + '/status?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.alarm_status()
        self.assertEqual("OFF", actual['data']['status'])

    @responses.activate
    def test_get_ignition_status(self):
        data = {
            'vehiclestatus': {
                'ignitionStatus': {
                    'KEY_IN_IGNITION': "FALSE"
                }
            }
        }
        responses.add('GET', const.API_URL + '/vehicles/v4/' +
                      self.vin + '/status?lrdt=01-01-1970%2000:00:00', json=data)
        actual = self.vehicle.ignition_status()
        self.assertEqual("FALSE", actual['data']['KEY_IN_IGNITION'])

    @responses.activate
    def test_wakeup(self):
        responses.add('GET', const.USER_URL + '/dashboard/v1/users/vehicles?language=EN&wakeupVin=' +
                      self.vin+'&skipRecall=true&country=USA&region=US', json={})
        actual = self.vehicle.wakeup()
        self.assertEqual({}, actual)

    @responses.activate
    def test_start(self):
        data = {
            "commandId": '123'
        }
        responses.add('PUT', const.API_URL + '/vehicles/v2/' + self.vin+'/engine/start', json=data)
        responses.add('GET', const.API_URL + '/vehicles/' + self.vin+'/engine/start/'+data['commandId'], json={'status': 200})
        actual = self.vehicle.start()
        self.assertEqual({'status': 200}, actual)

    @responses.activate
    def test_stop(self):
        data = {
            "commandId": '123'
        }
        responses.add('DELETE', const.API_URL + '/vehicles/v2/' +
                      self.vin+'/engine/start', json=data)
        responses.add('GET', const.API_URL + '/vehicles/' + self.vin +
                      '/engine/start/'+data['commandId'], json={'status': 200})
        actual = self.vehicle.stop()
        self.assertEqual({'status': 200}, actual)

    @responses.activate
    def test_lock(self):
        data = {
            "commandId": '123'
        }
        responses.add('PUT', const.API_URL + '/vehicles/v2/' +
                      self.vin+'/doors/lock', json=data)
        responses.add('GET', const.API_URL + '/vehicles/' + self.vin +
                      '/doors/lock/'+data['commandId'], json={'status': 200})
        actual = self.vehicle.lock()
        self.assertEqual({'status': 200}, actual)

    @responses.activate
    def test_lock(self):
        data = {
            "commandId": '123'
        }
        responses.add('DELETE', const.API_URL + '/vehicles/v2/' +
                      self.vin+'/doors/lock', json=data)
        responses.add('GET', const.API_URL + '/vehicles/' + self.vin +
                      '/doors/lock/'+data['commandId'], json={'status': 200})
        actual = self.vehicle.unlock()
        self.assertEqual({'status': 200}, actual)

