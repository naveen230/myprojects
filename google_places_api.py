#!/usr/bin/env python3

import requests
import json
import csv

api_key = '' 
#url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
query = input('Search query: ')
r = requests.get(url + 'query=' + query + '&key=' + api_key)
x = r.json()
y = x['results']

for i in range(len(y)):
    placeid = y[i]['place_id']
    name = y[i]['name']
    addr = y[i]['formatted_address'] 
    rating = y[i]['rating']
    url02 = "https://maps.googleapis.com/maps/api/place/details/json?"
    r02 = requests.get(url02 + '&key=' + api_key + '&place_id=' + placeid + '&fields=formatted_phone_number,website')
    x02 = r02.json() 
    y02 = x02['result']
    phone = y02['formatted_phone_number'] 
    website = y02['website']
    fields = [name, addr, website, phone, rating]
    with open('addiction-center-toronto-02.csv', 'a') as f:
        towrite = csv.writer(f)
        towrite.writerow(fields)
