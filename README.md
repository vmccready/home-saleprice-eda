![]()

# Snohomish County Housing Market Analysis
Exploratory Data Analysis of Home Sales in Seattle Area

Home prices in the Greater Seattle Area have been rapidly increasing for over a decade. This continued increase in price has made the area a prime location for investment, but also a barrier to those looking to buy their first home.

As a current resident I hope to gain some insight in this market as a potential owner and investor. Using publicly available information of home sales, I hope to explore factors that influence price or correlate with price and value. 
```
         (
 
           )
         ( _   _._
          |_|-'_~_`-._
       _.-'-_~_-~_-~-_`-._
   _.-'_~-_~-_-~-_~_~-_~-_`-._
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |  []  []   []   []  [] |
    |           __    ___   |   
  ._|  []  []  | .|  [___]  |_._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._. 
  |=|________()|__|()_______|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|
^^^^^^^^^^^^^^^ === ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    _______      ===   
   <_4sale_>       === 
      ^|^             ===
       |                 ===
```
## Data
Snohomish County provides data for home sales through a web search [available here.](http://www.snoco.org/app4/sas/assessor/services/salessearch.aspx) The data available from this search is shown below in the first row. As we can see some values could be missing, but certain columns always had values including: parcel, date of sale, sale price, and use code. The county also provides parcel information in a separate search, but the information in the sale query has the primary columns I would like to explore. The information was scraped from the web with multiple queries since each individual search result had a max return value of 800 results. Data was stored in a Mongo Database as strings and were cleaned through a data pipeline into the useable types shown in the second row. 


|    |       Parcel # | Date of Sale        |   Sale Price |   Lot Size |   Year Built | Type      | Quality/Grade   |   Sqft | Address                  | City      |    Nbhd |   Use Code |
|---:|---------------:|:--------------------|-------------:|-----------:|-------------:|:----------|:----------------|-------:|:-------------------------|:----------|--------:|-----------:|
|  0 | 31051100400500 | 1/31/2020 12:00:00 AM | $2,500,000.00 |       5.44 |              |           |                 |        | 21015 STATE ROUTE 9 NE | Arlington | Nbhd:5203000 |        521 |
|  2 | 00960009607300 | 2020-01-31 12:00:00 |        75000 |       0    |         1996 | Dbl Wide  | V Good          |   1620 | 20227 80TH AVE NE SPC 73 | Arlington | 2408906 |        119 |

## 
