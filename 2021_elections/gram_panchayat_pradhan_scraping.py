from selenium import webdriver

import csv
import time
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Firefox()  

driver.maximize_window()  
driver.get("http://sec.up.nic.in/site/DownloadCandidateFaDebt.aspx")  

el = driver.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_ddlPostTypes\"]")

# open the file in the write mode
f = open('up_gram_panchayat_pradhan_candidates_2021_missing.csv', 'a')
header = ['zila', 'vikas_khand', 'gram_panchayat_name', 'aarakshan', 'candidate_name', 'father_husband_name', 'gender', 'age', 'education', 'caste', 'criminal_history', 'vote_percentage', 'results']
# create the csv writer
writer = csv.writer(f)            

# write the header
# writer.writerow(header)

INDEX = 0

while True:
    for option in el.find_elements_by_tag_name('option'):
        if option.text == 'ग्राम पंचायत प्रधान':
            option.click()
            time.sleep(0.5)
            zila = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlDistrictName')
            zila_options = zila.find_elements_by_tag_name('option')
            zila_options = [opt.text for opt in zila_options]

            for index, opt in enumerate(zila_options):

                opt_obj = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[3]/div[3]/div[1]/table/tbody/tr[1]/td[2]/select/option' + '[' + str(index + 1) + ']')
                if opt in ['बाराबंकी']:

                    if index < INDEX:
                        continue
                    opt_obj.click()
                    time.sleep(0.3)

                    opt_obj = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[3]/div[3]/div[1]/table/tbody/tr[1]/td[2]/select/option' + '[' + str(index + 1) + ']')
                    opt_obj.click()
                    time.sleep(0.2)

                    # loop through all the vikas khands

                    vikas_khands = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlBlockName')
                    vk_options = vikas_khands.find_elements_by_tag_name('option')
                    vk_options = [o.text for o in vk_options]

                    for i, vk_opt in enumerate(vk_options):
                        vk_obj = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[3]/div[3]/div[1]/table/tbody/tr[1]/td[3]/select/option' + '[' + str(i + 1) + ']')
                        
                        if vk_opt != 'ब्लॉक चुनें ':
                            vk_obj.click()

                            time.sleep(0.2)

                            while True:
                                try:
                                    gram_panchayats = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddlGpName"]')
                                    gp_options = gram_panchayats.find_elements_by_tag_name('option')
                                    gp_options = [g.text for g in gp_options]
                                    break
                                except:
                                    print('trying to get gp list again')

                            for j, gp_opt in enumerate(gp_options):
                                time.sleep(0.5)

                                while True:
                                    try:
                                        try:
                                            gp_obj = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[3]/div[3]/div[1]/table/tbody/tr[1]/td[4]/select/option' + '[' + str(j + 1) + ']')
                                        except:
                                            print('shit')
                                            break

                                        if gp_opt != 'ग्राम पंचायत चुनें':
                                            gp_obj.click()
                                            time.sleep(0.4)

                                            while True:
                                                try:
                                                    driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnSubmit').click()
                                                    break
                                                except:
                                                    print('pressing button again')

                                            time.sleep(0.5)
                                            
                                            while True:
                                                try:
                                                    gp_table = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[3]/div[3]/div[2]/div[1]/table')
                                                    break
                                                except:
                                                    driver.find_element_by_id('ctl00_ContentPlaceHolder1_btnSubmit').click()
                                                    print('trying to get gp table again')
                                            time.sleep(0.3)

                                            try:
                                                aarakshan = gp_table.find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[3].text
                                            except:
                                                aarakshan = ''

                                            zila = opt
                                            vikas_khand = vk_opt
                                            gram_panchayat_name = gp_opt

                                            time.sleep(0.6)

                                            while True:
                                                try:   
                                                    # winner_candidate = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_GridView2"]').find_elements_by_tag_name('tr')[1]
                                                    # winner_candidate_name = winner_candidate.find_elements_by_tag_name('td')[2].text
                                                    # winner_candidate_father_husband_name = winner_candidate.find_elements_by_tag_name('td')[3].text
                                                    # winner_candidate_age = winner_candidate.find_elements_by_tag_name('td')[5].text
                                                    # winner_candidate_gender = winner_candidate.find_elements_by_tag_name('td')[4].text
                                                    # winner_candidate_education = winner_candidate.find_elements_by_tag_name('td')[6].text
                                                    # winner_candidate_caste = winner_candidate.find_elements_by_tag_name('td')[7].text
                                                    # winner_candidate_criminal_history = winner_candidate.find_elements_by_tag_name('td')[10].text
                                                    # winner_candidate_vote_percentage = winner_candidate.find_elements_by_tag_name('td')[12].text
                                                    # writer.writerow([zila, vikas_khand, gram_panchayat_name, aarakshan, winner_candidate_name, winner_candidate_father_husband_name, winner_candidate_gender, winner_candidate_age, winner_candidate_education, winner_candidate_caste, winner_candidate_vote_percentage, 'winner'])
                                                    runner_up_candidate = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_GridView2"]').find_elements_by_tag_name('tr')[2]
                                                    runner_up_candidate_name = runner_up_candidate.find_elements_by_tag_name('td')[2].text
                                                    runner_up_candidate_father_husband_name = runner_up_candidate.find_elements_by_tag_name('td')[3].text
                                                    runner_up_candidate_age = runner_up_candidate.find_elements_by_tag_name('td')[5].text
                                                    runner_up_candidate_gender = runner_up_candidate.find_elements_by_tag_name('td')[4].text
                                                    runner_up_candidate_education = runner_up_candidate.find_elements_by_tag_name('td')[6].text
                                                    runner_up_candidate_caste = runner_up_candidate.find_elements_by_tag_name('td')[7].text
                                                    runner_up_candidate_criminal_history = runner_up_candidate.find_elements_by_tag_name('td')[10].text
                                                    runner_up_candidate_vote_percentage = runner_up_candidate.find_elements_by_tag_name('td')[12].text
                                                    writer.writerow([zila, vikas_khand, gram_panchayat_name, aarakshan, runner_up_candidate_name, runner_up_candidate_father_husband_name, runner_up_candidate_gender, runner_up_candidate_age, runner_up_candidate_education, runner_up_candidate_caste, runner_up_candidate_vote_percentage, 'runner-up'])
                                                    break
                                                except:
                                                    print('nahi hua bhai')
                                            
                                        break
                                    except UnexpectedAlertPresentException as e:
                                        print('this shit again')
                                        driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[3]/div[3]/div[1]/table/tbody/tr[1]/td[3]/select/option[2]').click()
                            

            INDEX += 1
            break



f.close()


