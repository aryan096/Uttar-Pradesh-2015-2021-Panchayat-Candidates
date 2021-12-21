from selenium import webdriver
import csv
import time

driver = webdriver.Firefox()  

driver.maximize_window()  
driver.get("http://sec.up.nic.in/site/DownloadCandidateFaDebt.aspx")  

el = driver.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_ddlPostTypes\"]")

# open the file in the write mode
f = open('up_zila_panchayat_sadasya_candidates.csv', 'a')
header = ['zila', 'reservation', 'candidate_id', 'candidate_name', 'father_or_husband_name', 'gender', 'age', 'education', 'caste', 'movable_property', 'immovable_property', 'criminal_history', 'votes_received', 'votes_percentage', 'legal_votes_percentage', 'assets_status', 'result']
# create the csv writer
writer = csv.writer(f)            

# write the header
# writer.writerow(header)

INDEX = 69

for option in el.find_elements_by_tag_name('option'):
    if option.text == 'जिला पंचायत सदस्य':
        option.click()
        time.sleep(0.1)
        janpad = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlDistrictName')
        janpad_options = janpad.find_elements_by_tag_name('option')
        janpad_options = [opt.text for opt in janpad_options]

        for index, opt in enumerate(janpad_options):

            opt_obj = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[3]/div[3]/div[1]/table/tbody/tr[1]/td[2]/select/option' + '[' + str(index + 1) + ']')
            if opt != 'जनपद चुनें':

                if index < INDEX:
                    continue
                opt_obj.click()
                
                # loop through all the wards
                wards = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlZpWardName')
                wards_options = wards.find_elements_by_tag_name('option')
                wards_opts = [w.text for w in wards_options]
                time.sleep(0.5)
                for index, ward_opt in enumerate(wards_opts):
                    ward_obj = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[3]/div[3]/div[1]/table/tbody/tr[2]/td/select/option' + '[' + str(index + 1) +']')
                    time.sleep(0.3)
                    if ward_opt != 'जिला पंचायत वॉर्ड चुनें':
                        ward_obj.click()
                        
                        # click view button
                        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_btnSubmit"]').click()
                        time.sleep(1)
                        zila = opt  
                        ward_table = driver.find_element_by_id('ctl00_ContentPlaceHolder1_GridView1')
                        try:
                            aarakshan = ward_table.find_elements_by_tag_name('td')[1].text
                            ward = ward_table.find_elements_by_tag_name('td')[0].text 
                        except IndexError:
                            continue

                        candidate_table = driver.find_element_by_id('ctl00_ContentPlaceHolder1_GridView2')
                        table_rows = candidate_table.find_elements_by_tag_name('tr')
                        time.sleep(0.5)
                        for row in table_rows[1:]:
                            if len(table_rows) > 2:
                                cols = row.find_elements_by_tag_name('td')
                                candidate_id = cols[1].text
                                candidate_name = cols[2].text
                                father_husband_name = cols[3].text
                                gender = cols[4].text
                                age = cols[5].text
                                education = cols[6].text
                                caste = cols[7].text
                                movable_property = cols[8].text
                                immovable_property = cols[9].text
                                criminal_history = cols[10].text
                                votes_received = cols[11].text
                                votes_percentage = cols[12].text
                                legal_votes_percentage = cols[13].text
                                assets_status = cols[14].text
                                result = cols[15].text
                                writer.writerow([zila, ward, aarakshan, candidate_id, candidate_name, father_husband_name, gender, age, education, caste, movable_property, immovable_property, criminal_history, votes_received, votes_percentage, legal_votes_percentage, assets_status, result])
                            else:
                                cols = row.find_elements_by_tag_name('td')
                                candidate_id = cols[1].text
                                candidate_name = cols[2].text
                                father_husband_name = cols[3].text
                                gender = cols[4].text
                                age = cols[5].text
                                education = cols[6].text
                                caste = cols[7].text
                                movable_property = cols[8].text
                                immovable_property = cols[9].text
                                criminal_history = cols[10].text
                                result = cols[11].text
                                votes_received = 'N/A'
                                votes_percentage = 'N/A'
                                legal_votes_percentage = 'N/A'

                                writer.writerow([zila, ward, aarakshan, candidate_id, candidate_name, father_husband_name, gender, age, education, caste, movable_property, immovable_property, criminal_history, votes_received, votes_percentage, legal_votes_percentage, assets_status, result])
                
        break

f.close()


