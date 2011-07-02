"""
fuelwatch - A simple Python 3 module that parses the FuelWatch RSS feed provided by the Western Australian Government,
which is located at <http://www.fuelwatch.wa.gov.au>.

    Copyright (C) 2011  Adam Gibson

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import httplib2
import xml.etree.ElementTree as etree
from urllib.parse import urlencode
import datetime as dt

__author__ = 'Adam Gibson'

product = {
    1: "Unleaded Petrol",
    2: "Premium Unleaded",
    4: "Diesel",
    5: "LPG",
    6: "98 RON",
    7: "B20 Diesel"
}

region = {
    1: "Boulder",
    2: "Broome",
    3: "Busselton (Townsite)",
    4: "Carnarvon",
    5: "Collie",
    6: "Dampier",
    7: "Esperance",
    8: "Kalgoorlie",
    9: "Karratha",
    10: "Kununurra",
    11: "Narrogin",
    12: "Northam",
    13: "Port Hedland",
    14: "South Hedland",
    15: "Albany",
    16: "Bunbury",
    17: "Geraldton",
    18: "Mandurah",
    19: "Capel",
    20: "Dardanup",
    21: "Greenough",
    22: "Harvay",
    23: "Murray",
    24: "Waroona",
    25: "Metro : North of River",
    26: "Metro : South of River",
    27: "Metro : East/Hills",
    28: "Augusta / Margaret River",
    29: "Busselton (Shire)",
    30: "Bridgetown / Greenbushes",
    31: "Donnybrook / Balingup",
    32: "Manjimup",
    33: "Cataby",
    34: "Collgardie",
    35: "Cunderdin",
    36: "Dalwallinu",
    37: "Denmark",
    38: "Derby",
    39: "Dongara",
    40: "Exmouth",
    41: "Fitzroy Crossing",
    42: "Jurien",
    43: "Kambalda",
    44: "Kellerberrin",
    45: "Kojonup",
    46: "Meekatharra",
    47: "Moora",
    48: "Mt Barker",
    49: "Newman",
    50: "Norseman",
    51: "Ravensthorpe",
    53: "Tammin",
    54: "Williams",
    55: "Wubin",
    56: "York"
}

brand = {
    2: "Ampol",
    3: "Better Choice",
    4: "BOC",
    5: "BP",
    6: "Caltex",
    7: "Gull",
    8: "Kleenheat",
    9: "Kwikfuel",
    10: "Liberty",
    13: "Peak",
    14: "Shell",
    15: "Independent",
    16: "Wesco",
    19: "Caltex Woolworths",
    20: "Coles Express",
    21: "Black & White",
    23: "United",
    24: "Eagle"
}

suburbs = [
        'Albany',
        'Alexander Heights',
        'Alfred Cove',
        'Applecross',
        'Armadale',
        'Ascot',
        'Attadale',
        'Augusta',
        'Australind',
        'Balcatta',
        'Baldivis',
        'Balga',
        'Balingup',
        'Ballajura',
        'Barragup',
        'Baskerville',
        'Bassendean',
        'Bayswater',
        'Beckenham',
        'Bedfordale',
        'Beechboro',
        'Beldon',
        'Bellevue',
        'Belmont',
        'Benger',
        'Bentley',
        'Bertram',
        'Bibra Lake',
        'Bicton',
        'Binningup',
        'Boulder',
        'Bouvard',
        'Boyanup',
        'Brentwood',
        'Bridgetown',
        'Broome',
        'Brunswick Junction',
        'Bull Creek',
        'Bullsbrook',
        'Bunbury',
        'Burswood',
        'Busselton',
        'Byford',
        'Canning Vale',
        'Cannington',
        'Capel',
        'Carbunup River',
        'Carine',
        'Carlisle',
        'Carnarvon',
        'Cataby',
        'Caversham',
        'Chidlow',
        'Claremont',
        'Clarkson',
        'Cloverdale',
        'Collie',
        'Como',
        'Coolgardie',
        'Coolup',
        'Cottesloe',
        'Cowaramup',
        'Cunderdin',
        'Currambine',
        'Dalwallinu',
        'Dampier',
        'Dardanup',
        'Dawesville',
        'Denmark',
        'Derby',
        'Dianella',
        'Dongara',
        'Donnybrook',
        'Doubleview',
        'Duncraig',
        'Dunsborough',
        'Dwellingup',
        'East Fremantle',
        'East Perth',
        'East Victoria Park',
        'Eaton',
        'Edgewater',
        'Ellenbrook',
        'Erskine',
        'Esperance',
        'Exmouth',
        'Falcon',
        'Fitzroy Crossing',
        'Floreat',
        'Forrestdale',
        'Forrestfield',
        'Fremantle',
        'Gelorup',
        'Geraldton',
        'Gidgegannup',
        'Girrawheen',
        'Glen Forrest',
        'Glendalough',
        'Glenfield',
        'Gnangara',
        'Golden Bay',
        'Gosnells',
        'Gracetown',
        'Greenbushes',
        'Greenough',
        'Greenwood',
        'Guildford',
        'Gwelup',
        'Halls Head',
        'Hamilton Hill',
        'Harvey',
        'Herne Hill',
        'High Wycombe',
        'Highgate',
        'Hillarys',
        'Huntingdale',
        'Innaloo',
        'Jandakot',
        'Jolimont',
        'Joondalup',
        'Jurien Bay',
        'Kalamunda',
        'Kalgoorlie',
        'Kambalda',
        'Karawara',
        'Kardinya',
        'Karragullen',
        'Karratha',
        'Karridale',
        'Karrinyup',
        'Kellerberrin',
        'Kelmscott',
        'Kewdale',
        'Kiara',
        'Kingsley',
        'Kirup',
        'Kojonup',
        'Koondoola',
        'Kununurra',
        'Kwinana',
        'Lakelands',
        'Langford',
        'Leda',
        'Leederville',
        'Leeming',
        'Lesmurdie',
        'Lynwood',
        'Maddington',
        'Madeley',
        'Malaga',
        'Mandurah',
        'Manjimup',
        'Manning',
        'Manypeaks',
        'Margaret River',
        'Meadow Springs',
        'Meekatharra',
        'Merriwa',
        'Middle Swan',
        'Midvale',
        'Mindarie',
        'Mirrabooka',
        'Moonyoonooka',
        'Moora',
        'Morley',
        'Mosman Park',
        'Mount Barker',
        'Mt Hawthorn',
        'Mt Helena',
        'Mt Lawley',
        'Mt Pleasant',
        'Mullaloo',
        'Mundaring',
        'Mundijong',
        'Munster',
        'Murdoch',
        'Myalup',
        'Myaree',
        'Narrogin',
        'Naval Base',
        'Nedlands',
        'Neerabup',
        'Newman',
        'Nollamara',
        'Noranda',
        'Norseman',
        'North Dandalup',
        'North Fremantle',
        'North Perth',
        'Northam',
        'Northbridge',
        'Northcliffe',
        'Nowergup',
        "O'Conner",
        'Ocean Reef',
        'Osborne Park',
        'Padbury',
        'Palmyra',
        'Parmelia',
        'Pearsall',
        'Pemberton',
        'Perth',
        'Picton',
        'Pinjarra',
        'Port Hedland',
        'Port Kennedy',
        'Preston Beach',
        'Quinns Rock',
        'Ravensthorpe',
        'Redcliffe',
        'Redmond',
        'Ridgewood',
        'Riverton',
        'Rivervale',
        'Rockingham',
        'Roleystone',
        'Rosa Brook',
        'Rottnest Island',
        'Sawyers Valley',
        'Scarborough',
        'Secret Harbour',
        'Serpentine',
        'Singleton',
        'Sorrento',
        'South Fremantle',
        'South Hedland',
        'South Lake',
        'South Perth',
        'South Yunderup',
        'Southern River',
        'Spearwood',
        'Stratham Downs',
        'Stratton',
        'Subiaco',
        'Success',
        'Swan View',
        'Swanbourne',
        'Tammin',
        'The Lakes',
        'Thornlie',
        'Tuart Hill',
        'Upper Swan',
        'Vasse',
        'Victoria Park',
        'Waikiki',
        'Walpole',
        'Wangara',
        'Wanneroo',
        'Warnbro',
        'Waroona',
        'Warwick',
        'Waterloo',
        'Wattle Grove',
        'Wedgefield',
        'Wellstead',
        'Welshpool',
        'Wembley',
        'West Perth',
        'West Swan',
        'Westfield',
        'Westminster',
        'Willetton',
        'Williams',
        'Witchcliffe',
        'Woodvale',
        'Wooroloo',
        'Wubin',
        'Yanchep',
        'Yokine',
        'York',
        'Young Siding',
        'Yunderup'
]

base_url_v1 = "http://www.fuelwatch.wa.gov.au/fuelWatchRSS.cfm?"
base_url_v2 = "http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?"

def generate_options(product, location, location_type='suburb', day='today', surrounding=False):
    #TODO
    pass

def generate_url(optionsdict, api=2):
    """ Generate a URL to access FuelWatch via API version 1 or 2 (default), based on the options dict.
    """
    options = urlencode(optionsdict)
    if api == 1:
        url = base_url_v1 + options
    elif api == 2:
        url = base_url_v2 + options
    else:
        url = None
    return url

def getdata(url):
    """ Return a us-ascii text string from a given URL.
    """
    h = httplib2.Http('.cache')
    response, content = h.request(url)
    #TODO - Catch Exceptions (i.e. if no internet connection).
    #decode byte-array to string, us-ascii selected as mime type text/xml
    datastring = content.decode("us-ascii")
    return datastring

def parse(datastring):
    """ Parse XML string and return a list that contains a dict of attributes for each servo.
    """
    rss = etree.fromstring(datastring)
    results = []
    for channel in rss:
        print("+", channel) #for debugging
        for tag in channel:
            print("++", tag) #for debugging
            if tag.tag == "item":
                item = {}
                for subtag in tag:
                    k, v = preprocess(subtag.tag, subtag.text) #preprocess tag and value before adding to item.
                    #item[subtag.tag] = subtag.text
                    item[k] = v
                    #print(subtag.tag, ": ", subtag.text) #for debugging
                    print(k, ": ", v)
                item_p = postprocess(item)
                results.append(item_p)
    return results


def preprocess(tag, value):
    """ A general inline function to pre-process tag and value before it is added to a dict.
    """
    if tag == "price":
        #convert price to float.
        output_tag = tag
        output_value = float(value)
    elif tag == "date":
        #convert APIv2 output to a datetime module date.
        output_tag = tag
        output_value = dt.date(int(value[0:4]),int(value[5:7]),int(value[8:10]))
    elif tag == "datePosted":
        #convert APIv1 output to a datetime module date, save tag as 'date'.
        output_tag = "date"
        output_value = dt.date(int(value[0:4]),int(value[5:7]),int(value[8:10]))
    else:
        output_tag = tag
        output_value = value
    return output_tag, output_value

def postprocess(dict):
    """ A general function to post-process a dict before it is added to the results list.
    """
    # Condition added to split
    if "Address:" not in dict["description"]:
        dict['price'] = float(dict["description"].split(":")[0])
        dict['trading-name'] = dict["description"].split(":")[1].split("-")[0].strip()
        addr_loc = dict["description"].split(":")[1].split("-")[1]
        for s in suburbs:
            if addr_loc.endswith(s.upper()):
                #TODO (BUG) - 'address' and 'location' keys are not populated when suburb is 'O'Conner' and
                #'description' is "140.9: Caltex Woolworths O'Connor - Cnr Stock Rd & Forsythe St O'CONNOR"
                dict['address'] = addr_loc[0:len(addr_loc)-len(s)].strip()
                dict['location'] = s.upper()
                print("break")
                break
        #debug
        #print('$'*40)
        #for i in ['price','trading-name','location','address']:
        #    print(i, ": ", dict[i])
    return dict

