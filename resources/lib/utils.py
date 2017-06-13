import xbmc, xbmcplugin, xbmcaddon, xbmcgui, urllib, urllib2, re, sys, os, time, socket
from StringIO import StringIO
import gzip

addonID = 'plugin.video.arka-demo-addon'
__addon__ = xbmcaddon.Addon(id=addonID)
home = __addon__.getAddonInfo('path')
__handle__ = int(sys.argv[1])


def get_params():
    param_string = sys.argv[2]
    commands = {}

    if param_string:
        split_commands = param_string[param_string.find('?') + 1:].split('&')

        for command in split_commands:
            if len(command) > 0:
                if "=" in command:
                    split_command = command.split('=')
                    key = split_command[0]
                    value = urllib.unquote_plus(split_command[1])
                    commands[key] = value
                else:
                    commands[command] = ""
    return commands

def add_item( action="" , title="" , plot="" , url="" , thumbnail="" , fanart="" , show="" , episode="" , extra="", page="", info_labels = None, isPlayable = False , folder=True ):

    listitem = xbmcgui.ListItem( title, iconImage="DefaultVideo.png", thumbnailImage=thumbnail )
    if info_labels is None:
        info_labels = { "Title" : title, "FileName" : title, "Plot" : plot }
    listitem.setInfo( "video", info_labels )

    if fanart!="":
        listitem.setProperty('fanart_image',fanart)
        xbmcplugin.setPluginFanart(__handle__, fanart)

    if url.startswith("plugin://"):
        itemurl = url
        listitem.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem( handle=__handle__, url=itemurl, listitem=listitem, isFolder=folder)
    elif isPlayable:
        listitem.setProperty("Video", "true")
        listitem.setProperty('IsPlayable', 'true')
        itemurl = '%s?action=%s&title=%s&url=%s&thumbnail=%s&plot=%s&extra=%s&page=%s' % ( sys.argv[ 0 ] , action , urllib.quote_plus( title ) , urllib.quote_plus(url) , urllib.quote_plus( thumbnail ) , urllib.quote_plus( plot ) , urllib.quote_plus( extra ) , urllib.quote_plus( page ))
        xbmcplugin.addDirectoryItem( handle=__handle__, url=itemurl, listitem=listitem, isFolder=folder)
    else:
        itemurl = '%s?action=%s&title=%s&url=%s&thumbnail=%s&plot=%s&extra=%s&page=%s' % ( sys.argv[ 0 ] , action , urllib.quote_plus( title ) , urllib.quote_plus(url) , urllib.quote_plus( thumbnail ) , urllib.quote_plus( plot ) , urllib.quote_plus( extra ) , urllib.quote_plus( page ))
        xbmcplugin.addDirectoryItem( handle=__handle__, url=itemurl, listitem=listitem, isFolder=folder)

def close_item_list():
    xbmcplugin.endOfDirectory(handle=__handle__, succeeded=True)

def get_media_path(qstring):
    return xbmc.translatePath( os.path.join( home, qstring ))
