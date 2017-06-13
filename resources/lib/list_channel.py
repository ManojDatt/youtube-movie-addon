import os, sys
import simplejson as json
from urlparse import parse_qsl
import xbmc, xbmcgui, xbmcplugin, xbmcaddon, urllib
# Get the plugin url in plugin:// notation.
__url__ = sys.argv[0]
# Get the plugin handle as an integer number.
__handle__ = int(sys.argv[1])
_addon_ = xbmcaddon.Addon('plugin.video.arka-demo-addon')
home = _addon_.getAddonInfo('path')
fanart = xbmc.translatePath( os.path.join( home, 'resources/data/fanart.jpg' ))
icon = xbmc.translatePath( os.path.join( home, 'resources/data/icon.png' ))
_data_ = xbmc.translatePath(os.path.join(home, "resources/data/source.json"))
with open(_data_) as row:
    data_source_ = json.load(row)
## Get all setting value by ADDON.getSetting("SETTING_ID")
ADDON  = xbmcaddon.Addon()
VIDEOS = data_source_

def get_categories():
    return VIDEOS.keys()


def list_categories():
    categories = get_categories()
    listing = []
    for category in categories:
        list_item = xbmcgui.ListItem(label=category)
        list_item.setProperty('fanart_image', fanart)
        url = '{0}?action=listing&category={1}'.format(__url__, category)
        is_folder = True
        listing.append((url, list_item, is_folder))
    if _addon_.getSetting("setting_show") == "true":
        settings_menu_item = xbmcgui.ListItem(_addon_.getLocalizedString(300020),thumbnailImage=icon)
        settings_menu_item.setProperty('fanart_image', _addon_.getAddonInfo("fanart"))
        url = '{0}?action=settings'.format(__url__)
        listing.append((url, settings_menu_item, True))

    xbmcplugin.addDirectoryItems(__handle__, listing, len(listing))
    xbmcplugin.addSortMethod(__handle__, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(__handle__)
