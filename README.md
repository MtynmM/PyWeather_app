PyWeather App
A clean and modern desktop weather application built with Python, featuring a responsive UI and real-time data fetching. This project demonstrates a solid understanding of software architecture and API integration.

<details>
<summary><b>(ترجمه فارسی)</b></summary>

یک اپلیکیشن دسکتاپ ساده و مدرن برای نمایش اطلاعات آب و هوا که با پایتون ساخته شده است. این برنامه دارای رابط کاربری واکنش‌گرا و قابلیت دریافت داده‌های لحظه‌ای است. این پروژه نشان‌دهنده درک قوی از معماری نرم‌افزار و یکپارچه‌سازی API است.

</details>

✨ Features
Real-time Weather Data: Fetches and displays current weather conditions for any specified location.

Modern GUI: Built with ttkbootstrap for a beautiful, themeable user interface (defaulting to "superhero" dark theme).

Clean Architecture: Strictly follows the MVC (Model-View-Controller) pattern to ensure separation of concerns and maintainability.

Secure API Key Management: Utilizes environment variables (.env file) to securely manage the API key, keeping it out of version control.

Robust Error Handling: Gracefully handles invalid user inputs (e.g., unknown city) and network-related issues.

<details>
<summary><b>(ویژگی‌ها به فارسی)</b></summary>

داده‌های لحظه‌ای آب و هوا: دریافت و نمایش شرایط آب و هوایی لحظه‌ای برای هر مکان مشخص شده.

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

🚀 Getting Started
To run this project locally, follow these steps:

<details>
<summary><b>(راهنمای اجرا به فارسی)</b></summary>

برای اجرای این پروژه به صورت محلی، مراحل زیر را دنبال کنید:

</details>

Clone the repository:

git clone https://github.com/[your-username]/PyWeather_app.git
cd PyWeather_app

Set up the virtual environment:

python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Create the .env file:
Create a file named .env in the project root and add your API key:

WEATHER_API_KEY="your_api_key_from_weatherapi.com"

Run the application:

python -m app.main

acknowledgements
This application uses weather data provided by WeatherAPI.com.

<details>
<summary><b>(قدردانی به فارسی)</b></summary>

این برنامه از داده‌های آب و هوا که توسط WeatherAPI.com ارائه شده، استفاده می‌کند.

</details>

Developed by [Matin Mohammadi]