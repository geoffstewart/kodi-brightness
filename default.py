# import the kodi python modules we are going to use
# see the kodi api docs to find out what functionality each module provides
import xbmc
import xbmcgui
import xbmcaddon
import time

# create a class for your addon, we need this to get info about your addon
ADDON = xbmcaddon.Addon()
# get the full path to your addon, decode it to unicode to handle special (non-ascii) characters in the path
CWD = ADDON.getAddonInfo('path')

# this is the entry point of your addon, execution of your script will start here
if (__name__ == '__main__'):
    # open the osdvideosettings, click DONW 8 times and select to get brightness dialog
    xbmc.executebuiltin('ActivateWindow(osdvideosettings)')
    xbmc.executebuiltin('Action(Down)')
    xbmc.executebuiltin('Action(Down)')
    xbmc.executebuiltin('Action(Down)')
    xbmc.executebuiltin('Action(Down)')
    xbmc.executebuiltin('Action(Down)')
    xbmc.executebuiltin('Action(Down)')
    xbmc.executebuiltin('Action(Down)')
    xbmc.executebuiltin('Action(Down)')
    xbmc.executebuiltin('Action(Select)')
# the end!
