#! /usr/bin/python3
import requests  # from requests
import json
import gpiozero  # from RPi.GPIO

# init config
host = "sunpowerconsole.com"
path  = "http://{host}/cgi-bin/dl_cgi?Command={command}"


def get(command):
    """ Return JSON block from the console API """
    url = path.format(path, host=host, command=command)
    req = requests.get(url)
    return req.json()

# ALWAYS start a session with a `Start` command
get("Start")
list = get("DeviceList")
# Not technically needed, but polite to terminate a session
get("Stop")

panels = []
temps = []
gen = 0

for device in list.get('devices'):
    if device["DEVICE_TYPE"] == "Inverter":
        panels.append({
            "id": device["SERIAL"],
            "kw": float(device["p_3phsum_kw"]),
            "temperature": float(device["t_htsnk_degc"]),
            })
        gen += float(device["p_3phsum_kw"])
        temps.append(float(device["t_htsnk_degc"]))

# Report the Pi CPU temperature.
cpu = gpiozero.CPUTemperature()
temps.sort()

# get the average temperature of the panels.
avg_panel = 0
for t in temps:
    avg_panel += t
avg_panel = avg_panel / len(temps)

# HASS YAML sometimes accepts the panel dict, sometimes
# doesn't.
out = {
    "pi": round(cpu.temperature, 2),
    "generated": round(gen, 2),
    "panel_temp_avg": round(avg_panel, 2),
    "panel_temp_low": temps[0],
    "panel_temp_hi": temps[-1],
    #"panels": panels,
    }

# Flatten out the panels into unique values.
for panel in panels:
    id = "panel_{}".format(panel["id"][-2:])
    out["{}_kw".format(id)] = panel["kw"]
    out["{}_temp".format(id)] = panel["temperature"]

print("Content-Type: application/json\n")
print(json.dumps(out, indent=1))
