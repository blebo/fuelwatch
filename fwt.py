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
    along with fuelwatch.  If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = 'Adam Gibson'

import fuelwatch as fw
data = fw.getdata("http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=O'Connor")
results = fw.parse(data)

print('='*40)

data2 = fw.getdata("http://www.fuelwatch.wa.gov.au/fuelWatchRSS.cfm?Product=1&Suburb=O'Connor")
results2 = fw.parse(data2)

print('='*40)

opts3 = {'Product': 1, 'Suburb': "O'Connor"}
url3 = fw.generate_url(opts3)
data3 = fw.getdata(url3)
results3 = fw.parse(data3)


print('='*40)

opts4 = {'Product': 1, 'Suburb': "O'Connor"}
url4 = fw.generate_url(opts4, 1)
data4 = fw.getdata(url4)
results4 = fw.parse(data4)


print('='*40)

print("url3: ", url3)
print("url4: ", url4)

print("api2: ", results == results3)
print("api1: ", results2 == results4)

print('+'*40)
print(results)
print('+'*40)
print(results2)
print('+'*40)
print(results3)
print('+'*40)
print(results4)