﻿# -*- coding: utf-8 -*-

"""
*
* LPIP XBMC Addon
* Version 1.2.0
* 
* www.letsplayimpot.de
* 
* Addon written by cyprus/swift
*
*
* Change-Log:
* Version 1.0.0
* - Erstes offizielles Release
*
* Version 1.1.0
* - Bug fixed:     Spielernamen wurden unter Umständen abgeschnitten.
* - Bug fixed:     Spiele mit mehr als 48 Videos und "Alle Spiele von $" mit mehr als 48 Videos wurden nicht angezeigt.
* - Bug fixed:     Kompatibilität zu Linux und OSX Version von XBMC verbessert.
* - Feature added: Spielnamen und Spielernamen werden nun abhängig von der jeweiligen Übersicht angezeigt.
* - Feature added: Spielername, Erscheinungsdatum (im XBMC nicht sichtbar?!), Genre und Spieldauer
*                  werden nun in die Videoinformationen hinzugefügt.
*
* Version 1.2.0
* - Feature added: "Meist gesehene Videos" hinzugefügt.
* - Feature added: "Längste Videos" hinzugefügt.
"""

import urllib, urllib2, re
import htmlentitydefs

from xml.dom import minidom
url = '?g=2144'
fullUrl = 'http://letsplayimpot.de/' + url
def __RequestData( url ):
    request = urllib2.Request( url )
    request.add_header( 'User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13' )
    #request.add_header( 'Referer', 'http://letsplayimpot.de/' )
    
    response = urllib2.urlopen( request )
    data = response.read()
    response.close()
    
    return data

data = __RequestData( fullUrl )
   
#regEx = re.compile( '<a.*href="(.+?)"[^>]*>[^<]*<span.*class="name"[^>]*>(.+?)<\/span>[^<]*<span.*class="time"[^>]*>([^<]*)<\/span>[^<]*<span class="infos">[^<]*<b>Uploader:<\/b>&nbsp;([^\|]*)\|[^<]*<b>Kategorie:<\/b>&nbsp;([^\|]*)\|[^<]*<b>Views:<\/b>&nbsp;[^\|]*\|[^<]*<b>Länge:<\/b>&nbsp;([^<]*)', re.IGNORECASE )
regEx = re.compile('<b>Von:<\/b>&nbsp;([^\|]*)\|[^<]*<b>Kategorie:<\/b>&nbsp;([^\|]*)\|[^<]*<b>Views:<\/b>&nbsp;[^\|]*\|[^<]*<b>Länge:<\/b>&nbsp;([^<]*)', re.IGNORECASE)
match = regEx.findall( data )

print match



