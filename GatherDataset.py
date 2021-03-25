#!/usr/bin/env python
# coding: utf-8

# In[128]:


from urllib.parse import urlparse
import re
import urllib
import urllib.request  #changing import urllib2 to import urllib.request
#import minidom
import csv
import unicodedata
import requests
import chardet
import charade
import socket
import pandas as pd
import numpy as np
import json
import random
import socket
import struct
from geopy.geocoders import Nominatim
import os
#from global_land_mask import globe
from htmldate import find_date
import xlwt
from xlwt import Workbook
import tld
from tld import get_tld
from time import sleep


# In[129]:


def main():
    # excel
    wb = Workbook()
    sheet1 = wb.add_sheet("Sheet 1")
    wb = Add_Column_Names(wb, sheet1)
    
    # txt file
    file1 = open('websites.txt', 'r')
    count = 0
    num_columns = 16
    

    for line in file1.readlines():
        urlfeatures = []
        count += 1
        # Save url
        url_input = str(line.strip())
        # extract features of each url
        urlfeatures = Extract_Features(url_input, urlfeatures)
        # add to excel
        if (len(urlfeatures) == 0):
            urlfeatures.append(url_input)
            Populate_Row(wb, sheet1, count, num_columns, urlfeatures)
            #sleep(2)
        else:
            Populate_Row(wb, sheet1, count, num_columns, urlfeatures)
            #sleep(2)

        print(count)
        
    file1.close()
    


def Extract_Features(url_input, urlfeatures):
    #tokens_words = re.split('\W+', url)  # Extract bag of words stings delimited by (.,/,?,,=,-,_)
    isComplete = False
    
    while (isComplete == False):
    
        obj = urlparse(url_input)
        host = obj.netloc

        try:
            r = requests.get(url_input, verify=False)
        except:          
            return urlfeatures
            break

        urlfeatures.append(url_input)
        urlfeatures.append(str(len(url_input)))
        urlfeatures.append(Get_TLD(url_input))
        urlfeatures.append(Contains_Special_Characters(url_input))     
        urlfeatures.append(r.encoding)
        urlfeatures.append(Get_Server(url_input, r))
        urlfeatures.append(Get_Content_Length(url_input, r)) #Length of HTML
        urlfeatures.append(Get_Country(host))
        urlfeatures.append(Get_State(host, r))
        urlfeatures.append(Get_Date_Created(url_input))
        urlfeatures.append(Get_Last_Mod_Date(url_input, r))
        urlfeatures.append(Get_Zip_Code(host))
        urlfeatures.append(Get_City(host))
        urlfeatures.append(Get_Content_Encoding(url_input, r))
        urlfeatures.append(Get_HSTS(url_input, r))
        urlfeatures.append(Get_Content_Type(url_input,r))
        isComplete = True
        
        return urlfeatures


def getting_ip(ip):
    """This function calls the api and return the response"""
    url =f"https://freegeoip.app/json/{ip}"       # getting records from getting ip address
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    response = requests.request("GET", url, headers=headers)
    respond = json.loads(response.text)
    return respond

def Get_TLD(url_input):
    try:
        tld = get_tld(url_input)
        return tld
    except:
        return None
    
def Get_Headers(url_input):
    try:
        r = requests.get(url_input)
        return r.headers  
    except:
        return None
    
def Get_IP_Address(host):
    ip = socket.gethostbyname(host)
    return ip

def Get_Country(host):
    try:
        ip = Get_IP_Address(host)
        country = getting_ip(ip)['country_name']
        return country
    except:
        return None
    
def Get_State(host, r):
    try:
        latlong = Get_Long_Lat(host, r)
        geolocator = Nominatim(user_agent="app")
        location = geolocator.reverse(latlong)
        address = location.raw['address']
        state = str(location.raw['address']['state'])
        return state
    except:
        return None

def Get_Zip_Code(host):
    try:
        ip = Get_IP_Address(host)
        zipcode = getting_ip(ip)['zip_code']
        return zipcode
    except:
        return None
    
def Get_City(host):
    try:
        ip = Get_IP_Address(host)
        city = getting_ip(ip)['city']
        return city
    except:
        return None
    
def Get_Content_Length(url_input, r):
    try:
        Get_Headers(url_input)
        content_length = str(r.headers["content-length"])
        return content_length
    except:
        try:
            r = requests.get(url_input)
            r.text
            content_length = str(len(r.text))
            return content_length
        except:
            return None
        

def Get_Server(url_input, r):
    try:
        Get_Headers(url_input)
        if (str(r.headers["server"]) != None):
            server = str(r.headers["server"])
            return server
        if (str(r.headers["Server"]) != None):
            server = str(r.headers["Server"])
            return server
    except:
        return None

def Contains_Special_Characters(url_input):
    try:
        count = 0
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        special_chars = re.sub('[\w]+' , '', url_input)
        count = str(len(special_chars))
        return count
    except:
        return None

def Get_Last_Mod_Date(url_input, r):
    Get_Headers(url_input)
    try:
        date = str(r.headers['Last-Modified'])
        return date
    except:
        return None
    
def Get_Date_Created(url_input):
    try:
        date = find_date(url_input)
        return date
    except:
        return None
    
def Get_Content_Encoding(url_input, r):
    Get_Headers(url_input)
    try:
        content_encoding = str(r.headers['content-encoding'])
        return content_encoding
    except:
        return None
    
def Get_HSTS(url_input, r):
    try:                            
        Get_Headers(url_input)
        hsts = str(r.headers['strict-transport-security'])
        return hsts
    except:
        return None
    
def Get_Content_Type(url_input, r):
    Get_Headers(url_input)
    try:
        content_type = str(r.headers['content-type'])
        return content_type
    except:
        return None
    
def Get_Long_Lat(host, r):
    try:
        latlong = ""
        ip = Get_IP_Address(host)
        latitude = str(getting_ip(ip)['latitude'])
        longitude = str(getting_ip(ip)['longitude'])
        latlong = latitude + "," + longitude
        return latlong
    except:
        return None


# In[133]:


def Add_Column_Names(wb, sheet1):
    column_names = ['URL', 'URL_LENGTH', 'TLD', 'NUMBER_SPECIAL_CHARACTERS', 'CHARTSET','SERVER', 'CONETNT_LENGTH', 'WHOIS_COUNTRY',
                  'WHOIS_STATEPRO', 'WHOIS_REGDATE', 'WHOIS_UPDATED_DATE', 'WHOIS_ZIPCODE', 'WHOIS_CITY', 'CONTENT_ENCODING',
                  'HSTS', 'CONTENT_TYPE']
    column_count = len(column_names) # number of features
    i = 0
    while (i < column_count):
        sheet1.write(0,i, column_names[i])
        i += 1
    
    wb.save('websitedata.xls')
    return wb


# In[134]:


def Populate_Row(wb, sheet1, count, num_columns, urlfeatures):
    i = 0
    if (len(urlfeatures) == 1):
        sheet1.write(count, i, urlfeatures[i])
        wb.save('websitedata.xls')
        return wb
    else:
        while (i < num_columns):
            sheet1.write(count, i, urlfeatures[i])
            i += 1

        wb.save('websitedata.xls')
        return wb
       


# In[135]:


main()


# 4:14

# In[ ]:




