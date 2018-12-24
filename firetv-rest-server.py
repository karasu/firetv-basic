#!/usr/bin/python

import subprocess

from flask import Flask

app = Flask(__name__)


def connect_firetv(firetv_ip='192.168.1.3'):
    """ Connect to firetv in debug mode """
    cmd = ['adb', 'connect', firetv_ip]
    subprocess.call(cmd)


def awake_firetv():
    """ Awake firetv """
    cmd = ['adb', 'shell', 'input', 'keyevent']
    
    # KEYCODE_WAKEUP
    subprocess.call(cmd + ['224'])

    # UNLOCK SCREEN
    subprocess.call(cmd + ['82'])


@app.route('/<application>')
def run_app(application):
    """ Run app in firetv basic stick using android debugger """

    apps = {
        'netflix': 'com.netflix.ninja/.MainActivity',
        'prime': 'com.amazon.amazonvideo.livingroom.firetv/com.amazon.ignition.FireOsIgnitionActivity',
        'kodi': 'org.xbmc.kodi/.Splash',
        'movistar': 'com.movistarplus.androidtv/.MainActivity'
    }

    cmd = ['/usr/bin/adb', 'shell', 'am', 'start', '-n']

    myapp = apps.get(application, None)

    if myapp:
        connect_firetv()
        awake_firetv()
        cmd = ['/usr/bin/adb', 'shell', 'am', 'start', '-n', myapp]
        subprocess.call(cmd)
        return "{} opened".format(application)
    else:
        return "Unknown application"
