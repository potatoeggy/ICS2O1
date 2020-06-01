# Name: Daniel Chen
# Date: 6 March 2019
# Description: OV9 - Reads name, street, city, province, and postal code individually and outputs them simultaneously

name = input('Name: ')
street = input('Street: ')
city = input('City: ')
province = input('Province: ')
postal_code = input('Postal Code: ')

print(name + ', lives on ' + street + ', in ' + city + ', ' + province + ', with a postal code of ' + postal_code + '.')