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
