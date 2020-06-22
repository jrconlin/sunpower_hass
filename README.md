# Hacky HomeAssistant SunPower sensor module

This is a quick sensor script that can be used by [HomeAssistant](http://homeassistant.io) (sorta).

[SunPower](https://us.sunpower.com/home-solar/) does not provide a consumer accessible API.

They do provide a website you can use to monitor your panels, so a bit
of hackery is required.

## Installing
I'd recommend installing this using python `virtualenv`. If you're not familiar with the
python installation incantation, it's:

```bash
$ virtualenv -p python3 venv
$ venv/bin/python setup.py install
```

## Running

You can run the program either as
```bash
$ venv/python sunpower
```

or
```bash
$ venv/reading
```

## Using in Home Assistant

In [HASS](http://homeassistant.io/), I've set up the following custom sensor:

```yaml
sensor:
  - platform: command_line
    scan_interval: 1800
    name: Solar Production
    command: reading
    unit_of_measurement: "kW"
```
**NOTE**: You'll have to specify the directory you installed in the command line.
(e.g. if you installed on `/home/bob/sunpower_hass/` you'd use
```yaml
   ...
   command: /home/bob/sunpower_hass/venv/reading
```
)

##TODO:

* Make this a proper HASS module.

## More Info Than You Want

I have no idea why they make this hard.

First off, your sunpower unit sends updates of the current power load
every five minutes. For reasons, the site updates data once an hour.

Sunpower's site system breaks fairly frequently with connectivity
issues causing data backlogs (they appear as dips & spikes as data is
accumulated).

There are no published endpoints that let you query the data locally.

I do my best to be as kind as possible here, the script only queries
once per hour and logs in like any browser client would.

The monitoring panel does not appear to have any TCP socket we can
read, nor does it use the  so yay? good security?

Still, kinda dumb that a device, sitting on your network doesn't
expose a simple port that returns just the current power generation
level.
