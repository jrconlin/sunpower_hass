# Hacky HomeAssistant SunPower sensor module

*NOTE* I do not plan on maintaining this code. It is provided for
educational and legacy reasons.

This is a quick sensor script that can be used by [HomeAssistant](http://homeassistant.io) (sorta).

[SunPower](https://us.sunpower.com/home-solar/) does not provide a consumer accessible API.

They do provide a website you can use to monitor your panels, so a bit of hackery is required.

## *_Please note_:*
As metioned, the SunPower "API" leaves much to be desired. I'm probably not going to continue messing with trying to pull data out of the web-API and have sinced moved to
[_direct_](../direct) access of the data via the Sunpower controller box.

## Installing
I'd recommend installing this using python `virtualenv`. If you're not familiar with the python installation incantation, it's:

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
    scan_interval: 300
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
