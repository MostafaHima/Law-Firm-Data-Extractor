import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PrepereData:
    def __init__(self, driver):
        # Initializing the driver, index and setting up empty lists for company info and links
        # تهيئة المتغيرات مثل الفهرس والقوائم الفارغة لمعلومات الشركات والروابط
        self.driver = driver
        self.index = 1
        self.info = []
        self.links = []

    def load_more(self):
        # This function is used to keep loading more content as long as the index is less than 30
        # هذه الدالة تُستخدم لتحميل المزيد من المحتوى طالما أن الفهرس أقل من 30
        while self.index < 30:

            try:
                # Trying to find the "Load More" button and click it
                # محاولة العثور على زر "تحميل المزيد" والنقر عليه
                load_more = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, f"loadmore{self.index}"))
                )

                # Scroll the "Load More" button into view
                # تمرير زر "تحميل المزيد" إلى العرض
                self.driver.execute_script("arguments[0].scrollIntoView(true);", load_more)

                # Wait for the "Load More" button to be clickable
                # الانتظار حتى يصبح زر "تحميل المزيد" قابلاً للنقر
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, f"loadmore{self.index}"))
                )

                # Click the "Load More" button
                # النقر على زر "تحميل المزيد"
                load_more.click()
                time.sleep(2.5)  # Wait for the page to load more content
                print(f"Load Number: {self.index}")

            except Exception as e:
                # If no "Load More" button is found or the pages have ended, print a message
                # إذا لم يتم العثور على زر "تحميل المزيد" أو انتهت الصفحات، يتم طباعة رسالة
                print(f"لم يتم العثور على زر تحميل المزيد {self.index} أو انتهت الصفحات")

            self.index += 1

    def compnaies_info(self):
        # This function extracts company links from the page and stores them in the 'links' list
        # هذه الدالة تستخرج روابط الشركات من الصفحة وتخزنها في قائمة "الروابط"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".hp-events")))

        # Find all elements with the CSS selector '.hp-events', which contains the company info
        # العثور على جميع العناصر باستخدام المحدد CSS ".hp-events" الذي يحتوي على معلومات الشركات
        self.info = self.driver.find_elements(By.CSS_SELECTOR, ".hp-events")
        print(len(self.info))  # Print the number of companies found on the page

        for company in self.info:
            # For each company, find the list of links in the element
            # لكل شركة، نقوم بالبحث عن روابط العناصر في العنصر
            company_link_element = WebDriverWait(company, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li"))
            )

            # Loop through all found links and extract their href attribute
            # التكرار عبر جميع الروابط المستخرجة وأخذ السمة "href" الخاصة بها
            for get_links in company_link_element:
                links = WebDriverWait(get_links, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "p a"))
                )

                # Add the link to the list of company links
                # إضافة الرابط إلى قائمة الروابط الخاصة بالشركة
                company_link = links.get_attribute("href")
                self.links.append(company_link)

        return self.links  # Return the list of links
        # إرجاع قائمة الروابط




