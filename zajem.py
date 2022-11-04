from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains
import os
from selenium.webdriver.support.ui import Select


url = "https://old.chesstempo.com/chess-openings.html"
 
def save_string_to_file(text, directory, filename):
    """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
    locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
    niz "directory" prazen datoteko ustvari v trenutni mapi.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None

#zazenemo driver
driver = webdriver.Chrome('chromedriver') 
driver.get(url) 
time.sleep(3) 

#na strani izberemo 500 otvoritev na stran
select = Select(driver.find_element("xpath",'//*[@id="yui-pg0-0-rpp"]'))
select.select_by_value('500')
time.sleep(2)

#za vsako stran preberemo html tekst in jo shranimo v svojo datoteko
for i in range(4):
    if i != 0:
        stran = driver.find_element("xpath",f'//*[@id="yui-pg0-0-pages"]/a[{i}]')
        ActionChains(driver).click(stran).perform()
        time.sleep(2)
        text = driver.page_source
        save_string_to_file(text, "otvoritve", f"index_otvoritve{i}.html")
    else:
        text = driver.page_source
        save_string_to_file(text, "otvoritve", f"index_otvoritve{i}.html")

driver.close()
    