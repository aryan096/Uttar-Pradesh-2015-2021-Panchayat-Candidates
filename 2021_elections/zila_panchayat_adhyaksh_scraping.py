from selenium import webdriver
import csv

driver = webdriver.Firefox()  

driver.maximize_window()  
driver.get("http://sec.up.nic.in/site/DownloadCandidateFaDebt.aspx")  

el = driver.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_ddlPostTypes\"]")

# open the file in the write mode
f = open('up_zila_panchayat_adhyaksh_candidates.csv', 'w')
header = ['zila', 'reservation', 'candidate_id', 'candidate_name', 'father_or_husband_name', 'gender', 'age', 'education', 'caste', 'movable_property', 'immovable_property', 'criminal_history', 'votes_received', 'votes_percentage', 'legal_votes_percentage', 'assets_status', 'result']
# create the csv writer
writer = csv.writer(f)            

# write the header
writer.writerow(header)

for option in el.find_elements_by_tag_name('option'):
    if option.text == 'जिला पंचायत अध्यक्ष':
        option.click()
        janpad = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddlDistrictName"]')
        options = janpad.find_elements_by_xpath('/html/body/div/div[2]/form/div[3]/div[3]/div[1]/table/tbody/tr[1]/td[2]/select/option')
        options = [opt.text for opt in options]
        for index, opt in enumerate(options):
            opt_obj = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[3]/div[3]/div[1]/table/tbody/tr[1]/td[2]/select/option' + '[' + str(index + 1) + ']')
            if opt != 'जनपद चुनें':
                opt_obj.click()
                
                driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_btnSubmit"]').click()
                zila = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[3]/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[1]').text
                aarakshan = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[3]/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[2]').text
                
                tbody = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[3]/div[3]/div[2]/div[2]/table/tbody')
                table_rows = tbody.find_elements_by_tag_name('tr')
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
                        writer.writerow([zila, aarakshan, candidate_id, candidate_name, father_husband_name, gender, age, education, caste, movable_property, immovable_property, criminal_history, votes_received, votes_percentage, legal_votes_percentage, assets_status, result])
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

                        writer.writerow([zila, aarakshan, candidate_id, candidate_name, father_husband_name, gender, age, education, caste, movable_property, immovable_property, criminal_history, votes_received, votes_percentage, legal_votes_percentage, assets_status, result])
                
        break

f.close()


