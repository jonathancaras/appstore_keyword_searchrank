# -*- coding: utf-8 -*-
#appstore ranking search
import urllib,simplejson
import config

def search(keyword):
	print keyword.decode("utf8")
	json = urllib.urlopen(("http://itunes.apple.com/search?term="+urllib.quote(keyword)+"&country=jp&entity=software")).read()
	results = simplejson.loads(json)["results"]
	for i,result in enumerate(results):
		if result["artistName"] == config.artist_name:
			print "\t",i+1,result["trackCensoredName"]

for keyword in config.keywords:
	search(keyword)
print "Press any key."
import sys;sys.stdin.readline()
