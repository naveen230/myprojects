#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import csv
import pickle

max_page = 2429 #total number of pages,change the value if needed.
i = 1

for i in range(1, max_page):
    # the items in the data set will be extracted in ascending order
    #change to home URL https://www.data.gov/ if needed
    page = requests.get("https://catalog.data.gov/dataset?q=&sort=score+desc%2C+name+asc&page=" + str(i))
    soup = BeautifulSoup(page.content, 'html.parser')
    for dv in soup.find_all("div", class_="dataset-content"):
        heading = dv.find("h3", class_="dataset-heading")
        if heading is not None:
            heading = dv.find("h3", class_="dataset-heading").text.strip()
        orgtype = dv.find("span", class_="organization-type")
        if orgtype is not None:
            orgtype = dv.find("span", class_="organization-type").text.strip()
        dataorg = dv.find("p", class_="dataset-organization")
        if dataorg is not None:
            dataorg = dv.find("p", class_="dataset-organization").text.strip()
        desc = dv.find("div", class_="notes")
        if desc is not None:
            desc = dv.find("div", class_="notes").text.strip()
        for link in dv("a", "label", href=True):
            url = link['href']
            fields = [heading, orgtype, dataorg, desc, url]
            with open('complete.csv', 'a') as f:
                towrite = csv.writer(f)
                towrite.writerow(fields)
                
i = i + 1
if i > max_page:
    print("The complete dataset is now downloaded!")
