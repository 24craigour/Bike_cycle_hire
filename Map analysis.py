#########################################################
#Importing packages#
#########################################################

# importing the folium package, pandas package and the numpy package
import folium
import pandas
import numpy as np
import matplotlib.pyplot as plt
import datetime

bike_data=pandas.read_csv("C:/Users/adam.tran/Desktop/Edinburgh Cycle Hire Project Data/Cycle Hire Data/09-18.csv")



#########################################################
##Doing some exploratory Bike Data analysis using Numpy##
##########################################################

#Looking at the number of rows and columns of the data
#print(np.shape(bike_data))

#Printing all the names of the columns
#print(bike_data.columns.values)

#Print some columns so we can initially look at the data (print first five and last five rows)
#print(bike_data.head())
#print(bike_data.tail())

#Obtain some summary statistics of the dataset
#print(bike_data.describe())

#Doing a quick sample of the data - to get a feel for it
#bike_sample=bike_data.sample(5)
#print(bike_sample)

#Checking for null or missing data - Returns true for missing data
#Can also do missing value imputation but often complicated and heavily debated/multiple ways+ methods
#print(bike_data.isnull())


#Route concatenation
bike_data['Route_path']= (bike_data['start_station_name'])+(bike_data['end_station_name'])


#Creating frequency table of the dataset
start_points=pandas.crosstab(bike_data['start_station_name'], columns='count')
end_points=pandas.crosstab(bike_data['end_station_name'], columns='count')
route_frequency=pandas.crosstab(bike_data['Route_path'], columns='count')

see=route_frequency.sort_values('count', ascending=False)
top_10_routes=see.head(10)

interim_start=start_points.sort_values('count', ascending=False)
interim_end=end_points.sort_values('count', ascending=False)

top_10_start=interim_start.head(10)
top_10_end=interim_end.head(10)

#Calculating frequency of hiring times
#Checking out variable types
print(bike_data.dtypes)

#Convert times to datetime standard format
bike_data['converted_start_times']=pandas.to_datetime(bike_data.started_at)
bike_data['converted_end_times']=pandas.to_datetime(bike_data.ended_at)
print(bike_data.dtypes)

#Obtain day of the week indicator for date times + hour
bike_data['dow_start']=bike_data.converted_start_times.dt.dayofweek
bike_data['dow_end']=bike_data.converted_end_times.dt.dayofweek
bike_data['hour_start']=bike_data.converted_start_times.dt.hour
bike_data['hour_end']=bike_data.converted_end_times.dt.hour
start_dow=pandas.crosstab(bike_data['dow_start'], columns='count')
end_dow=pandas.crosstab(bike_data['dow_end'], columns='count')
start_hour=pandas.crosstab(bike_data['hour_start'], columns='count')
end_hour=pandas.crosstab(bike_data['hour_end'], columns='count')

#########################################################
#Matplotlib - graphs and visualisations
#########################################################

#A histogram of bike journey time
#plt.hist(bike_data['duration'])
#plt.show()


#Plot bar chart of points
top_10_start.plot.bar()
plt.show()

top_10_end.plot.bar()
plt.show()

#Day of week frequency
#start_dow.plot.bar()
#plt.show()

#end_dow.plot.bar()
#plt.show()

#Hour frequency
start_hour.plot.bar()
plt.show()

end_hour.plot.bar()
plt.show()

#Route frequency - Top ten routes in terms of start and stop
top_10_routes.plot.bar()
plt.show()

print(top_10_routes)
#########################################################
#Geographical Visualisations
#########################################################

#Drawing a map around Edinburgh
m = folium.Map(location=[55.95415, -3.20277],zoom_start=13)

#Create markers on the map

#Create Global Tooltip
tooltip = 'Click me!'

#Adding markers for each individual bike station
folium.Marker([55.95474881,	-3.192773669], popup='<i>St Andrew Square</i>', tooltip=tooltip).add_to(m)
folium.Marker([55.95264104,	-3.187526919], popup='<i>Waverley Station</i>', tooltip=tooltip).add_to(m)
folium.Marker([55.96503981,	-3.176686415], popup='<i>Leith Walk</i>', tooltip=tooltip).add_to(m)
folium.Marker([55.96092975,	-3.181005315], popup='<i>Brunswick Place</i>', tooltip=tooltip).add_to(m)


folium.Circle(radius=100,location=[55.95474881,	-3.192773669],popup='The Waterfront',color='crimson',fill=True,).add_to(m)

m.save("map.html")

print(route_frequency.head())