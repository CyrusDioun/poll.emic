import os
import sys
import simplejson as json
from pprint import pprint as pp

LOG_PATH = "log/"

def load_snowball():

    SNOWBALL_PATH = "snowball-47545000-3.json"
    if len(sys.argv) > 1:
        SNOWBALL_PATH = sys.argv[1]

    if os.path.isfile("%s" % (SNOWBALL_PATH)):
        snowball_file = open("%s" % (SNOWBALL_PATH),'r')
        snowball = json.loads(snowball_file.read())
        return snowball
    else:
        print "error"


if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

snowball = load_snowball()

for u_id, metadata in snowball.items():
    #print "crawling: ", line
    pp(metadata)
    if metadata.has_key('screen_name'):
        screen_name = metadata['screen_name']
        cmd = "twitter-log " + screen_name + " > " + LOG_PATH + screen_name + ".txt"
        print cmd
        os.system(cmd)
    else:
        print 'No screen name for %s'%(u_id)


 
