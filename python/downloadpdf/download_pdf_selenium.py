from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
import shutil

def download_pdf_by_webdriver(download_dir, url, file_name):
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs',  {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
        }
    )

    browser = webdriver.Chrome(options = chrome_options)
    browser.get(url)

    latest_filename = max([download_dir + "/" + f for f in os.listdir(download_dir)],key=os.path.getctime)
    shutil.move(latest_filename, os.path.join(download_dir, file_name + ".pdf"))

if __name__ == '__main__':
    download_dir = '/Users/jianbfan/Desktop/github/study/python/downloadpdf/acm2018'
    url = 'https://dl.acm.org/doi/pdf/10.1145/3173574.3173593'
    file_name = 'When David Meets Goliath: Combining Smartwatches with a Large Vertical Display for Visual Data Exploration'
    download_pdf_by_webdriver(download_dir, url, file_name)
