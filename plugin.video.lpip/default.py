# -*- coding: utf-8 -*-

"""
*
* LPIP XBMC Addon
* Version 1.2.2
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
*
* Version 1.2.1
* - Feature added: "Fixed Regex for ShowGame"
*
* Version 1.2.2
* - Bug fixed:     Removed python api 1 (https://github.com/bomba1988/xbmc-lpip/issues/1)
*
"""

import urllib, urllib2, re, xbmcplugin, xbmcgui
import htmlentitydefs

from xml.dom import minidom

def ShowStartOverview():
    __AddDirectory( 'Neueste Videos', '', 'SHOW_NEWEST', '' )
    __AddDirectory( 'Meist gesehene Videos', '', 'SHOW_MOST_VIEWED', '' )
    __AddDirectory( 'Längste Videos', '', 'SHOW_LONGEST', '' )

    __AddDirectory( 'User', '', 'SHOW_USERS', '' )
    __AddDirectory( 'Spiele', '', 'SHOW_GAMES', '' )
    __AddDirectory( 'Kategorien', '', 'SHOW_CATEGORIES', '' )
    __AddDirectory( 'Tutorials', '', 'SHOW_TUTORIALS', '' )

    __AddDirectory( 'Suchen...', '', 'SEARCH_GAME', '' )

def ShowNewest( url ):
    """ Media-RSS Feed Methode
    items = __RequestRSSFeed();

    if( len( items ) > 0 ):
        for item in items:
            titleNode = __GetNodeByName( item.childNodes, 'title' )
            title = __GetNodeData( titleNode )

            enclosureNode = __GetNodeByName( item.childNodes, 'enclosure' )
            url = __GetNodeAttribute( enclosureNode, 'url' )

            __AddVideoLink( title, url, '' )
    """

    """ HTML-Methode """
    start = 1

    if( not( url is None ) and len( url ) > 0 ):
        start = int( url )

    url = 'video.php?action=get_rows&start=' + str( start ) + '&sort=Datum'

    __AddDirectory( '→ Nächste Seite...', str( start + 1 ), 'SHOW_NEWEST', '' )

    if( not( start == 1 ) ):
        __AddDirectory( '← Vorherige Seite...', str( start - 1 ), 'SHOW_NEWEST', '' )

    ShowGame( url, 'SHOW_NEWEST' )

    if( not( start == 1 ) ):
        __AddDirectory( '← Vorherige Seite...', str( start - 1 ), 'SHOW_NEWEST', '' )

    __AddDirectory( '→ Nächste Seite...', str( start + 1 ), 'SHOW_NEWEST', '' )

def ShowMostViewed( url ):
    start = 1

    if( not( url is None ) and len( url ) > 0 ):
        start = int( url )
        
    url = 'video.php?action=get_rows&start=' + str( start ) + '&sort=Views'
    
    __AddDirectory( '→ Nächste Seite...', str( start + 1 ), 'SHOW_MOST_VIEWED', '' )
    
    if( not( start == 1 ) ):
        __AddDirectory( '← Vorherige Seite...', str( start - 1 ), 'SHOW_MOST_VIEWED', '' )
    
    ShowGame( url, 'SHOW_MOST_VIEWED' )
    
    if( not( start == 1 ) ):
        __AddDirectory( '← Vorherige Seite...', str( start - 1 ), 'SHOW_MOST_VIEWED', '' )
    
    __AddDirectory( '→ Nächste Seite...', str( start + 1 ), 'SHOW_MOST_VIEWED', '' )

def ShowLongest( url ):
    start = 1
    
    if( not( url is None ) and len( url ) > 0 ):
        start = int( url )
        
    url = 'video.php?action=get_rows&start=' + str( start ) + '&sort=Länge'
    
    __AddDirectory( '→ Nächste Seite...', str( start + 1 ), 'SHOW_LONGEST', '' )
    
    if( not( start == 1 ) ):
        __AddDirectory( '← Vorherige Seite...', str( start - 1 ), 'SHOW_LONGEST', '' )
    
    ShowGame( url, 'SHOW_LONGEST' )
    
    if( not( start == 1 ) ):
        __AddDirectory( '← Vorherige Seite...', str( start - 1 ), 'SHOW_LONGEST', '' )
    
    __AddDirectory( '→ Nächste Seite...', str( start + 1 ), 'SHOW_LONGEST', '' )    

def ShowUsers( url ):
    if( not( url is None ) and len( url ) > 0 ):
        url = 'http://letsplayimpot.de/userlist.php' + url
    
        __GenerateListOverview( url, 'SHOW_USER_GAMES' )
    else:
        __AddDirectory( '#', '?action=get_rows&start=0', 'SHOW_USERS', '' )
        __AddDirectory( 'A', '?action=get_rows&start=1', 'SHOW_USERS', '' )
        __AddDirectory( 'B', '?action=get_rows&start=2', 'SHOW_USERS', '' )
        __AddDirectory( 'C', '?action=get_rows&start=3', 'SHOW_USERS', '' )
        __AddDirectory( 'D', '?action=get_rows&start=4', 'SHOW_USERS', '' )
        __AddDirectory( 'E', '?action=get_rows&start=5', 'SHOW_USERS', '' )
        __AddDirectory( 'F', '?action=get_rows&start=6', 'SHOW_USERS', '' )
        __AddDirectory( 'G', '?action=get_rows&start=7', 'SHOW_USERS', '' )
        __AddDirectory( 'H', '?action=get_rows&start=8', 'SHOW_USERS', '' )
        __AddDirectory( 'I', '?action=get_rows&start=9', 'SHOW_USERS', '' )
        __AddDirectory( 'J', '?action=get_rows&start=10', 'SHOW_USERS', '' )
        __AddDirectory( 'K', '?action=get_rows&start=11', 'SHOW_USERS', '' )
        __AddDirectory( 'L', '?action=get_rows&start=12', 'SHOW_USERS', '' )
        __AddDirectory( 'M', '?action=get_rows&start=13', 'SHOW_USERS', '' )
        __AddDirectory( 'N', '?action=get_rows&start=14', 'SHOW_USERS', '' )
        __AddDirectory( 'O', '?action=get_rows&start=15', 'SHOW_USERS', '' )
        __AddDirectory( 'P', '?action=get_rows&start=16', 'SHOW_USERS', '' )
        __AddDirectory( 'Q', '?action=get_rows&start=17', 'SHOW_USERS', '' )
        __AddDirectory( 'R', '?action=get_rows&start=18', 'SHOW_USERS', '' )
        __AddDirectory( 'S', '?action=get_rows&start=19', 'SHOW_USERS', '' )
        __AddDirectory( 'T', '?action=get_rows&start=20', 'SHOW_USERS', '' )
        __AddDirectory( 'U', '?action=get_rows&start=21', 'SHOW_USERS', '' )
        __AddDirectory( 'V', '?action=get_rows&start=22', 'SHOW_USERS', '' )
        __AddDirectory( 'W', '?action=get_rows&start=23', 'SHOW_USERS', '' )
        __AddDirectory( 'X', '?action=get_rows&start=24', 'SHOW_USERS', '' )
        __AddDirectory( 'Y', '?action=get_rows&start=25', 'SHOW_USERS', '' )
        __AddDirectory( 'Z', '?action=get_rows&start=26', 'SHOW_USERS', '' )

def ShowUserGames( url ):
    url = 'http://letsplayimpot.de/' + url

    __GenerateListOverview( url, 'SHOW_GAME', 'SHOW_USER_GAMES' )

def ShowGames( url ):
    if( not( url is None ) and len( url ) > 0 ):
        if( url.find( 'c=' ) < 0 ):
            url = 'http://letsplayimpot.de/gameslist.php' + url
        else:
            url = 'http://letsplayimpot.de/' + url

        __GenerateListOverview( url, 'SHOW_GAME', 'SHOW_GAMES' )
    else:
        __AddDirectory( '#', '?action=get_rows&start=0', 'SHOW_GAMES', '' )
        __AddDirectory( 'A', '?action=get_rows&start=1', 'SHOW_GAMES', '' )
        __AddDirectory( 'B', '?action=get_rows&start=2', 'SHOW_GAMES', '' )
        __AddDirectory( 'C', '?action=get_rows&start=3', 'SHOW_GAMES', '' )
        __AddDirectory( 'D', '?action=get_rows&start=4', 'SHOW_GAMES', '' )
        __AddDirectory( 'E', '?action=get_rows&start=5', 'SHOW_GAMES', '' )
        __AddDirectory( 'F', '?action=get_rows&start=6', 'SHOW_GAMES', '' )
        __AddDirectory( 'G', '?action=get_rows&start=7', 'SHOW_GAMES', '' )
        __AddDirectory( 'H', '?action=get_rows&start=8', 'SHOW_GAMES', '' )
        __AddDirectory( 'I', '?action=get_rows&start=9', 'SHOW_GAMES', '' )
        __AddDirectory( 'J', '?action=get_rows&start=10', 'SHOW_GAMES', '' )
        __AddDirectory( 'K', '?action=get_rows&start=11', 'SHOW_GAMES', '' )
        __AddDirectory( 'L', '?action=get_rows&start=12', 'SHOW_GAMES', '' )
        __AddDirectory( 'M', '?action=get_rows&start=13', 'SHOW_GAMES', '' )
        __AddDirectory( 'N', '?action=get_rows&start=14', 'SHOW_GAMES', '' )
        __AddDirectory( 'O', '?action=get_rows&start=15', 'SHOW_GAMES', '' )
        __AddDirectory( 'P', '?action=get_rows&start=16', 'SHOW_GAMES', '' )
        __AddDirectory( 'Q', '?action=get_rows&start=17', 'SHOW_GAMES', '' )
        __AddDirectory( 'R', '?action=get_rows&start=18', 'SHOW_GAMES', '' )
        __AddDirectory( 'S', '?action=get_rows&start=19', 'SHOW_GAMES', '' )
        __AddDirectory( 'T', '?action=get_rows&start=20', 'SHOW_GAMES', '' )
        __AddDirectory( 'U', '?action=get_rows&start=21', 'SHOW_GAMES', '' )
        __AddDirectory( 'V', '?action=get_rows&start=22', 'SHOW_GAMES', '' )
        __AddDirectory( 'W', '?action=get_rows&start=23', 'SHOW_GAMES', '' )
        __AddDirectory( 'X', '?action=get_rows&start=24', 'SHOW_GAMES', '' )
        __AddDirectory( 'Y', '?action=get_rows&start=25', 'SHOW_GAMES', '' )
        __AddDirectory( 'Z', '?action=get_rows&start=26', 'SHOW_GAMES', '' )
        
def ShowCategories():
    url = 'http://letsplayimpot.de/?categoryslist'
    
    __GenerateListOverview( url, 'SHOW_GAMES' )
    
def ShowTutorials():
    ShowGame( '?g=325' )

def ShowGame( url, referer = '' ):
    fullUrl = 'http://letsplayimpot.de/' + url
    data = __RequestData( fullUrl )
    
    regEx = re.compile( '<a.*href="(.+?)"[^>]*>[^<]*<span.*class="name"[^>]*>(.+?)<\/span>[^<]*<span.*class="time"[^>]*>([^<]*)<\/span>[^<]*<span class="infos">[^<]*<b>Von:<\/b>&nbsp;([^\|]*)\|[^<]*<b>Kategorie:<\/b>&nbsp;([^\|]*)\|[^<]*<b>Views:<\/b>&nbsp;[^\|]*\|[^<]*<b>Länge:<\/b>&nbsp;([^<]*)', re.IGNORECASE )
    match = regEx.findall( data )
    
    count = None
    
    if( len( match ) <= 0 and referer != 'SHOW_NEWEST' and referer != 'SHOW_MOST_VIEWED' and referer != 'SHOW_LONGEST' and referer != 'SEARCH_GAME' ):
        url2 = 'http://letsplayimpot.de/gameslist.php' + url + '&action=row_count'
        
        if( referer == 'SHOW_USER_GAMES' ):
            url2 = 'http://letsplayimpot.de/userlist.php' + url + '&action=row_count'
        
        data2 = __RequestData( url2 )
        
        try:
            count = int( data2.strip() )
            
            if( count > 0 ):
                url2 = 'http://letsplayimpot.de/gameslist.php' + url + '&action=get_rows&start=1'
                
                if( referer == 'SHOW_USER_GAMES' ):
                    url2 = 'http://letsplayimpot.de/userlist.php' + url + '&action=get_rows&start=1'
                
                data2 = __RequestData( url2 )
                
                url = url + '&action=get_rows&start=1'
                
                match = regEx.findall( data2 )
        except:
            pass
    
    if( url.find( 'get_rows' ) > -1 and referer != 'SHOW_NEWEST' and referer != 'SHOW_MOST_VIEWED' and referer != 'SHOW_LONGEST' and referer != 'SEARCH_GAME' ):
        if( count is None ):
            url2 = 'http://letsplayimpot.de/gameslist.php' + url.replace( 'get_rows', 'row_count' ).replace( '&start=', '&1' )
            
            if( referer == 'SHOW_USER_GAMES' ):
                url2 = 'http://letsplayimpot.de/userlist.php' + url.replace( 'get_rows', 'row_count' ).replace( '&start=', '&1' )
            
            data2 = __RequestData( url2 )
            
            count = int( data2.strip() )
        
        start = int( url[( url.find( 'start' ) + 6 )] )
        
        nextUrl = url.replace( '&start=' + str( start ), '&start=' + str( start + 1 ) )
        backUrl = url.replace( '&start=' + str( start ), '&start=' + str( start - 1 ) )

        if( ( 48 * start ) < count ):
            __AddDirectory( '→ Nächste Seite...', nextUrl, 'SHOW_GAME', '', referer )
        
        if( start > 1 ):
            __AddDirectory( '← Vorherige Seite...', backUrl, 'SHOW_GAME', '', referer )
        
        __GenerateGameOverview( data, match, referer )

        if( start > 1 ):
            __AddDirectory( '← Vorherige Seite...', backUrl, 'SHOW_GAME', '', referer )
        
        if( ( 48 * start ) < count ):
            __AddDirectory( '→ Nächste Seite...', nextUrl, 'SHOW_GAME', '', referer )
    
    else:
        __GenerateGameOverview( data, match, referer )

def PlayVideo( url ):
    data = __RequestData( 'http://letsplayimpot.de/' + url )
    
    regEx = re.compile( 'file=([^&]*)&amp', re.IGNORECASE )
    match = regEx.findall( data )
    
    videoUrl = ''
    
    for str in match:
        videoUrl = str
    
    if( len( videoUrl ) > 0 ):
        xbmc.Player().play( videoUrl )

def SearchGames():
    searchText = ''
    
    keyboard = xbmc.Keyboard( '', 'Suchen...' )
    keyboard.doModal()
    
    if( keyboard.isConfirmed() ):
        searchText = keyboard.getText()
    
    searchText = searchText.replace( ' ', '%20' )
    searchUrl = 'livesearch.php?q=' + searchText
    
    ShowGame( searchUrl, 'SEARCH_GAME' )

def __GenerateListOverview( url, mode, referer = '' ):
    data = __RequestData( url )
    
    regEx = re.compile( '<a.*href="(.+?)"[^>]*>[^<]*<span.*class="name"[^>]*>(.+?)<\/span>[^<]*<span.*class="time"[^>]*>(.+?)<\/span>', re.IGNORECASE )
    match = regEx.findall( data )
    
    for url, name, count in match:
        orgName = name
        
        try:
            name = __Unescape( name )
            __AddDirectory( name + ' - ' + count, url, mode, '', referer )
        
        except:
            __AddDirectory( orgName + ' - ' + count, url, mode, '', referer )

def __GenerateGameOverview( data, match, referer ):
    for url, name, time, user, categorie, length in match:
        url = url.strip()
        name = name.strip()
        time = time.strip()
        user = user.strip()
        categorie = categorie.strip()
        length = length.strip()
        
        if( referer == 'SHOW_GAMES' or referer == 'SHOW_USER_GAMES' ):
            gameHeader = None
            
            regEx2 = re.compile( '<h1>([^\[]*)', re.IGNORECASE )
            match2 = regEx2.findall( data )
            
            for header in match2:
                gameHeader = header.strip()
            
            if( not( gameHeader is None ) ):
                if( gameHeader.find( user ) > -1 ):
                    gameHeader = gameHeader.replace( user + ' - ', '' ).strip()
                
                name = name.replace( gameHeader + ' - ', '' ).strip()
        
        orgName = name
        orgUser = user

        try:
            name = __Unescape( name )
            user = __Unescape( user )
            
            if( referer == 'SHOW_USER_GAMES' ):
                __AddVideoEmbeddedLink( name, url, '', user, time, categorie, length )
            else:
                __AddVideoEmbeddedLink( name + ' von ' + user, url, '', user, time, categorie, length )
        
        except:
            if( referer == 'SHOW_USER_GAMES' ):
                __AddVideoEmbeddedLink( orgName, url, '', user, time, categorie, length )
            else:
                __AddVideoEmbeddedLink( orgName + ' von ' + orgUser, url, '', user, time, categorie, length )

def __RequestData( url ):
    request = urllib2.Request( url )
    request.add_header( 'User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13' )
    #request.add_header( 'Referer', 'http://letsplayimpot.de/' )
    
    response = urllib2.urlopen( request )
    data = response.read()
    response.close()
    
    return data

def __Unescape(text):
    text = __SpecialChars( text )
    
    def fixup(m):
        text = m.group(0)
        
        if text[:2] == "&#":
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
                    
            except ValueError:
                pass
            
        else:
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
            
        return text
    
    return re.sub( "&#?\w+;", fixup, text )

def __SpecialChars( str ):
    str = str.replace( '&amp;', '&' )
    str = str.replace( '&gt;', '>' )
    str = str.replace( '&lt;', '<' )
    
    str = str.replace( '&#196;', 'Ä' )
    str = str.replace( '&#228;', 'ä' )
    
    str = str.replace( '&#214;', 'Ö' )
    str = str.replace( '&#246;', 'ö' )
    
    str = str.replace( '&#220;', 'Ü' )
    str = str.replace( '&#252;', 'ü' )
    
    str = str.replace( '&#223;', 'ß' )
    
    str = str.replace( '&#178;', '²' )
    str = str.replace( '&#179;', '³' )
    
    str = str.replace( '&#216;', 'Ø' )
    
    return str

def __RequestRSSFeed():
    url = 'http://letsplayimpot.de/media_rss.php'
    
    request = urllib2.Request( url )
    request.add_header( 'User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
    
    response = urllib2.urlopen( request )
    data = response.read()
    response.close()
    
    rssXML = minidom.parseString( data )
    
    return rssXML.getElementsByTagName( 'item' )

def __GetNodeByName( nodeList, name ):
    for node in nodeList:
        if( node.nodeName.lower() == name.lower() ):
            return node
    
    return None

def __GetNodeData( node ):
    rc = []
    
    for child in node.childNodes:
        if( child.nodeType == child.TEXT_NODE ):
            rc.append( child.data )
    
    return ''.join( rc )

def __GetNodeAttribute( node, attrName ):
    for key in node.attributes.keys():
        if( key.lower() == attrName.lower() ):
            return node.attributes[key].value
    
    return ''

def __AddDirectory( name, url, mode, iconImage, referer = '' ):
    u = sys.argv[0] + "?url=" + urllib.quote_plus( url ) + "&mode=" + urllib.quote_plus( mode ) + "&name=" + urllib.quote_plus( name )+ "&referer=" + urllib.quote_plus( referer )
    
    liz = xbmcgui.ListItem( name, iconImage = "DefaultFolder.png", thumbnailImage = iconImage )
    liz.setInfo( type = "Video", infoLabels = { "Title": name } )
    
    return xbmcplugin.addDirectoryItem( handle = int( sys.argv[1] ), url = u, listitem = liz, isFolder = True )

def __AddVideoEmbeddedLink( name, url, iconImage, studio = '', date = '', category = '', length = '' ):
    u = sys.argv[0] + "?url=" + urllib.quote_plus( url ) + "&mode=PLAY_VIDEO&name=" + urllib.quote_plus( name )
    
    liz = xbmcgui.ListItem( name, iconImage = "DefaultVideo.png", thumbnailImage = iconImage )
    liz.setInfo( type = "Video", infoLabels = { "Title": name, "Date": date, "Duration": length, "Genre": category, "Studio": studio } )
    
    return xbmcplugin.addDirectoryItem( handle = int( sys.argv[1] ), url = u, listitem = liz )

def __AddVideoLink( name, url, iconImage ):
    liz = xbmcgui.ListItem( name, iconImage = "DefaultVideo.png", thumbnailImage = iconImage )
    liz.setInfo( type = "Video", infoLabels = { "Title": name } )

    return xbmcplugin.addDirectoryItem( handle = int( sys.argv[1] ), url = url, listitem = liz )
    
def GetParameters():
    param = []
    paramstring=sys.argv[2]
    
    if( len( paramstring ) >= 2 ):
        params = sys.argv[2]
        cleanedparams = params.replace( '?', '' )
        
        if( params[len( params ) - 1] == '/' ):
            params = params[0:len( params ) - 2]
        
        pairsofparams=cleanedparams.split( '&' )
        param={}
        
        for i in range( len( pairsofparams ) ):
            splitparams = {}
            splitparams = pairsofparams[i].split( '=' )
            
            if( ( len( splitparams ) ) == 2 ):
                param[splitparams[0]] = splitparams[1]

    return param

params = GetParameters()
url = None
name = None
mode = None
referer = None

try:
    url = urllib.unquote_plus( params["url"] )
except:
    pass

try:
    name = urllib.unquote_plus( params["name"] )
except:
    pass

try:
    mode = urllib.unquote_plus( params["mode"] )
except:
    pass

try:
    referer = urllib.unquote_plus( params["referer"] )
except:
    pass

if( mode == None ):
    ShowStartOverview()

elif( mode == 'SHOW_NEWEST' ):
    ShowNewest( url )

elif( mode == 'SHOW_MOST_VIEWED' ):
    ShowMostViewed( url )

elif( mode == 'SHOW_LONGEST' ):
    ShowLongest( url )
    
elif( mode == 'SHOW_USERS' ):
    ShowUsers( url )
    
elif( mode == 'SHOW_USER_GAMES' ):
    ShowUserGames( url )

elif( mode == 'SHOW_GAMES' ):
    ShowGames( url )

elif( mode == 'SHOW_CATEGORIES' ):
    ShowCategories()
    
elif( mode == 'SHOW_GAME' ):
    ShowGame( url, referer )

elif( mode == 'PLAY_VIDEO' ):
    PlayVideo( url )

elif( mode == 'SHOW_TUTORIALS' ):
    ShowTutorials()

elif( mode == 'SEARCH_GAME' ):
    SearchGames()

xbmcplugin.endOfDirectory( int( sys.argv[1] ) )
