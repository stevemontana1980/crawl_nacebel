from selenium import webdriver
from selenium.common.exceptions import WebDriverException

driver = webdriver.Firefox()
driver.implicitly_wait(10)

f = open('Missing_NACE.csv', 'r')
for row in f:
    driver.get("https://cri.nbb.be/bc9/web/catalog?")
    element = driver.find_element_by_name("page_searchForm:j_id3:generated_number_2_component")
    element.send_keys(str.strip(row))
    search = driver.find_element_by_id("page_searchForm:actions:0:button")
    search.click()
    try:
        nace = driver.find_element_by_xpath("//table[contains(@class, 'company-details')]/tbody/tr[last()]/td[2]")
        element_text = nace.text
        with open('output.csv', 'a') as g:
            g.write(str.strip(row) + '\t' + str.strip(element_text) + '\n')
            g.close()

    except WebDriverException:
        with open('output.csv', 'a') as g:
            g.write(str.strip(row) + '\t' + 'FAILED' + '\n')
            g.close()