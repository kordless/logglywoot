import httplib2
import simplejson
import sys
import time
import subprocess

# loggly info 
username = 'kordless'
password = 'password'
subdomain = 'geekceo'

# connection to query
h = httplib2.Http("")
h.add_credentials(username, password)

# connection to arduino server
j = httplib2.Http("")

while True:
  # facet check for signups 2 minutes ago to 1 minute ago
  resp, content = h.request("http://%s.loggly.com/api/facets/date/?q='/thankyou/'&from=NOW-2MINUTE&until=NOW-1MINUTE&buckets=1" % subdomain, "GET", headers={'content-type':'text/plain'} )
  foo = simplejson.loads(content)
  free = foo['data'].items()[0][1]

  # facet check for paid 2 minutes ago to 1 minute ago
  resp, content = h.request("http://%s.loggly.com/api/facets/date/?q='/register/'&from=NOW-2MINUTE&until=NOW-1MINUTE&buckets=1" % subdomain, "GET", headers={'content-type':'text/plain'} )
  foo = simplejson.loads(content)
  paid = foo['data'].items()[0][1]

  # ping the arduino server to turn on the lights, and play a wave (OSX only)
  if free > 0 or paid > 0:
    resp, content = h.request("http://localhost:9090/?action=on", "GET", headers={'content-type':'text/plain'} )
    if paid > 0:
       subprocess.Popen(['/usr/bin/afplay', "/Users/kord/Dropbox/Code/logglywoot/paid.mp3"])
    else:
       subprocess.Popen(['/usr/bin/afplay', "/Users/kord/Dropbox/Code/logglywoot/bell.mp3"])

  else:
    resp, content = h.request("http://localhost:9090/?action=off", "GET", headers={'content-type':'text/plain'} )

  time.sleep(60)
