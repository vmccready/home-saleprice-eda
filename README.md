# Snohomish County Housing Market Analysis
Exploratory Data Analysis of Home Sales in Seattle Area

Home prices in the Greater Seattle Area have been rapidly increasing for over a decade. This continued increase in price has made the area a prime location for investment, but also a barrier to those looking to buy their first home.

As a current resident I hope to gain some insight in this market as a potential owner and investor. What influences the value of a home? Using publicly available information of home sales I hope to explore factors that influence price or correlate with price and value. 

![](img/fredgraph.png)

## Data
Snohomish County provides data for home sales through a web search [available here.](http://www.snoco.org/app4/sas/assessor/services/salessearch.aspx) The data available from this search is shown below in the first row. As we can see some values could be missing, but certain columns always had values including: parcel, date of sale, sale price, and use code. The county also provides parcel information in a separate search, but the information in the sale query has the primary columns I would like to explore. The information was scraped from the web with multiple queries since each individual search result had a max return value of 800 results. Data was stored in a Mongo Database as strings and were cleaned through a data pipeline into the useable types shown in the second row. 


|    |       Parcel # | Date of Sale        |   Sale Price |   Lot Size |   Year Built | Type      | Quality/Grade   |   Sqft | Address                  | City      |    Nbhd |   Use Code |
|---:|---------------:|:--------------------|-------------:|-----------:|-------------:|:----------|:----------------|-------:|:-------------------------|:----------|--------:|-----------:|
|  0 | 31051100400500 | 1/31/2020 12:00:00 AM | $2,500,000.00 |       5.44 |              |           |                 |        | 21015 STATE ROUTE 9 NE | Arlington | Nbhd:5203000 |        521 |
|  2 | 00960009607300 | 2020-01-31 12:00:00 |        75000 |       0    |         1996 | Dbl Wide  | V Good          |   1620 | 20227 80TH AVE NE SPC 73 | Arlington | 2408906 |        119 |

## Exploratory Data Analysis

One of our primary columns to observe is price. However it may be difficult to draw conclusions when the prices for homes change over time. One assumption we will have to make is that any possible influencers of price change uniformly between the different factors. This allows us to examine a larger dataset and at the moment I hope to draw general conclusions that are not time specific. 

![](img/mean_price_time.png)

### Narrowing to Single Family Residences
#### Use codes
The data we would like to observe specifically are values for single family residences. This is the most available home type and the lowest cost of entry for both investors and people looking for a place to live. Use Codes distinguish the different types of homes. T

![](img/use_code_counts.png)

As we can see, the majority fall in the 111 Single Family Residence - Detached. This is what one would imagine as the "Standard House": no shared walls on its own property. 

Another assumption I will make is that a larger home has a higher price as we can see below. This is fairly obvious and intuitive, so in order to make general conclusions I will normalize this price by comparing a common metric for home values: Price per Square foot. 

![](img/price_sqft_sfr.png)

I would like to do see if there is a significant difference in value based on the different use codes. To do so I will use a t-test and test against my null hypotheses that there is no significant difference in price per square foot between the different use codes. Before testing I will confirm that the distributions of the price per square feet are normal. 

![](img/price_sqft_sfr_hists.png)

Now I know the distributions are normal I can determine if the difference is significant. I would like to be 90% confident before rejecting any null hypothesis After comparing the data for different use codes I found that I could not reject the following hypotheses:
1. Single Family Residences - Detached are drawn from the same distribution as Common Wall Single Family Residences.
2. Single Family Residences - Detached are drawn from the same distribution as Single Family Residence Condominium Detached. 
The 1st case above had a p-value of 0.20 and the 2nd had a p-value of 0.102. Though the p-value was close to my rejection threshold, I did not have enough evidence to reject my hypothesis in general. Looking at specific date ranges may yield different results if I were to do additional exploration. 


