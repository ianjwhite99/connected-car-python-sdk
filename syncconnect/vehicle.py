from .api import Api
from . import const

class Vehicle(object):

    def __init__(self, vehicle_id, access_token):
        self.access_token = access_token
        self.vehicle_id = vehicle_id
        self.api = Api(access_token)

    def vin_info(self):
        response = self.api.get(const.VEHICLE_URL, 'vinlookup/v1/vins/'+self.vehicle_id+'/detail?country=USA&language=EN')
        return response.json()

    # Not Working
    def status(self):
        response = self.api.get(const.API_URL, 'vehicles/v4/'+self.vehicle_id+'/status?lrdt=01-01-1970%2000:00:00')
        return response.json()

    def send_auth(self):
        response = self.api.post(const.API_URL, 'vehicles/v2/'+self.vehicle_id+'/drivers', None)
        return response

    def auth_status(self):
        response = self.api.get(const.API_URL, 'vehicles/'+self.vehicle_id+'/authstatus?lrdt=01-01-1970%2000:00:00')
        return response.json()

    def details(self):
        response = self.api.get(const.API_URL, 'users/vehicles/'+self.vehicle_id+'/detail?lrdt=01-01-1970%2000:00:00')
        return response.json()

    # Not Working
    def start(self):
        job_id = self.api.action('PUT', const.API_URL, 'vehicles/v2/'+self.vehicle_id+'/engine/start').json()['commandId']
        response = self.api.action('GET', const.API_URL, 'vehicles/'+self.vehicle_id+'/engine/start/'+job_id)
        return response.json()
    
    # Not Working
    def stop(self):
        job_id = self.api.action('DELETE', const.API_URL, 'vehicles/v2/'+self.vehicle_id+'/engine/start').json()['commandId']
        response = self.api.action('GET', const.API_URL, 'vehicles/'+self.vehicle_id+'/engine/start/'+job_id)
        return response.json()

    # Not Working
    def lock(self):
        job_id = self.api.action('PUT', const.API_URL, 'vehicles/v2/'+self.vehicle_id+'/doors/lock').json()['commandId']
        response = self.api.action('GET', const.API_URL, 'vehicles/'+self.vehicle_id+'/doors/lock/'+job_id)
        return response.json()

    # Not Working
    def unlock(self):
        job_id = self.api.action('DELETE', const.API_URL, 'vehicles/v2/'+self.vehicle_id+'/doors/lock').json()['commandId']
        response = self.api.action('GET', const.API_URL, 'vehicles/'+self.vehicle_id+'/doors/lock/'+job_id)
        return response.json()
