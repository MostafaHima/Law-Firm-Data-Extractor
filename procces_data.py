class Process:
    def __init__(self, companies_urls, companies_names, companies_description, companies_rank, companies_overview,
                 companies_urls_on_low_website):
        # Initializing the class with data attributes for URLs, names, descriptions, rankings, and overviews
        # تهيئة الكلاس مع خصائص البيانات مثل الروابط، الأسماء، الأوصاف، التقييمات، والنظرة العامة
        self.companies_urls = companies_urls
        self.companies_names = companies_names
        self.companies_description = companies_description
        self.companies_rank = companies_rank
        self.companies_overview = companies_overview
        self.companies_urls_on_low_website = companies_urls_on_low_website
        self.all_data = []  # This will hold the processed data

    def process_data(self):
        # Find the shortest length among all input lists to avoid index errors during iteration
        # العثور على أقصر طول بين جميع القوائم المدخلة لتجنب أخطاء الفهرسة أثناء التكرار
        min_length = min(len(self.companies_urls_on_low_website), len(self.companies_names),
                         len(self.companies_description), len(self.companies_rank), len(self.companies_overview))

        # Check if all lists are of the same length, otherwise print a warning
        # التحقق من أن جميع القوائم بنفس الطول، وإلا يتم طباعة تحذير
        if not (len(self.companies_urls_on_low_website) == len(self.companies_names) ==
                len(self.companies_description) == len(self.companies_rank) == len(self.companies_overview)):
            print("Warning: Lists come in different lengths. Even the shortest list data will be processed.")

        # Trim the lists to the shortest length to prevent out-of-bounds access
        # تقليص القوائم لتناسب الطول الأقصر لمنع الوصول إلى فهرس غير صالح
        self.companies_urls_on_low_website = self.companies_urls_on_low_website[:min_length]
        self.companies_names = self.companies_names[:min_length]
        self.companies_description = self.companies_description[:min_length]
        self.companies_rank = self.companies_rank[:min_length]
        self.companies_overview = self.companies_overview[:min_length]

        # Loop through the data and create dictionaries to store the firm data
        # التكرار عبر البيانات وإنشاء قواميس لتخزين بيانات الشركات
        for i in range(len(self.companies_names)):
            try:
                # If the description is empty, use a default value
                # إذا كانت الوصف فارغًا، استخدم قيمة افتراضية
                description = self.companies_description[i] if self.companies_description[
                    i] else "Description not available"

                # Create a dictionary to store the firm's information
                # إنشاء قاموس لتخزين معلومات الشركة
                firm_data = {
                    "Name": self.companies_names[i],  # Firm name
                    "URL": self.companies_urls[i],  # Firm URL
                    "Description": description,  # Firm description
                    "Ranking": {},  # Placeholder for rankings
                    "Overview": self.companies_overview[i],  # Firm overview
                    "Url_on_low_website": self.companies_urls_on_low_website[i]  # URL from a law website
                }

                # Create a dictionary for rankings, grouped by year
                # إنشاء قاموس للتقييمات، مرتبة حسب السنة
                rankings_by_year = {}
                for category, year_data in self.companies_rank[i].items():
                    for entry in year_data:
                        for year, rank in entry.items():
                            if year not in rankings_by_year:
                                rankings_by_year[year] = {}  # Create an entry for each year
                            rankings_by_year[year][category] = rank  # Assign the rank to the year and category

                # Add the rankings to the firm_data dictionary
                # إضافة التقييمات إلى قاموس firm_data
                firm_data["Ranking"] = rankings_by_year
                self.all_data.append(firm_data)  # Append the firm data to the all_data list

                # Print the success message for each company processed
                # طباعة رسالة النجاح لكل شركة تمت معالجتها
                print(f"The company ( {i + 1} of {len(self.companies_names)} ) has been added successfully.")
            except IndexError as e:
                # Catch any errors that occur if the index is out of bounds
                # التقاط أي أخطاء تحدث إذا كان الفهرس خارج النطاق
                print(f"An error occurred at index {i}: {e}")
                break

        # Print the length of the final data list and return the processed data
        # طباعة طول قائمة البيانات النهائية وإرجاع البيانات المعالجة
        print(f"Length of final list: {len(self.all_data)}")
        return self.all_data
