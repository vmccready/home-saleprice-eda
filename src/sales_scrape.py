
# Connect to Database
# from pymongo import MongoClient

# Requests sends and recieves HTTP requests.
import requests
import pandas as pd 
import numpy as np 
import random 
import time 
from datetime import date 
from bs4 import BeautifulSoup

snohomish_cities = [
    'Arlington', 
    'Bothell',
    'Brier',
    'Darrington',
    'Edmonds',
    'Everett',
    'Gold Bar',
    'Granite Falls',
    'Index',
    'Lake Stevens',
    'Lynnwood',
    'Marysville',
    'Mill Creek',
    'Monroe',
    'Mountlake Terrace',
    'Mukilteo',
    'Snohomish',
    'Stanwood',
    'Sultan',
    'Woodway']


def get_sales(city, start_date, end_date):
    # Return search URL with given parameters
    # Parameters:
    # city: str - city to search
    # start_date: date
    sale_search_url = 'http://www.snoco.org/app4/sas/assessor/services/salessearch2.aspx?TextBox1={city}&TextBox12=&DropDownList3=&DropDownList1=&DropDownList2=&TextBox2=&TextBox3=&TextBox4=&TextBox5=&TextBox8=&TextBox9=&TextBox10={s_m}%2F{s_d}%2F{s_y}&TextBox11={e_m}%2F{e_d}%2F{e_y}'
    search_term = sale_search_url.format(
        city='Arlington', 
        s_m=start_date.month, s_d=start_date.day, s_y=start_date.year,
        e_m=end_date.month, e_d=end_date.day, e_y=end_date.year)
    return search_term

if __name__=='__main__':
    # client = MongoClient('localhost', 27017)
    empty_row = {
        "Parcel #": None, 
        "Date of Sale": None, 
        "Sale Price": None, 
        "Lot Size": None,
        "Year Built": None,
        "Type": None,
        "Quality/Grade": None,
        "Sq.ft.": None,
        "Address": None,
        "City": None,
        "Nbhd": None,
        "Use Code": None}
    
    # Create months
    from pandas.tseries.offsets import MonthEnd
    months = []
    for beg in pd.date_range('2020-01-01', '2020-12-1', freq='MS'):
        months.append((
            date.fromisoformat( beg.strftime("%Y-%m-%d") ), 
            date.fromisoformat( (beg + MonthEnd(1)).strftime("%Y-%m-%d")) ))
    

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    all_rows = []
    for city in snohomish_cities:
        for month in months:
            # Get info for each city and month
            print(f"Getting {city} sales from {month[0]} to {month[1]}")
            
            try:
                start = time.time()
                r = requests.get(get_sales(city, month[0], month[1]), headers=headers)
                soup = BeautifulSoup(r.content, "html.parser")
                delay = time.time() - start
                
                # select the table
                table = soup.find("table", {"id": "GridView1"})
                rows = table.find_all("tr", recursive=False)
            except Exception as e:
                print(e)
            
            # loop through entries on page
            if rows:
                for row in rows[1:]:
                    new_row = empty_row.copy()
                    columns = row.find_all("td")
                    new_row['Parcel #'] = columns[1].a.text.strip()
                    new_row['Date of Sale'] = columns[2].text.strip()
                    new_row['Sale Price'] = columns[3].text.strip()
                    new_row['Lot Size'] = columns[4].text.strip()
                    new_row['Year Built'] = columns[5].text.strip()
                    new_row['Type'] = columns[6].text.strip()
                    new_row['Quality/Grade'] = columns[7].text.strip()
                    new_row['Sqft'] = columns[8].text.strip()
                    new_row['Address'] = columns[9].text.strip()
                    new_row['City'] = columns[10].text.strip()
                    new_row['Nbhd'] = columns[11].text.strip()
                    new_row['Use Code'] = columns[12].text.strip()
                    all_rows.append(new_row)
            else:
                print("No results for {city} from {month[0]} to {month[1]}")
            
            # timer between request
            time.sleep(random.uniform(2, 4) * delay)
    
    pd.DataFrame(all_rows).to_csv('sales.csv')



