
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class GettingData:
    def __init__(self, links, driver):
        self.links = links  # List of URLs to scrape data from / قائمة الروابط لاستخراج البيانات منها
        self.driver = driver  # WebDriver used for controlling the browser / السائق المستخدم للتحكم في المتصفح
        self.company_overview_element = None  # Element for company overview / عنصر النظرة العامة للشركة
        self.company_rank_element = None  # Element for company ranking / عنصر تصنيف الشركة

        # Lists to store extracted data / قوائم لتخزين البيانات المستخرجة
        self.ranking = []
        self.overview = []
        self.description = []
        self.names = []
        self.urls = []

    def get_data(self):
        # Loop through the links and extract data / حلقة لاستخراج البيانات من الروابط
        for index, page_url in enumerate(self.links, start=1):
            self.driver.get(page_url)  # Open the URL / فتح الرابط

            try:
                # Wait for the page to load completely / الانتظار لتحميل الصفحة بالكامل
                WebDriverWait(self.driver, 25).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
            except Exception:
                self.driver.refresh()  # Refresh the page if something fails / إعادة تحميل الصفحة إذا حدث خطأ
                print("Refresh Page Done.")
                WebDriverWait(self.driver, 25).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )

            time.sleep(5)

            try:
                # Extract the company name / استخراج اسم الشركة
                company_name_element = WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".block h1"))
                )
                self.names.append(company_name_element.text)  # Append name to names list / إضافة الاسم إلى قائمة الأسماء
                print(f"Company: {index}: ")
                print(f"[ Name {company_name_element.text},")
            except Exception:
                self.driver.refresh()  # Refresh if the name element is not found / إعادة تحميل الصفحة إذا لم يتم العثور على عنصر الاسم
                company_name_element = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".block h1"))
                )
                self.names.append(company_name_element.text)  # Append name again / إضافة الاسم مرة أخرى
                print(f"Company: {index}: ")
                print(f"[ Name {company_name_element.text},")

            try:
                # Extract company description / استخراج وصف الشركة
                company_description_element = WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='__layout']/div/div[7]/div/div/div[2]/article[1]/p"))
                )
                self.description.append(company_description_element.text)  # Append description to description list / إضافة الوصف إلى قائمة الأوصاف
                print(f"Descrption Company {company_name_element.text} ")
            except Exception:
                print(f"Company {company_name_element.text} doesn't have description.")  # If description is not available / إذا لم يتوفر الوصف
                pass

            # Extract company overview / استخراج نظرة عامة عن الشركة
            self.company_overview_element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".overview"))
            )
            self.get_overview()

            # Extract company ranking / استخراج تصنيف الشركة
            self.company_rank_element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='__layout']/div/div[7]/div/div/div[2]/article[2]"))
            )
            self.get_ranking()

            try:
                # Extract company URL / استخراج رابط الشركة
                company_url_element = WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id=\"__layout\"]/div/div[7]/div/div/div[2]/article[1]/a"))
                )

                company_url = company_url_element.get_attribute("href")
                self.urls.append(company_url)  # Append URL to urls list / إضافة الرابط إلى قائمة الروابط
            except Exception:
                print(f"Company: {company_name_element.text} doesn't have URL")  # If URL is not available / إذا لم يتوفر الرابط
                pass
            print(f"Url Company: {company_name_element.text} Done. ]")
            print("\n-------------------------------------------------------------------\n")

    def get_overview(self):
        # Extract the company overview details / استخراج تفاصيل نظرة الشركة العامة
        overview_elements = self.company_overview_element.find_elements(By.TAG_NAME, "li")

        company_overview_dict = {}

        for i in range(len(overview_elements)):
            overview_data = overview_elements[i].text.split("\n")

            if len(overview_data) == 2:
                key = overview_data[0].strip()  # Key of the overview item / المفتاح
                value = overview_data[1].strip()  # Value of the overview item / القيمة
                company_overview_dict[key] = value

        # Append overview data to the overview list / إضافة البيانات إلى قائمة النظرة العامة
        self.overview.append(company_overview_dict)
        print("Overview Added")

        return self.overview

    def get_ranking(self):
        # Extract the company ranking details / استخراج تفاصيل التصنيف
        ranking_elements = self.company_rank_element.find_elements(By.TAG_NAME, "div")
        ranking_len = len(ranking_elements)

        rankings_dict = {}

        for i in range(ranking_len):
            rank_data = ranking_elements[i].text.split("\n")

            key = rank_data[0]

            values = []
            for j in range(1, len(rank_data), 2):
                year = rank_data[j]
                rank = rank_data[j + 1]
                values.append({year: rank})

            rankings_dict[key] = values

        # Append ranking data to the ranking list / إضافة بيانات التصنيف إلى قائمة التصنيفات
        self.ranking.append(rankings_dict)
        print("Ranking Added")
        return self.ranking







