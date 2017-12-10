import urllib3
import facebook
import requests
import collections
import token_info
import json
import sqlite3
from datetime import datetime 
import itertools


#Manali Desai

token = token_info.token
graph = facebook.GraphAPI(access_token=token) 


CACHE_FNAME = "206_bean_events_cache.json"
# Put the rest of your caching setup here:

try:
	cache = open(CACHE_FNAME, 'r')
	cache_content = cache.read()
	cache.close()
	cache_dict = json.loads(cache_content)
except:
	cache_dict = {}


#function that gets facebook event data based on search term given
def get_events(search_term):

	if search_term in cache_dict:
		print("from cache")
		return cache_dict[search_term]
	else:
		print("fetching data")
		data = graph.request('/v2.2/search?type=event&q=' + search_term + '&since=2016-01-01&limit=1000')

		cache_dict[search_term] = data
		dump_json_cache = json.dumps(cache_dict)
		fw = open(CACHE_FNAME, 'w')  
		fw.write(dump_json_cache)
		fw.close()
		return data


#getting facebook bean events
bean_events = get_events("Bean")

conn = sqlite3.connect('bean_events_DB.sqlite')
cur = conn.cursor()


#creating table of all the events
cur.execute('DROP TABLE IF EXISTS Events')
cur.execute('CREATE TABLE Events (event_id INTEGER, event_name TEXT, start_time TEXT, city TEXT, attending INTEGER, interested INTEGER )')


#goes through each event in the event data
for event in bean_events['data']:

	event_id = event['id']

	#gets extra info on each event from facebook 
	event_data = graph.get_object(id= event_id,
                         fields='attending_count, maybe_count')

	#gets city data for event if it is available. else puts in 0 
	location = 0
	if event.get('place',0):
		a = event.get('place',0)
		if a.get('location',0):
			b = a.get('location',0)
			if b.get('city',0):
				location = b.get('city',0)


	#places data into database
	cur.execute('INSERT INTO Events(event_id, event_name, start_time, city, attending, interested) VALUES (?,?,?,?,?,?)' ,
		( event_id , event['name'] , event['start_time'] , location , event_data['attending_count'] , event_data['maybe_count']  ))


conn.commit()

cur.close()
conn.close()







