#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Flask
from flask import Flask, jsonify


# In[3]:


# Dependencies and Setup
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy


# In[4]:


# Dependencies and Setup
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.pool import StaticPool


# In[5]:


#create engine, reflect database
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station


# In[6]:


#create session link
session = Session(engine)


# In[9]:


#define flask app--define welcome route
app = Flask(__name__)
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')


# In[10]:


@app.route("/api/v1.0/precipitation")

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)


# In[11]:


@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


# In[12]:


@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.tobs).    filter(Measurement.station == 'USC00519281').    filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


# In[40]:


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]           

    if not end: 
        results = session.query(*sel).        filter(Measurement.date <= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

        results = session.query(*sel).        filter(Measurement.date >= start).        filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

