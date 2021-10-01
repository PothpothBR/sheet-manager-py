# Google Sheets open API
# Reference: https://docs.gspread.org/en/latest/user-guide.html
import gspread
from io_format import *
from students import Students


# login API on drive service and get the table for edit
# how can not use with, insert in try statement
prif('loading dependencies')
try:
    gs = gspread.service_account(filename='credentials.json')
    sheet = gs.open_by_key('1tIMTlr5wTVvporWXutqQm2EOaSyLcK9DEB9toGzglCU')
    worksheet = sheet.sheet1
except:
    exif('fail connection attempt')


# get all data for processing and then format
prif('downloading data')
try:
    res = worksheet.get('a4:f27')
    res.insert(0, worksheet.get('a2'))
except:
    exif('fail data download attempt')

# creating the student class and building their values
prif('generate results')
school = Students(res)

# check for possible unintended use
if inpf('data will be modified, continue? [any key/n]', 'warn').lower() == 'n':
    # don't update table
    prif('data not uploaded', 'warn')
else:
    # insert the results in table
    prif('uploading data')
    try:
        worksheet.update('g4:h27', list(zip(school.situations, school.NAF)))
    except:
        exif('fail data upload attempt')

prif('shutting down')
