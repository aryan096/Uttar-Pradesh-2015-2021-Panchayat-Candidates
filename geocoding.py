import googlemaps
from datetime import datetime
import pandas as pd
from indictrans import Transliterator
import argparse 

def get_locations(start_index, end_index):

    gmaps = googlemaps.Client(key='AIzaSyCRLecPdPVfKp7TlRydo5I8tFbOj36OIqM')
    h2e = Transliterator(source='hin', target='eng', build_lookup=True)

    missing_data = pd.read_csv('2021_panchayat_elections/missing_data.csv')

    output_file = open('missing_data_locations.csv', 'a+')

    addresses = []
    lats = []
    longs = []
    print(start_index, end_index)

    for i,r in list(missing_data.iterrows())[start_index:end_index]:
        zila = h2e.transform(r[8])
        village = h2e.transform(r[10])
        geocode_result = gmaps.geocode(zila + ', ' + village + ', ' + 'Uttar Pradesh')
        address = 'NA'
        lat = 0
        lon = 0
        try:
            address = geocode_result[0]['formatted_address']
            location = geocode_result[0]['geometry']['location']
            lat = location['lat']
            lon = location['lng']
        except:
            print('woops')
        addresses.append(address)
        lats.append(lat)
        longs.append(lon)

        line = (','.join(str(v) for v in r)) + ',"' + address + '",' + str(lat) + ',' + str(lon) + '\n'
        print(line)
        output_file.write(line)

def main(start_index, end_index):

    get_locations(start_index, end_index)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--array', type = int)
    args = argparser.parse_args()

    # array is the id of the node running
    array = args.array

    start_index = (int(array) - 1) * 187
    end_index = int(array) * 187

    main(start_index, end_index)