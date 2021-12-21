import pandas as pd 

missing_data = pd.read_csv('up_gram_panchayat_pradhan_candidates_2021_missing.csv')

missing_data['village'] = missing_data['village'].apply(lambda x: x.split('-')[1])

missing_data['matching'] = missing_data['vikaskhand'] + ' ' + missing_data['village']

missing_data_runner_ups = missing_data[missing_data['result'] == 'runner-up']
missing_data_runner_ups = missing_data_runner_ups[['candidate_name_2021','father_husband_name_2021','gender','age','education','caste','vote_percentage','matching']]
missing_data_winner = missing_data[missing_data['result'] == 'winner']

missing_data_runner_ups.merge(missing_data_winner, on='matching').to_csv('missing_data.csv')
