import xbmc, xbmcaddon, os
import simplejson as json
addonID = 'plugin.video.arka-demo-addon'
__addon__ = xbmcaddon.Addon(id=addonID)
home = __addon__.getAddonInfo('path')

def data_sources():
    _data_ = xbmc.translatePath(os.path.join(home, "resources/data/source.json"))
    with open(_data_) as row:
        data_source_ = json.load(row)
    return data_source_
