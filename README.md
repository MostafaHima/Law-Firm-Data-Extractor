# **LawFirmScraper**

**LawFirmScraper** is a web scraping project that gathers detailed information about law firms from the "Law.com" website. The project uses **Selenium** to automate the process of collecting data from multiple pages and stores it in an organized format.

## **Features**

- **Web scraping**: Collect data about law firms such as names, ratings, descriptions, and more.
- **Data processing**: Process the collected data to extract relevant details.
- **Data uploading**: Upload the processed data to an external database (like Sheety).
- **Browser automation**: Uses Selenium and ChromeDriver to automate browser interaction.

## **Technologies Used**

- **Selenium**: For extracting data from web pages.
- **Python**: The primary programming language for the project.
- **Sheety API**: For uploading the data to an external database.
- **ChromeDriver**: To automate interaction with the Chrome browser.

## **Project Setup**

### 1. **Install Dependencies**

First, clone the project:

```bash
git clone https://github.com/your_username/your_project_name.git
cd your_project_name

python -m venv venv
source venv/bin/activate  # For Linux/Mac systems
venv\Scripts\activate     # For Windows systems
pip install -r requirements.txt
API_KEY=your_api_key_here
SHEET_URL=your_sheety_url_here
python main.py

LawFirmScraper/
│
├── .gitignore             # .gitignore file (includes .env and other unnecessary files)
├── .env                   # File for storing environment variables like API keys
├── .idea/                 # IDE project files (can be ignored)
├── __pycache__/           # Python bytecode files
├── get_data.py            # Script to extract data from law firm pages
├── main.py                # Main script to run the project
├── prepere_data.py        # Script to prepare the data and load more pages
├── procces_data.py        # Script to process and clean the data
├── upload_data.py         # Script to upload the processed data
├── requirements.txt       # List of dependencies for the project
└── README.md              # Project documentation (this file)
```


# How It Works
1. Extraction: The project first navigates to the law firm listing page on Law.com and clicks the "Load More" button to load all available firms.
2. Data Extraction: After the page is fully loaded, the script collects the law firm links and other important details for each firm.
3. Data Processing: The collected data is cleaned and structured to be ready for uploading.
4. Data Uploading: The processed data is uploaded to an external database using the Sheety API.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
##
##

##


# **LawFirmScraper**

**LawFirmScraper** هو مشروع لاستخراج البيانات من الإنترنت (ويب سكرابينغ) يجمع معلومات تفصيلية عن شركات المحاماة من موقع "Law.com". يستخدم المشروع **Selenium** لأتمتة عملية جمع البيانات من عدة صفحات وتخزينها في تنسيق منظم.

## **المميزات**

- **استخراج البيانات من الويب**: جمع بيانات عن شركات المحاماة مثل الأسماء، التقييمات، الأوصاف، والمزيد.
- **معالجة البيانات**: معالجة البيانات المجمعة لاستخراج التفاصيل ذات الصلة.
- **رفع البيانات**: رفع البيانات المعالجة إلى قاعدة بيانات خارجية (مثل Sheety).
- **أتمتة المتصفح**: يستخدم Selenium وChromeDriver لأتمتة التفاعل مع المتصفح.

## **التقنيات المستخدمة**

- **Selenium**: لاستخراج البيانات من صفحات الويب.
- **Python**: اللغة الأساسية للمشروع.
- **Sheety API**: لرفع البيانات إلى قاعدة بيانات خارجية.
- **ChromeDriver**: لأتمتة تفاعل المتصفح Chrome.

## **إعداد المشروع**

### 1. **تثبيت الاعتمادات**

أولاً، قم باستنساخ المشروع:

```bash
git clone https://github.com/اسم_المستخدم/اسم_المشروع.git
cd اسم_المشروع

python -m venv venv
source venv/bin/activate  # في حالة نظام Linux/Mac
venv\Scripts\activate     # في حالة نظام Windows
pip install -r requirements.txt
API_KEY=your_api_key_here
SHEET_URL=your_sheety_url_here
python main.py


LawFirmScraper/
│
├── .gitignore             # ملف .gitignore (يحتوي على .env وملفات أخرى غير ضرورية)
├── .env                   # ملف لتخزين المتغيرات البيئية مثل مفاتيح API
├── .idea/                 # ملفات مشروع IDE (يمكن تجاهلها)
├── __pycache__/           # ملفات Python البايت
├── get_data.py            # سكربت لاستخراج البيانات من صفحات شركات المحاماة
├── main.py                # السكربت الرئيسي لتشغيل المشروع
├── prepere_data.py        # سكربت لإعداد البيانات وتحميل المزيد من الصفحات
├── procces_data.py        # سكربت لمعالجة وتنظيف البيانات
├── upload_data.py         # سكربت لرفع البيانات المعالجة
├── requirements.txt       # قائمة بالاعتمادات للمشروع
└── README.md              # وثائق المشروع (هذا الملف)
```

## **كيفية العمل**
1. الاستخراج: يقوم المشروع أولاً بالانتقال إلى صفحة شركات المحاماة في Law.com ويضغط على زر "تحميل المزيد" لتحميل جميع الشركات المتاحة.
2. استخراج البيانات: بعد تحميل الصفحة بالكامل، يقوم السكربت بجمع روابط الشركات والتفاصيل الأخرى المهمة لكل شركة.
3. معالجة البيانات: يتم تنظيف البيانات المجمعة وهيكلتها بحيث تكون جاهزة للرفع.
4. رفع البيانات: يتم رفع البيانات المعالجة إلى قاعدة بيانات خارجية باستخدام Sheety API.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

