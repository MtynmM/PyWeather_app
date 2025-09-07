PyWeather App
A clean and modern desktop weather application built with Python, featuring a responsive UI and real-time data fetching. This project demonstrates a solid understanding of software architecture and API integration.

<details>
<summary><b>(ترجمه فارسی)</b></summary>

یک اپلیکیشن دسکتاپ ساده و مدرن برای نمایش اطلاعات آب و هوا که با پایتون ساخته شده است. این برنامه دارای رابط کاربری واکنش‌گرا و قابلیت دریافت داده‌های لحظه‌ای است. این پروژه نشان‌دهنده درک قوی از معماری نرم‌افزار و یکپارچه‌سازی API است.

</details>

✨ Features
Real-time Weather Data: Fetches and displays current weather conditions for any specified location.

Modern GUI: Built with ttkbootstrap for a beautiful, themeable user interface (defaulting to "superhero" dark theme).

Dynamic weather icons based on the current condition.

Clean Architecture: Strictly follows the MVC (Model-View-Controller) pattern to ensure separation of concerns and maintainability.

Secure API Key Management: Utilizes environment variables (.env file) to securely manage the API key, keeping it out of version control.

Robust Error Handling: Gracefully handles invalid user inputs (e.g., unknown city) and network-related issues.

<details>
<summary><b>(ویژگی‌ها به فارسی)</b></summary>

داده‌های لحظه‌ای آب و هوا: دریافت و نمایش شرایط آب و هوایی لحظه‌ای برای هر مکان مشخص شده.

نمایش آیکون‌های پویای آب و هوا بر اساس وضعیت فعلی

رابط کاربری گرافیکی مدرن: ساخته شده با ttkbootstrap برای یک رابط کاربری زیبا و قابل تم‌بندی (با تم پیش‌فرض "superhero").

معماری تمیز: پیروی دقیق از الگوی MVC (Model-View-Controller) برای تضمین جداسازی مسئولیت‌ها و قابلیت نگهداری کد.

مدیریت امن کلید API: استفاده از متغیرهای محیطی (فایل .env) برای مدیریت امن کلید API و جلوگیری از ثبت آن در کنترل نسخه.

مدیریت خطای قوی: مدیریت هوشمند خطاهای ورودی کاربر (مانند شهر نامعتبر) و مشکلات مربوط به شبکه.

</details>

🛠️ Tech Stack
Language: Python 3

GUI Framework: Tkinter, ttkbootstrap

API Communication: Requests

Configuration Management: python-dotenv

Version Control: Git

<details>
<summary><b>(تکنولوژی‌های استفاده شده به فارسی)</b></summary>

زبان: پایتون ۳

فریمورک رابط کاربری: Tkinter, ttkbootstrap

ارتباط با API: Requests

مدیریت تنظیمات: python-dotenv

کنترل نسخه: Git

</details>


    ## 🚀 Getting Started
To get a local copy up and running, follow these simple steps.

<details>
<summary><b>(راهنمای راه اندازی به فارسی)</b></summary>

برای راه اندازی و اجرای یک نسخه محلی از پروژه، این مراحل ساده را دنبال کنید.

</details>
### 1. Clone the Repository
```bash
git clone [https://github.com/MtynmM/PyWeather_app.git](https://github.com/MtynmM/PyWeather_app.git)
cd PyWeather_app
### 2. Set up The Virtual Environment
```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
### 3. Install Dependencies
```bash
pip install -r requirements.txt
### 4. Create The `.env` File & Add API Key (Crucial Step!)
This application requires a free API key from **WeatherAPI.com** to function.

1.  Go to [www.weatherapi.com](https://www.weatherapi.com) and sign up for a free account.
2.  After signing up, find your **API Key** on your account dashboard and copy it.
3.  In the root directory of the project, create a new file named `.env`.
4.  Open the `.env` file and add the following line, replacing `"YOUR_API_KEY_HERE"` with the key you copied:
    ```env
    WEATHER_API_KEY="YOUR_API_KEY_HERE"
    ```

<details>
<summary><b>(ترجمه فارسی: ساخت فایل .env و افزودن کلید API)</b></summary>

این برنامه برای کار کردن، به یک کلید API رایگان از **WeatherAPI.com** نیاز دارد.

1.  به وب‌سایت [www.weatherapi.com](https://www.weatherapi.com) بروید و یک حساب کاربری رایگان بسازید.
2.  پس از ثبت‌نام، **کلید API** خود را در داشبورد حساب کاربری پیدا کرده و آن را کپی کنید.
3.  در پوشه اصلی پروژه، یک فایل جدید به نام `.env` بسازید.
4.  فایل `.env` را باز کرده و خط زیر را در آن اضافه کنید. به جای `"YOUR_API_KEY_HERE"`، کلیدی که کپی کرده‌اید را قرار دهید:
    ```env
    WEATHER_API_KEY="YOUR_API_KEY_HERE"
    ```

</details>
### 5. Run the Application
```bash
python -m app.main

Developed by [Matin Mohammadi]
