#!/usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json
import datetime

def get_jsonparsed_data(url):
    """Receive the content of ``url``, parse it as JSON and return the
       object.
	   data = response.read().decode('utf-8')
	"""

    response = urlopen(url)
    data = response.read().decode('utf-8')
    return json.loads(data)
	
if __name__ == "__main__":
    import sys
    print ''
    print '       *****************'	
    print '       *               *'
    print '       *  LEADERBOARD  *'
    print '       *               *'
    print '       *****************'	
    print ''
    print "start time: " + datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    players = [{"count":5,"score":5,"player":"Bob"},{"count":5,"score":4,"player":"John"},{"count":5,"score":3,"player":"Jessie"},{"count":4,"score":2,"player":"Mary"},{"count":5,"score":2,"player":"Jeff"},{"count":5,"score":1,"player":"Hugh"},{"count":5,"score":1,"player":"Andy"}]
    #players = json.loads(get_jsonparsed_data(sys.argv[1]))
    i=1
    print ''
    print '-------------------------------'	
    print ' N. Player     Score  Questions'	
    print '-------------------------------'	
    for player in players:
       if (i == 1):
          print '\u001b[0;32m%2d  %-10s %3d      %3d\u001b[0m'.decode('unicode_escape') % (i,player["player"],player["score"],player["count"])
       else:
          print '%2d  %-10s %3d      %3d' % (i,player["player"],player["score"],player["count"])
		  #print i,' player:', player["player"], ' score:', player["score"], ' countquestions:', player["count"]
       i=i + 1
    print ''
    #print "end time: " + datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
	
