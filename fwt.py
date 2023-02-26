"""
    This file is part of fuelwatch.

    fuelwatch is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    fuelwatch is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with fuelwatch.  If not, see <https://www.gnu.org/licenses/>.
"""
__author__ = 'Adam Gibson'

import fuelwatch as fw
data = fw.getdata("https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=O'Connor")
results = fw.parse(data)

print('='*40)

opts3 = {'Product': 1, 'Suburb': "O'Connor"}
url3 = fw.generate_url(opts3)
data3 = fw.getdata(url3)
results3 = fw.parse(data3)


print('='*40)

print("url3: ", url3)

print("api2: ", results == results3)

print('+'*40)
print(results)
print('+'*40)
print(results3)

print('='*40)
print('='*40)
print('='*40)

# Documentation Examples:
example_urls = [
    "https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale",
    "https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale&Surrounding=no",
    "https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Suburb=Clarkson",
    "https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Suburb=Mandurah",
    "https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=4&Suburb=Mindarie&Day=tomorrow", # after 2.30pm, tomorrows prices returned.
    "https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=5&Region=28",
    "https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=6&Region=25&Day=tomorrow",  # after 2.30pm, tomorrows prices returned.
    "https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Northbridge&Brand=23",
    "https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Tuart%20Hill&Surrounding=no&Brand=3"
]

i=0
for u in example_urls:
    i+=1
    print("Example", i)
    print(fw.parse(fw.getdata(u)))
    print('=' * 40)


example_opts = [
    {'Product': 1, 'Suburb': "O'Connor"},
    {'Product': 1, 'Suburb': "Bedford"},
    {'Product': 11, 'Suburb': "Perth"},
    {'Product': 2, 'Suburb': "Embleton"},
]

i=0
for o in example_opts:
    i+=1
    print("Example opts ", i)
    print(fw.parse(fw.getdata(fw.generate_url(o))))
    print('=' * 40)

