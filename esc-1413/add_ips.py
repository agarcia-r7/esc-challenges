import ipaddress
import requests

API_KEY = "some API key"
API_HEADER = { "X-Api-Key": API_KEY}
PATH = "/path/to/iocs.csv"
REGION = "us"
THREAT_KEY = "some threat key"

def validate_key():
    try:
        r = requests.get("https://" + REGION + ".api.insight.rapid7.com/validate", headers=API_HEADER)
        if r.status_code == 200:
            print("API key validated")
            return True
        else:
            print("Validation failed: response code " + str(r.status_code))
            return False
    except requests.RequestException as e:
        print(e)
        return False

def add_ip():
    try:
        files = {'file':open(PATH)}
        r = requests.post("https://" + REGION + ".api.insight.rapid7.com/idr/v1/customthreats/key/" + THREAT_KEY + "/indicators/replace", headers=API_HEADER, files=files, data={"format":"csv"})
        print(str(r.status_code) + " - " + r.text)
    except requests.RequestException as e:
        print(e)
        
if validate_key():
    add_ip()

