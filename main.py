
"""

Data Collection and Processing Project from "Law.com" Using Selenium

This project consists of several stages:
1. Opening the browser and accessing the law firms' page.
2. Loading more data.
3. Collecting detailed data for each company.
4. Processing and preparing the data.
5. Uploading the data to an external database via Sheety.

Use this code to collect data from Law.com and upload it to an external database.

Written by: MOSTAFA IBRAHIM

"""
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
"""

مشروع جمع ومعالجة البيانات من موقع "Law.com" باستخدام Selenium

هذا المشروع يتكون من عدة مراحل:
1. فتح المتصفح والوصول إلى صفحة شركات المحاماة.
2. تحميل المزيد من البيانات.
3. جمع البيانات التفصيلية لكل شركة.
4. معالجة البيانات وتجهيزها.
5. رفع البيانات إلى قاعدة بيانات عبر Sheety.

استخدم هذا الكود لجمع البيانات من موقع Law.com وتحميلها إلى قاعدة بيانات خارجية.

كتابة هذا المشروع بواسطة: MOSTAFA IBRAHIM


"""
# ---------------------------------------------------------------------------------------------------

from selenium import webdriver
from prepere_data import PrepereData
from get_data import GettingData
from procces_data import Process
from upload_data import UploadData

# إعدادات المتصفح: تفعيل وضع عدم إغلاق المتصفح بعد انتهاء السكربت.
# Browser settings: Enabling the 'detach' option so that the browser doesn't close after script execution.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# فتح متصفح Chrome.
# Opening Chrome browser.
driver = webdriver.Chrome(options=chrome_options)

# الوصول إلى صفحة الشركات على موقع "Law.com"
# Accessing the law firms' page on "Law.com".
driver.get('https://www.law.com/law-firms/')

# إعداد الكائن لتحميل المزيد من البيانات من الصفحة.
# Preparing the object to load more data from the page.
prepere = PrepereData(driver)

# تحميل المزيد من البيانات (من خلال النقر على زر "تحميل المزيد").
# Loading more data by clicking on the "Load more" button.
prepere.load_more()

# جمع الروابط الخاصة بشركات المحاماة.
# Collecting the URLs of law firms.
links = prepere.compnaies_info()

# استخراج البيانات التفصيلية لكل شركة باستخدام الكائن "GettingData".
# Extracting detailed data for each company using the "GettingData" object.
data = GettingData(driver=driver, links=links)

# جمع البيانات من الصفحات الخاصة بكل شركة.
# Gathering the data from each company's page.
data.get_data()

# معالجة البيانات المجمعة.
# Processing the collected data.
procces = Process(companies_urls=data.urls,
                  companies_names=data.names,
                  companies_description=data.description,
                  companies_rank=data.ranking,
                  companies_overview=data.overview,
                  companies_urls_on_low_website=links
                  )

# تمرير البيانات للمعالجة النهائية.
# Passing the data for final processing.
procced_data = procces.process_data()

# رفع البيانات المعالجة إلى قاعدة بيانات عبر Sheety.
# Uploading the processed data to a database via Sheety.
upload = UploadData(ready_data=procced_data)
upload.upload_data()






