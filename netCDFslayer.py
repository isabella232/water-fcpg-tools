import rasterio as rs
import numpy as np
import datetime

# Script to destroy the netCDF file Roy got from gridMET

netCDFpath = "../data/cov/gridMET_PRmm.tif"

baseName = "gridMET_PRmm"

with rs.open(netCDFpath) as ds: # load parameter raster
        numBands = ds.count
        data = ds.read()
        profile = ds.profile
        paramNoData = ds.nodata
        tags = ds.tags()

day0 = datetime.datetime.strptime("01_01_1900", "%d_%m_%y") #Set the day time is counted from


days = list(tags["NETCDF_DIM_time_VALUES"]) #Get the list of dates associated with each band and convert to list

print(dates)

i = 0 

for band in data:

        day = days[i] #Get the days since beginning associated with the band
        
        date = day0 + datetime.timedelta(days=day) #Compute the date associated with the band

        fileName = baseName + "_" + datetime.strftime('%d_%m_%Y') + ".tif" #Create the name for the output file

        print(fileName)




        


        i = i + 1

