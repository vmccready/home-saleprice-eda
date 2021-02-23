
# Connect to Database
from pymongo import MongoClient

# Requests sends and recieves HTTP requests.
import requests

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
    client = MongoClient('localhost', 27017)
    