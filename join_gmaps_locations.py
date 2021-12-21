import pandas as pd 

gmaps = pd.read_csv('2021_pradhans_gmaps.csv')
pradhans = pd.read_csv('up_gp_pradhans_locations.csv')

pradhans = pradhans.drop(columns = ['zila_y', 'village', 'latitude', 'longitude', 'confidence']).drop_duplicates()
gmaps = gmaps[['matching','gmaps_address','lat','long']].drop_duplicates()

merged = (pradhans.merge(gmaps,on='matching'))
merged.to_csv('gmaps_pradhans.csv')
