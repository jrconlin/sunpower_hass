import json
import time
from urllib import request

"""
SunPower does not provide a consumer accessible API.
This has not stopped me.
They do provide a website you can use to monitor your panels, so
a bit of hackery is required.
 1) Log in to the https://monitor.us.sunpower.com/#/dashboard site.
 2) In your favorite browser of choice, open the Developer Tools
 3) Watch the network traffic (you may need to reload the page)
 4) You'll see a number of urls like:
  https://monitor.us.sunpower.com/CustomerPortal/Alerts/Alerts.svc/GetAlerts?id=12345678-1234-1234-1234-1234567890ab
 5) Copy the "id" value into the GUID below:
"""

GUID = "12345678-1234-1234-1234-1234567890ab"

"""
In HASS, I've set up the following custom sensor:

sensor:
  - platform: command_line
    scan_interval: 300
    name: Solar Production
    command: python sunpower.py
    unit_of_measurement: "kW"


TODO:
    * Make this a proper HASS module. (Maybe, because I also don't want to
        tip sunpower about their awesome site security model. ._.

"""


def smooth(value):
    """Attempt to "smooth" the data to prevent spikes on cloudy days. """
    try:
        with open("/tmp/solar.data", "r+") as history:
            data = json.loads(history.read())
            data.append(value)
            history.seek(0)
            data = data[-5:]
            history.write(json.dumps(data))
            history.truncate()
    except Exception as ex:
        with open("/tmp/solar_error.log", "a") as log:
            log.write("{}: {}\n".format(time.strftime("%D-%T"), ex))
        data = [0, 0, 0, 0, value]
        with open("/tmp/solar.data", "w") as history:
            history.write(json.dumps(data))
    return sum(data) / float(len(data))


def get_ts(offset_secs=0):
    zulu = "%Y-%m-%dT%H:%M:00"
    now = time.localtime(int(time.time() + offset_secs))
    return time.strftime(zulu, now)


def fetch(offset=30):
    """Fetch the data from SunPower. The panels update once every 5 minutes
    or so. """

    url = ("https://monitor.us.sunpower.com/CustomerPortal/SystemInfo/"
           "SystemInfo.svc/getPVProductionData")
    args = dict(
            id=GUID,
            interval="minute",
            startDateTime=get_ts(-(offset*60)),
            endDateTime=get_ts(+120)
            )
    headers = {
            'Accept': "application/json, text/plain",
            'Accept-Language': "en-US;en;q=0.5",
            }

    # can't use requests because ":"
    arg_list = []
    for arg in args.items():
        arg_list.append("{}={}".format(arg[0], arg[1]))
    url = "{}?{}".format(url, "&".join(arg_list))
    req = request.Request(
            url=url,
            headers=headers,
            method="GET")
    with request.urlopen(req) as resp:
        content = resp.read().decode('utf-8')
        return json.loads(content)


def latest_data(offset=30):
    data = fetch(offset)
    if int(data.get('StatusCode', 500)) != 200:
        raise Exception("Bad reply: {}".format(
            data.get('ResponseMessage', "Unknown")))

    current = data.get('Payload', {
        }).get('CurrentProduction', {}).get('value', 0)
    return smooth(float(current))


def main():
    try:
        print(latest_data())
    except Exception as ex:
        print("Error:{}".format(ex))


main()
