from google.transliteration import transliterate_word
import csv
import pandas as pd
from indictrans import Transliterator
import numpy as np


census = pd.read_csv('census_locations.csv')
pradhans = pd.read_csv('2021_pradhans_locations.csv')
district_codes = pd.read_csv('district_codes.csv')
codes = dict((row[1],row[0]) for i,row in district_codes.iterrows())

census_group = []
pradhans_group = []

for i,r in census.iterrows():
    code = codes[(r[1].strip().split()[0][1:])]
    census_group.append(code)

census = census.drop(columns='group')
census['group'] = census_group
census = census[['group','location']]
census.to_csv('census.csv', header=False, index=False, quoting=csv.QUOTE_NONE)
districts = []

for i,r in pradhans.iterrows():
    try:
        code = codes[(r[1].strip().split()[0][1:]).capitalize()]
    except:
        code = 0
    pradhans_group.append(code)

pradhans = pradhans.drop(columns='group')
pradhans['group'] = pradhans_group
pradhans = pradhans[['group','location']]
pradhans.to_csv('pradhans.csv', header=False, index=False, quoting=csv.QUOTE_NONE)
#-------------------------------------------------------------------
# CREATING FILES FOR MASALA MERGE

# locations = pd.read_csv('census_2001_villages.csv', index_col=0)
# pradhans = pd.read_csv('2021_pradhans_eng_matching.csv')

# census_locations = locations['matching']
# pradhans_locations = pradhans['eng_matching']

# with open('census_locations.csv', 'w+') as f:
#     for line in census_locations:
#         f.write('0, "' + line + '"\n')

# with open('2021_pradhans_locations.csv', 'w+') as f:
#     for line in pradhans_locations:
#         f.write('0, "' + line + '"\n')

#-------------------------------------------------------------------
## TRANSLITERATING

# locations = pd.read_csv('census_2001_villages.csv', index_col=0)
# pradhans = pd.read_csv('up_gp_pradhan_locations.csv')

# pradhans = pradhans.drop(columns=['confidence', 'latitude', 'longitude'])
# h2e = Transliterator(source='hin', target='eng', build_lookup=True)
# eng_matching_col = []

# for i,r in pradhans.iterrows():
#     # for each row, transliterate the zila + village name to english
#     matching = r[1] + ' ' + r[3]
#     eng_matching = h2e.transform(matching)
#     eng_matching_col.append(eng_matching)
#     print(i)

# pradhans['eng_matching'] = eng_matching_col
# pradhans.to_csv('2021_pradhans_eng_matching.csv')


# pradhan_religion_labels = pd.read_csv('pradhan_geohash_religion_labels.csv')
# combined_data = pd.read_csv('combined_data.csv')

# combined_data = combined_data.assign(candidate_religion_2021=pd.Series(['-' for i in range(12949)]))
# combined_data = combined_data.assign(candidate_religion_2015=pd.Series(['-' for i in range(12949)]))

# for i,r in combined_data.iterrows():
#     matching = r[0]
#     match = pradhan_religion_labels.loc[pradhan_religion_labels['matching'] == matching]

#     religion_2021, religion_2015 = '-', '-'

#     if not match.empty:
#         combined_data.at[i,'candidate_religion_2021'] = match['candidate_religion_2021'].values[0]
#         combined_data.at[i,'candidate_religion_2015'] = match['candidate_religion_2015'].values[0]

# combined_data.to_csv('combined_data_rel_labels.csv', index=False)


# with open('cleaned_UP_locations.csv') as f:
#     nf = open('new_cleaned_UP_locations.csv', 'w+')

#     for line in f.readlines()[1:]:
#         splitted = line.split(',')
#         if splitted[0] != splitted[2]:
#             nf.write(line)



# district_codes = {}
# with open('cleaned_UP_district_codes.csv') as f:
#     lines = f.readlines()
#     for line in lines[1:]:
#         if line == '\n':
#             break
#         splitted = line.split(',')
#         code = splitted[2].strip()
#         en_name = splitted[0]
#         hi_name = splitted[1]
        
#         if code not in district_codes:
#             district_codes[code] = (en_name, hi_name)

# with open('cleaned_UP_locations.csv') as f:
#     nf = open('new_cleaned_UP_locations.csv', 'w+')
#     lines = f.readlines()
#     writer = csv.writer(nf)
#     for line in lines:
#         splitted = line.split(',')
#         village = splitted[0].strip()
#         code = splitted[1].strip()
#         lat = splitted[2].strip()
#         longit = splitted[3].strip()
#         try:
#             (en_name, hi_name) = district_codes[code]
#             writer.writerow([village, en_name, hi_name, code, lat, longit])
#         except:
#             print('not found')
        

