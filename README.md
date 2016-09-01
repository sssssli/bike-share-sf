# bike-share-sf

Open source dataset from SF Bay Area Bike Share downloaded from [Kaggle.com (version 1.0)](https://www.kaggle.com/benhamner/sf-bay-area-bike-share)

Plan for this short little project:

1. Data visualizations, make some interesting insights from the data
2. Build a predictive model for guessing at bike availability per station
3. Front end portal for end user to use
4. Through on AWS (optional)
5. API friendly (optional)

## Data visualizations/Cleaning
### Basics
- [ ] Size of each table
- [ ] Identify/visualize missing values, number of distinct values
- [ ] Add another `Holiday` column in the trip, status, and weather table: U.S holiday
- [ ] Histogram of every column
- [ ] Distribution of bike usage by bike ID (to identify life time of a bike)
- [ ] Correlation analysis
  - [ ] Between bike usage and time, day of the week, holiday, seasonality
  - [ ] Between bike usage and weather

### Geo Visualization (via Google API?!)
- [ ] Label all the stations (heat map of usage)
- [ ] Identify all the routes
  - [ ] Just plot the routes first
  - [ ] by day of the week
  - [ ] by weather

**Options for graph/geo visualization**
- Gephi
- Networkx
- Neo4j
