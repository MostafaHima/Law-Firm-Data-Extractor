import requests
from dotenv import load_dotenv
import os
load_dotenv()
class UploadData:
    def __init__(self, ready_data):
        # Initializing the class with the URL for Sheety API and the ready data to be uploaded
        # تهيئة الكلاس مع الرابط الخاص بـ Sheety API والبيانات الجاهزة التي سيتم تحميلها
        self.url = os.environ["URL"]
        self.read_data = ready_data

    def upload_data(self):
        headers = {
            "Authorization": f"Bearer {os.environ["API_KEY"]}"
        }

        # Loop through each data in the ready data list
        # التكرار عبر كل عنصر في البيانات الجاهزة
        for data in self.read_data:
            # Flatten the nested data into a structure suitable for API upload
            # تحويل البيانات المتداخلة إلى هيكل مناسب للتحميل عبر API
            flat_data = {
                "name": data["Name"],  # Extract the name of the firm
                "description": data['Description'],  # Extract the description of the firm
                "website": data['URL'],  # Extract the URL (website) of the firm
                "globalRank": data['Ranking']["2024"]['Global 200'].split("#")[-1],
                # Extract the global ranking for 2024

                # Extract various data points related to the firm's overview
                # استخراج بيانات مختلفة تتعلق بنظرة عامة عن الشركة
                "totalOffices": data['Overview']['Total Offices:'],
                "totalHeadcount": data['Overview']['Total Headcount*:'],
                "equityPartners": data['Overview']['Equity Partners:'],
                "nonEquityPartners": data['Overview']['Non Equity Partners:'],
                "associates": data['Overview']['Associates:'],
                "totalRevenue": data['Overview']['Total Revenue:'],
                "profitPerEquityPartner": data['Overview']['Profit Per Equity Partner:'],
                "revenuePerLawyer": data['Overview']['Revenue Per Lawyer:'],

                # Extract global ranking for the previous years (2022, 2023, 2024)
                # استخراج الترتيب العالمي للسنوات السابقة (2022، 2023، 2024)
                "global200/2022": data['Ranking']['2022']['Global 200'].split("#")[-1],
                "global200/2023": data['Ranking']['2023']['Global 200'].split("#")[-1],
                "global200/2024": data['Ranking']['2024']['Global 200'].split("#")[-1],

                # Extract AM Law 200 rankings for the years 2022, 2023, and 2024
                # استخراج ترتيب AM Law 200 للسنوات 2022، 2023، و2024
                "amLaw200/2022": data['Ranking']['2022']['Am Law 200'].split("#")[-1],
                "amLaw200/2023": data['Ranking']['2023']['Am Law 200'].split("#")[-1],
                "amLaw200/2024": data['Ranking']['2024']['Am Law 200'].split("#")[-1],

                # Extract UK Top 50 rankings for the years 2022, 2023, and 2024
                # استخراج ترتيب UK Top 50 للسنوات 2022، 2023، و2024
                "ukTop50/2022": data['Ranking']['2022']['UK Top 50'].split("#")[-1],
                "ukTop50/2023": data['Ranking']['2023']['UK Top 50'].split("#")[-1],
                "ukTop50/2024": data['Ranking']['2024']['UK Top 50'].split("#")[-1],

                # Extract NLJ 500 rankings for the years 2022, 2023, and 2024
                # استخراج ترتيب NLJ 500 للسنوات 2022، 2023، و2024
                "nlj500/2022": data['Ranking']['2022']['NLJ 500'].split("#")[-1],
                "nlj500/2023": data['Ranking']['2023']['NLJ 500'].split("#")[-1],
                "nlj500/2024": data['Ranking']['2024']['NLJ 500'].split("#")[-1],

                # Extract the URL on the law website
                # استخراج الرابط على موقع القانون
                "linkOnLawWebsite": data["Url_on_low_website"]
            }

            # Send the flattened data to Sheety API via a POST request
            # إرسال البيانات المُسطحة إلى Sheety API عبر طلب POST
            response = requests.post(self.url, json={"lawfirm": flat_data})

            # Print the API response text for debugging and verification
            # طباعة استجابة API للتحقق من البيانات
            print(response.text)
            print()


