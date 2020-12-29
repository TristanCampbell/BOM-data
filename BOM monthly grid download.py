# Code to download monthly grids of weather conditions created by the Bureau of Meteorology (Australia)
# Gridded products cover Australia with an 0.05 degree resolution (~5 x 5 km grid)
# Browse products graphically at http://www.bom.gov.au/climate/maps/#tabs=Maps
# Dataset description from BOM with and cross-validation error analysis: http://doi.org/10.22499/2.5804.003
# Recommend downloading no more than 1 year at a time

# For comments, please contact tristan.campbell@curtin.edu.au

import csv
import webbrowser
import datetime
import calendar
import datedelta
import shutil
import os
import time

# Get date range from user
StartDate = input('Enter start month (YYYY/MM): ')
StartDateObj = datetime.datetime.strptime(StartDate, '%Y/%m')
EndDate = input('Enter end month (YYYY/MM): ')
EndDateObj = datetime.datetime.strptime(EndDate, '%Y/%m')
EndDateObj = datetime.datetime.strptime(str(EndDateObj.year) + str(EndDateObj.month) + str(calendar.monthrange(EndDateObj.year, \
         EndDateObj.month)[1]), '%Y%m%d')
print('BOM monthly grids will be extracted from ' +str(StartDateObj.date()) + ' to ' + str(EndDateObj.date()))

# Specify download folder
path = input('Specify the folder the downloads will be saved in: ')
pathrain = str(path) + '\Rain'
pathsolar = str(path) + '\Solar'
pathmaxtemp = str(path) + '\MaxTemp'
pathmintemp = str(path) + '\MinTemp'

createdir = input('Does the folder already exist? Y/N ')
if createdir in ['y', 'Y', 'yes', 'Yes', 'YES']:
    checkfolders = input('Do subfolders for each data type need to be created? Y/N ')
    if checkfolders in ['y', 'Y', 'yes', 'Yes', 'YES']:
        os.mkdir(pathrain)
        os.mkdir(pathsolar)
        os.mkdir(pathmaxtemp)
        os.mkdir(pathmintemp)
        print('Subfolders for each data type created')
    else:
        print('Please ensure no data to be downloaded is already present in subfolders')
        checkfiles = input('Have existing duplicates of data to be downloaded been deleted? Y/N ')
        if checkfiles in ['y', 'Y', 'yes', 'Yes', 'YES']:
            print('BOM download starting.')
        else:
             print('Please recheck file structure and existing data, then restart code')
else:
    os.mkdir(path)
    os.mkdir(pathrain)
    os.mkdir(pathsolar)
    os.mkdir(pathmaxtemp)
    os.mkdir(pathmintemp)
    print('Folder and subfolders for each data type created. BOM download starting.')

print('NOTE: There is a 3-second pause between downloading each file to prevent overloading the BOM server.')

# Create list of date formats to extract from
sleep = 3
ExtractDate = StartDateObj.date()
while ExtractDate <= EndDateObj.date():
    DateInput = str(ExtractDate.year) + str('{:02d}'.format(ExtractDate.month)) + str('{:02d}'.format(ExtractDate.day)) \
    + str(ExtractDate.year) + str('{:02d}'.format(ExtractDate.month)) + str(calendar.monthrange(ExtractDate.year, \
         ExtractDate.month)[1])
    print('Data from ' + str(ExtractDate.year) + '/' + str('{:02d}'.format(ExtractDate.month)) + ' is being downloaded')
    filename = str(DateInput) + '.grid.Z'
# Download BOM grids for date, move to correct subfolders
    #Minimum temperature
    url = "http://www.bom.gov.au/web03/ncc/www/awap/temperature/minave/month/grid/0.05/history/nat/" + str(filename)
    webbrowser.open(url)
    time.sleep(sleep)
    source = os.path.join(r'C:\Users\Tristan RSSRG\Downloads', filename)
    destination = os.path.join(pathmintemp, filename)
    shutil.move(source, destination)
    #Maximum temperature
    url = "http://www.bom.gov.au/web03/ncc/www/awap/temperature/maxave/month/grid/0.05/history/nat/" + str(DateInput) + ".grid.Z"
    webbrowser.open(url)
    time.sleep(sleep)
    source = os.path.join(r'C:\Users\Tristan RSSRG\Downloads', filename)
    destination = os.path.join(pathmaxtemp, filename)
    shutil.move(source, destination)
    # Rainfall
    url = "http://www.bom.gov.au/web03/ncc/www/awap/rainfall/totals/month/grid/0.05/history/nat/" + str(DateInput) + ".grid.Z"
    webbrowser.open(url)
    time.sleep(sleep)
    source = os.path.join(r'C:\Users\Tristan RSSRG\Downloads', filename)
    destination = os.path.join(pathrain, filename)
    shutil.move(source, destination)
    # Solar Exposure
    url = "http://www.bom.gov.au/web03/ncc/www/awap/solar/solarave/month/grid/0.05/history/nat/" + str(DateInput) + ".grid.Z"
    webbrowser.open(url)
    time.sleep(sleep)
    source = os.path.join(r'C:\Users\Tristan RSSRG\Downloads', filename)
    destination = os.path.join(pathsolar, filename)
    shutil.move(source, destination)

    #Iterate to next month
    ExtractDate = ExtractDate + datedelta.MONTH
