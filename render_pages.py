import sys, os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import arabic_reshaper
from bidi.algorithm import get_display
from generate_hamsyar_pdf import *

def build_pdf(filename="HamsYar_Biochemistry_Night_Before_Exam.pdf"):
    c = canvas.Canvas(filename, pagesize=(PAGE_W, PAGE_H))
    
    # ---------------- PAGE 1: COVER ----------------
    c.saveState()
    steps = 80
    for i in range(steps):
        t = i / steps
        if t < 0.4:
            f = t / 0.4
            r = (18 + f * (11 - 18)) / 255
            g = (161 + f * (98 - 161)) / 255
            b = (106 + f * (92 - 106)) / 255
        elif t < 0.75:
            f = (t - 0.4) / 0.35
            r = (11 + f * (42 - 11)) / 255
            g = (98 + f * (63 - 98)) / 255
            b = (92 + f * (137 - 92)) / 255
        else:
            f = (t - 0.75) / 0.25
            r = (42 + f * (79 - 42)) / 255
            g = (63 + f * (58 - 63)) / 255
            b = (137 + f * (182 - 137)) / 255
        c.setFillColorRGB(r, g, b)
        c.rect(0, PAGE_H - (i + 1) * (PAGE_H / steps), PAGE_W, (PAGE_H / steps) + 1, fill=1, stroke=0)

    c.setFillColor(C_WHITE)
    c.setFont('Vazirmatn-Bold', 12)
    c.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 120, fa("مجموعه جزوات شب امتحانی"))
    c.setFont('Vazirmatn-ExtraBold', 28.5)
    c.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 165, fa("جزوه‌ی شب‌امتحانی"))
    c.setFillColor(C_HIGHLIGHT)
    c.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 208, fa("بیوشیمی پزشکی"))
    c.setFillColor(C_WHITE)
    c.setFont('Vazirmatn-Medium', 12.0)
    c.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 250, fa("خلاصه جامع، نموداری و طبقه‌بندی‌شده از صفر تا صد"))
    c.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 270, fa("ویژه جمع‌بندی سریع آزمون‌های پایان‌ترم و جامع علوم پایه پزشکی"))

    pills = ["۱۲ فصل کامل آموزشی", "نکات کلیدی و دام‌های تستی", "تشبیه‌های مفهومی و بالینی", "جداول مقایسه‌ای و فرمول‌ها"]
    pill_y = PAGE_H - 330
    for idx, p_text in enumerate(pills):
        px = MARGIN_X + (idx % 2) * 270
        py = pill_y - (idx // 2) * 40
        c.setFillColorRGB(1, 1, 1, 0.15)
        c.roundRect(px, py, 250, 28, 14, fill=1, stroke=0)
        c.setFillColor(C_WHITE)
        c.setFont('Vazirmatn-Bold', 9.5)
        c.drawRightString(px + 235, py + 8, fa(f"✦  {p_text}"))

    c.setFont('Vazirmatn-Regular', 9.0)
    c.setFillColorRGB(0.85, 0.9, 0.95)
    c.drawRightString(PAGE_W - MARGIN_X, 80, fa("منطبق بر مراجع رسمی بیوشیمی پزشکی (Lehninger & Harper)"))
    c.drawRightString(PAGE_W - MARGIN_X, 60, fa("طراحی مهندسی‌شده با سیستم آموزشی HamsYar • پاییز ۱۴۰۳"))
    c.restoreState()
    c.showPage()

    # ---------------- PAGE 2: TOC ----------------
    c.saveState()
    c.setFont('Vazirmatn-ExtraBold', 18.0)
    c.setFillColor(C_BRAND_DARK)
    c.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 50, fa("فهرست سرفصل‌های جزوه"))
    c.setFont('Vazirmatn-Regular', 9.0)
    c.setFillColor(C_TEXT_MUTED)
    c.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 68, fa("راهنمای دسترسی سریع به ۱۲ فصل آموزشی، مباحث پایه‌ای و جمع‌بندی نهایی"))

    cards = [
        ("فصل اول", "شناخت بیوشیمی و سازمان‌یابی سلولی", "ص ۴"),
        ("فصل دوم", "آب، pH و سیستم‌های بافری فیزیولوژیک", "ص ۷"),
        ("فصل سوم", "کربوهیدرات‌ها ۱: ساختار و ایزومری", "ص ۱۰"),
        ("فصل چهارم", "کربوهیدرات‌ها ۲: واکنش‌ها و پلی‌ساکاریدها", "ص ۱۳"),
        ("فصل پنجم", "اسیدهای آمینه و خواص یونی", "ص ۱۶"),
        ("فصل ششم", "سطوح ساختاری پروتئین‌ها و واسرشتگی", "ص ۱۹"),
        ("فصل هفتم", "هموپروتئین‌ها، میوگلوبین و هموگلوبین", "ص ۲۲"),
        ("فصل هشتم", "شیمی و ساختار اسیدهای نوکلئیک", "ص ۲۵"),
        ("فصل نهم", "سازوکار و آنزیم‌های همانندسازی DNA", "ص ۲۸"),
        ("فصل دهم", "شیمی، ساختار و طبقه‌بندی لیپیدها", "ص ۳۱"),
        ("فصل یازدهم", "آنزیم‌ها و سینتیک کاتالیز زیستی", "ص ۳۴"),
        ("فصل دوازدهم", "ویتامین‌های محلول در چربی و آب", "ص ۳۷"),
        ("جمع‌بندی ۱", "کل درس بیوشیمی در یک نگاه مقایسه‌ای", "ص ۳۹"),
        ("جمع‌بندی ۲", "کلید طلایی اعداد، ثابت‌ها و خودآزمایی", "ص ۴۰")
    ]
    card_w, card_h = 255.0, 75.0
    start_y = PAGE_H - 100
    for idx, (c_tag, c_title, c_page) in enumerate(cards):
        col, row = idx % 2, idx // 2
        cx = MARGIN_X + (1 - col) * (card_w + 18)
        cy = start_y - (row + 1) * (card_h + 16)
        c.setFillColor(C_SURFACE)
        c.setStrokeColor(C_LINE)
        c.setLineWidth(0.75)
        c.roundRect(cx, cy, card_w, card_h, 6, fill=1, stroke=1)
        c.setFillColor(C_BRAND)
        c.roundRect(cx + card_w - 4, cy + 12, 4, card_h - 24, 2, fill=1, stroke=0)
        c.setFont('Vazirmatn-Bold', 8.8)
        c.setFillColor(C_BRAND_DARK)
        c.drawRightString(cx + card_w - 14, cy + card_h - 22, fa(c_tag))
        c.setFont('Vazirmatn-Bold', 8.5)
        c.setFillColor(C_BRAND)
        c.drawString(cx + 12, cy + card_h - 22, fa(c_page))
        c.setFont('Vazirmatn-Medium', 9.2)
        c.setFillColor(C_TEXT_STRONG)
        c.drawRightString(cx + card_w - 14, cy + card_h - 44, fa(c_title))
    c.restoreState()
    c.showPage()

    # ---------------- PAGE 3: GUIDE ----------------
    c.saveState()
    c.setFont('Vazirmatn-ExtraBold', 18.0)
    c.setFillColor(C_BRAND_DARK)
    c.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 50, fa("راهنمای بصری کادرها و نمادها"))
    c.setFont('Vazirmatn-Regular', 9.0)
    c.setFillColor(C_TEXT_MUTED)
    c.drawRightString(PAGE_W - MARGIN_X, PAGE_H - 68, fa("آشنایی با ساختار روان‌شناختی رنگ‌ها و جعبه‌های آموزشی در سیستم مطالعه شب امتحان"))
    cur_y = PAGE_H - 90
    cur_y = draw_lead(c, cur_y, [
        "این جزوه بر اساس اصول تصویرسازی ذهنی و یادگیری تقویت‌شده تدوین گردیده است.",
        "هر کادر آموزشی حامل یک بار معنایی اختصاصی است تا در شب امتحان سریع‌ترین مرور ممکن را فراهم آورد."
    ])
    cur_y = draw_section_title(c, cur_y, "جعبه‌های چهارگانه یادگیری معنادار")
    cur_y = draw_box(c, cur_y, 'tip', 'نکته طلایی (Golden Tip)', [
        "مفاهیم پرتکرار و تست‌خیز سال‌های اخیر که یادگیری مستقیم آن‌ها نمره امتحان را تضمین می‌کند.",
        "تمرکز اصلی این کادرها بر مقایسه‌ها و تفاوت‌های دقیق بیوشیمیایی است."
    ])
    cur_y = draw_box(c, cur_y, 'analogy', 'تشبیه مفهومی (Analogy)', [
        "پیوند دادن مفاهیم پیچیده مولکولی به پدیده‌های روزمره و شهودی پیرامون ما.",
        "تثبیت درک مکانیسم‌های شیمیایی در حافظه بلندمدت بدون نیاز به حفظ طوطی‌وار."
    ])
    cur_y = draw_box(c, cur_y, 'warning', 'دام امتحانی و هشدار (Exam Trap)', [
        "اشتباهات رایج دانشجویان در آزمون‌ها و گزینه‌های گمراه‌کننده طراحان سوال.",
        "تفکیک اصطلاحات بسیار شبیه به هم و خطاهای متداول در محاسبات ریاضی و pH."
    ])
    cur_y = draw_box(c, cur_y, 'mnemonic', 'ترفند حفظی و کدگذاری (Mnemonics)', [
        "رمزگذاری‌های مخفف و عبارات جذاب برای به‌خاطرسپاری زنجیره‌های طولانی آنزیم‌ها و اسیدهای آمینه.",
        "روشی سریع برای بازیابی بدون نقص اسامی در جلسات امتحانی پرفشار."
    ])
    cur_y = draw_chapter_summary(c, cur_y, "راهنمای علائم پایانی", [
        "ستاره‌های طلایی (★) در انتهای هر فصل نشانه خلاصه نهایی و فوق‌فشرده مبحث هستند.",
        "علامت‌های تیک (✓) در چک‌لیست‌های پایانی برای خودآزمایی و ارزیابی تسلط فردی تعبیه شده‌اند."
    ])
    c.restoreState()
    c.showPage()

    print("Pages 1 to 3 drawn in builder.")
    return c

print("Module render_pages.py loaded.")
