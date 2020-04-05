from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("user-agent=[Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/74.0]")
chrome_options.add_argument("--no-sandbox")

def getNewMap(Units):
    driver = webdriver.Chrome(executable_path=r'./chromedriver',options=chrome_options)
    driver.get(f'https://pamyat-naroda.ru/warunit/{Units}/')
    time.sleep(5)
    ymap = driver.find_element_by_css_selector('ymaps[class="ymaps-2-1-76-inner-panes"]')
    a = ymap.find_element_by_css_selector('ymaps[class="ymaps-2-1-76-ground-pane"]')
    b = ymap.find_element_by_css_selector('ymaps[class="ymaps-2-1-76-areas-pane"]')
    c = ymap.find_element_by_css_selector('ymaps[class="ymaps-2-1-76-places-pane"]')
    alll = f"""<div><ymaps class="ymaps-2-1-76-ground-pane" style="position: sticky;">{a.get_attribute('innerHTML')}</ymaps><ymaps class="ymaps-2-1-76-areas-pane" style="position: sticky;">{b.get_attribute('innerHTML')}</ymaps><ymaps class="ymaps-2-1-76-places-pane" style="position: sticky;">{c.get_attribute('innerHTML')}</ymaps></div>"""
    driver.quit()
    return(alll)