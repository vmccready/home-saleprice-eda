# Functions to clean data

import datetime
import pandas as pd
import numpy as np

def date_clean(d):
    return datetime.datetime.strptime(d, '%m/%d/%Y %H:%M:%S %p')

def sale_price_clean(price):
    return float(price.strip('$').replace(',',''))

def year_built_clean(year):
    if year:
        return int(year)
    else:
        return None

def sqft_clean(sqft):
    if sqft:
        return float(sqft)
    else:
        return None

def city_clean(city):
    wrong_city = {
        'BOT        Bothell': 'Bothell',
        'MIL        Mill Creek': 'Mill Creek',
        'LAKESTEVENS': 'Lake Stevens',
        'LYN        Lynnwood': 'Lynnwood',
        'BRI        Brier': 'Brier',
        'GF': 'Granite Falls',
        'MILLCREEK': 'Mill Creek',
        'EDM        Edmonds': 'Edmonds',
        'MUKILTEO': 'Mukilteo',
        'EVEEverett': 'Everett',
        'STA        Stanwood': 'Stanwood',
        'UNKNOWN': ''
    }
    if city in wrong_city:
        return wrong_city[city]
    return city

def nbhd_clean(nbhd):
    return nbhd.split(':')[1]

columns = {
#     'Parcel #':
    'Date of Sale': date_clean,
    'Sale Price': sale_price_clean,
    'Lot Size': float,
    'Year Built': year_built_clean,
#     'Type':
#     'Quality/Grade':
    'Sqft':sqft_clean,
#     'Address':
    'City': city_clean,
    'Nbhd': nbhd_clean,
    'Use Code': int
}

def clean_all_data(data):
    cleaned_data = data.copy()

    for column, c_func in columns.items():
        cleaned_data[column] = cleaned_data[column].map(c_func)
    
    return cleaned_data

def remove_bad_values(data):
    filtered_data = data.copy()

    # Duplicate sales
    filtered_data['sale_id'] = filtered_data['Parcel #'] + filtered_data['Date of Sale'].map(str)
    filtered_data.drop_duplicates(
        'sale_id', keep=False, inplace=True)

    # Duplicate sales
    filtered_data['batch'] =  filtered_data['Date of Sale'].map(str) + filtered_data['Sale Price'].map(str)
    filtered_data.drop_duplicates(
        'batch', keep=False, inplace=True)

    # Remove too small sqft
    filtered_data = filtered_data[filtered_data['Sqft']>100]

    # Remove impossible years
    filtered_data = filtered_data[
        (filtered_data['Year Built'] < 2022)&
        (filtered_data['Year Built'] > 1850)]
    
    # Remove non-residential use codes
    filtered_data = filtered_data[
        (filtered_data['Use Code']<150) & 
        (filtered_data['Use Code']>99)]
    
    # Remove too low Sale Price
    filtered_data = filtered_data[filtered_data['Sale Price']>25000]

    return filtered_data.drop(['sale_id', 'batch'], axis=1)
