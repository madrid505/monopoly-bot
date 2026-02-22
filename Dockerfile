# استخدم صورة Python الرسمية
FROM python:3.11-slim

# اعمل مجلد للتطبيق
WORKDIR /app

# انسخ كل الملفات للمجلد
COPY . /app

# ثبت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# شغل البوت عند بدء الحاوية
CMD ["python", "bot.py"]
