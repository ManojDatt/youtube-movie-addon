
import os
import sys
from resources.lib.utils import *
from resources.lib.list_channel import *
import xbmc, xbmcaddon
import base64
addonID = 'plugin.video.arka-demo-addon'
__addon__ = xbmcaddon.Addon(id=addonID)
home = __addon__.getAddonInfo('path')
fanart = xbmc.translatePath( os.path.join( home, 'resources/data/fanart.jpg' ))
icon = xbmc.translatePath( os.path.join( home, 'resources/data/icon.png' ))
base_url = base64.b64decode("cGx1Z2luOi8vcGx1Z2luLnZpZGVvLnlvdXR1YmUv")
from resources.lib.data_source import data_sources

VIDEOS = data_sources()

def main_list(params):
    for video in VIDEOS[params['category']]:
        list_icon = xbmc.translatePath( os.path.join( home, video['icon'] ))
        add_item(title=video['title'],
                 url="plugin://plugin.video.youtube/"+video['channel']+"/",
                 thumbnail=list_icon,
                 folder=True )
    close_item_list()

def router(paramstring):
    params = dict(parse_qsl(paramstring[1:]))
    name = __addon__.getSetting("playername")
    password = __addon__.getSetting("playerpass")
    if name =="MYUSER" and password=="PASSWORD":
        params = get_params()
        if params.get("action") == "listing":
            main_list(params)
        elif params.get("action") == "settings":
            __addon__.openSettings()
        else:
            list_categories()

    else:
        dialog = xbmcgui.Dialog()
        dialog.ok("Setting", "Please enter your trial account username: MYUSER, and password: PASSWORD in general setting tab.")
        __addon__.openSettings()


if __name__ == '__main__':
    router(sys.argv[2])
