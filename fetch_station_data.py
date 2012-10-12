#!/usr/bin/python

import httplib
from urlparse import urlparse
from array import *
import xml.etree.ElementTree as ET
import json

def get(url):
    "does a get request and returns the response. Exits if error"
    o = urlparse(url)
    conn = httplib.HTTPConnection(o.hostname)
    conn.request("GET", url)
    resp = conn.getresponse()
    if resp.status != 200:
        print "error!: get failed on "+url+" - "+str(resp.status)
        return 0
    else:
        return resp.read()


station_numbers = array('i', [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 112, 113, 114, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 127, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 156, 157, 158, 159, 160, 161, 163, 164, 165, 166, 167, 168, 169, 170, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 207, 208, 209, 210, 211, 212, 213, 214, 215, 217, 218, 219, 220, 221, 223, 224, 225, 226, 227, 228, 229, 230, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310])

station_info = ""

#fetch the existing data file
f = open('villo-data.jsonish','a')

# retrieve new data
for i in station_numbers:
    res = get("http://www.villo.be/service/stationdetails/bruxelles/"+str(i))
    root = ET.fromstring(res)
    available = root.find('available').text
    free = root.find('free').text
    total = root.find('total').text
    ticket = root.find('ticket').text
    is_open = root.find('open').text
    updated = root.find('updated').text
    connected = root.find('connected').text

    station_info += '{"updated": '+ updated + ', "stationid": '+ str(i) + ', "available": ' + available + ', "free": ' + free + ', "total": ' + total + ', "ticket": ' + ticket + ', "open": ' + is_open + ', "connected": ' + connected + "}\n"

    if i == 20:
        break

f.write(station_info)
f.close()

