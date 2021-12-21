from selenium import webdriver

import csv
import time
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Firefox()  

driver.maximize_window()  
driver.get("http://sec.up.nic.in/ElecLive/WinnerList.aspx")  

el = driver.find_element_by_id("ContentPlaceHolder1_ddlpost")

# open the file in the write mode
f = open('up_gram_panchayat_pradhan_winners_2015.csv', 'w+')
header = ['zila', 'block', 'gram_panchayat', 'aarakshan', 'candidate_name', 'father_husband_name', 'caste', 'education', 'gender', 'mobile_num', 'votes_received', 'votes_percentage', 'voter_turnout']
# create the csv writer
writer = csv.writer(f)            

# write the header
writer.writerow(header)

INDEX = 0

while True:
    for option in el.find_elements_by_tag_name('option'):
        if option.text == 'ग्राम पंचायत प्रधान':
            option.click()
            time.sleep(0.5)
            zila = driver.find_element_by_id('ContentPlaceHolder1_ddlDistrict')
            zila_options = zila.find_elements_by_tag_name('option')
            zila_options = [opt.text for opt in zila_options]

            for index, opt in enumerate(zila_options):

                opt_obj = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[6]/div/table/tbody/tr/td[1]/select/option' + '[' + str(index + 1) + ']')
                if opt != 'जिला चुनें':

                    if index < INDEX:
                        continue
                    opt_obj.click()
                    print(INDEX, opt)

                    time.sleep(10)

                    while True:
                        try:
                            winner_table = driver.find_element_by_id('ContentPlaceHolder1_winnerdetail')
                        except:
                            print('trying to find table again')
                        break

                    while True:
                        try:
                            table_rows = winner_table.find_elements_by_tag_name('tr')
                            time.sleep(0.5)
                            
                            for row in table_rows[1:]:

                                cols = row.find_elements_by_tag_name('td')
                                block = cols[0].text 
                                gram_panchayat = cols[1].text
                                aarakshan = cols[2].text
                                candidate_name = cols[3].text
                                father_husband_name = cols[4].text
                                caste = cols[5].text
                                education = cols[6].text
                                gender = cols[7].text
                                mobile_num = cols[8].text
                                votes_received = cols[9].text
                                votes_percentage = cols[10].text
                                voter_turnout = cols[11].text
                                
                                writer.writerow([opt, block, gram_panchayat, aarakshan, candidate_name, father_husband_name, caste, education, gender, mobile_num, votes_received, votes_percentage, voter_turnout])
                        except:
                            print('whoops')
                        break

            INDEX += 1
            break


f.close()


    