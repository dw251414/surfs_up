# surfs_up
--- 

## Overview Analysis

   The purpose of our analysis is to see temperature statistics for June and December to see if running a surf shop is sustainable year around. 
      The way we get the temperature data is by running two seperate queries, one being for June and the other being December. 
      Once we run our queries we store the temperatures in a list then convert them to a dataframe. 
             Once our dataframe is created we are able to get our summary statistics by using the .describe() method. Here is what we found:

## Comparison Analysis:

Based on a comparison of precipitation and temperature between June and December from 2010 to 2017 across all observation stations, it’s possible to notice the following statistical information:

  - In June we had a total count of 1700, mean of 74.9, min of 64.0 and max of 85.0
  - In December we had a total count of 1517, mean of 71.0, min of 56.0 and max of 83.0
  - Standard deviation is 3.25 in June and 3.75 -- making a .5 difference in the two different seasons

## Analysis Limitation Recommendation:

  - The lack of data in December, 2017 may cause less reliable of data. The database should generate more recently winter data to compare summer and winter precipitation.
  - In addition of statistical summery, various features and plots may help us better analyze the seasonal weather. For example, line plots would be able to provide quick and easy way to show time-varying. Histogram plots would tell us frequency of precipitation as well as temperature for both December and Jane.
  - For seasonal analysis, we need filter more detail precipitation and temperatures for Spring and Autumn.

--- 

## Summary

From our data we can tell what our temperatures are but since there are other attributes to the weather such as precipitation it shows that we can run additional queries to let us know whether or not people can come and visit the shop. If we are able to gain more data for the area we can run even more queries! From there we can decide how we would like to build the shop and what areas would make this a more prominent location for visitors to come.
