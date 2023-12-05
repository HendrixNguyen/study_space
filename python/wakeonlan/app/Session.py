

import os

import requests


class Session():

  def __init__(self) -> None:
    self.request = requests.Session()
    self.host = os.getenv('API_URL', 'localost')

  def getNetwork(self):
    self.request.get('https://hendrix-lab.duckdns.org:8006/api2/json/',headers={
      "Authorization": f"PVEAPIToken=root@pam!id1={self.host}"
    } )