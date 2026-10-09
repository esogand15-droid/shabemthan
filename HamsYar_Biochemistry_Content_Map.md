# HamsYar – نقشه‌ی محتوای بیوشیمی (Content Map)

**وضعیت:** مرحله‌ی ۱ (تحلیل و نقشه). این نقشه از بررسی متنی **۲۴۱ صفحه‌ی PDF** (جدول `analysis/page_ledger.csv`)، خواندن ساختار و تطبیق **۶٬۶۴۴ خط MD** و نمونه‌برداری تصویری ساخته شده است.
**هشدار مهم:** **۱۱۰ صفحه** (تصویری، فونت خراب یا خالی) هنوز **خوانده‌نشده** است. موضوع این صفحات از روی هدرها و شیت‌های کوچک برآورد شده و در ستون‌های «وضعیت» و «تأیید» مشخص شده است. هیچ ادعای «پوشش کامل محتوا» در این مرحله معتبر نیست.

## ۱. منابع و هویت فایل‌ها

| منبع | فایل در پروژه | مشخصات | وضعیت |
|---|---|---|---|
| PDF اصلی (اولویت ۱) | `sources/biochem_full_241p.pdf` | ۲۴۱ صفحه؛ PDF 1.7؛ ساخته‌شده با Microsoft Word 2013 و cpdf؛ ۳۹٬۲۲۲٬۱۴۴ بایت | تأیید شد (PyMuPDF و pypdf: ۲۴۱) |
| Markdown (اولویت ۲) | `sources/biochem_full.md` | ۴۳۴٬۴۶۸ بایت؛ UTF-8؛ ۶٬۶۴۴ خط؛ ۲۴۶٬۹۴۷ نویسه؛ **بدون سرفصل `#`**؛ ۱٬۸۳۸ خط ``` مزاحم؛ ۹٬۸۰۴ نویسه‌ی Presentation Forms | تأیید شد؛ ساختار ضعیف |
| مرجع طراحی | `sources/physio_reference_hamsyar.pdf` | ۳۷ صفحه؛ جدا از محتوای بیوشیمی | تأیید شد |
| کتاب‌های Harper و Lehninger (اولویت ۳ و ۴) | — | در این مرحله بررسی نشده‌اند | **بررسی‌نشده**؛ هیچ ارجاعی داده نشده |
| منابع ذکرشده در خود جزوه | Devlin (MD خط ۳۵۶۶) و Smith (PDF صفحه‌ی ۴) | نام برده شده‌اند؛ محتوایشان بررسی نشده | **نیاز به تأیید/دسترسی** |

## ۲. وضعیت صفحات PDF (از ledger)

| کد | معنی | تعداد | صفحات | اقدام لازم |
|---|---|---|---|---|
| **T** | متن قابل‌استفاده | ۱۱۷ | ۲–۹، ۱۲–۲۱، ۳۳–۳۸، ۴۰–۵۴، ۵۶–۶۹، ۷۱–۸۰، ۸۲–۹۰، ۹۲–۹۷، ۱۰۱، ۱۲۰–۱۲۶، ۱۲۸–۱۳۶، ۱۷۸–۱۸۵، ۲۱۵–۲۲۸ | مقایسه با MD؛ ۶۵ صفحه پرچم دارد (حروف ارائه‌ای یا فاصله‌گذاری شکسته) |
| **H** | جلد یا هدر بخش (متن کوتاه) | ۱۴ | ۱، ۱۱، ۲۳، ۳۲، ۳۹، ۵۵، ۷۰، ۸۱، ۹۱، ۹۸، ۱۱۹، ۱۲۷، ۱۷۷، ۲۰۳ | تأیید متنی انجام شد |
| **S** | تصویر اسکن‌شده؛ لایه‌ی متن ندارد | ۶۱ | ۱۰، ۲۲، ۲۴–۳۱، ۹۹–۱۰۰، ۱۰۹–۱۱۸، ۱۳۷–۱۵۴، ۱۵۶–۱۷۶ | **خوانش تصویری لازم** (رندر ۱۵۰–۱۷۰ dpi) |
| **G** | لایه‌ی متن خراب (فونت رمزگذاری‌نشده) | ۴۶ | ۱۰۲–۱۰۸، ۱۸۶–۲۰۲، ۲۰۴–۲۱۲، ۲۲۹–۲۴۱ | **خوانش تصویری لازم**؛ متن PDF قابل اتکا نیست |
| **E** | خالی یا فقط شماره‌ی صفحه | ۳ | ۱۵۵، ۲۱۳–۲۱۴ | بررسی بصری (ممکن است محتوای برداری داشته باشد) |

ابعاد صفحات: ۱۲۷۱×۱۷۹۷ pt برای صفحات ۱۵۲–۱۷۶ (قطع بزرگ اسکن)؛ بقیه A4 (۵۹۵×۸۴۲) یا Letter (۶۱۲×۷۹۲) [C].

## ۳. واحدهای محتوایی (Unit map)

| واحد | موضوع | استاد (در منبع) | صفحات PDF | صفحات S/G/E | خطوط MD | پیشنهاد صفحه‌ی خروجی |
|---|---|---|---|---|---|---|
| U00 | شناخت بیوشیمی و سلول (تعریف، بیوشیمی و شیمی آلی، سلول واحد حیات، علل بیماری، کاربرد آزمایش) | خیاطیان (جلسه‌ی اول) | ۱–۱۰ | ۱۰ | MD 1–328 | 2 |
| U01 | آب، pH و بافر (توزیع آب بدن، ویژگی‌های آب، pH، pKa، بافرها) | افتخار (پارت ۱ و ۲) | ۱۱–۳۱ | ۲۲، ۲۴–۳۱ | MD 329–532 | 3 |
| U02 | کربوهیدرات‌ها – جلسه‌ی اول و پارت ۲ (ساختار، نام‌گذاری، ایزومری، واکنش، دی‌ساکاریدها) | رحیم‌زاده | ۳۲–۵۴ | — | MD 533–1100 | 3 |
| U03 | کربوهیدرات‌ها – جلسه‌ی دوم (واکنش‌های مونوساکاریدها، دی‌ساکاریدها، پلی‌ساکاریدها، هتروپلی‌ساکاریدها) | رحیم‌زاده | ۵۵–۶۹ | — | MD 1101–1910 | 2–3 |
| U04 | اسیدهای آمینه (ساختار، دسته‌بندی زنجیره‌ی جانبی، یونیزاسیون، pI، منحنی تیتراسیون) | رحیم‌زاده | ۷۰–۹۰ | — | MD 1911–2599 | 3 |
| U05 | ساختار پروتئین‌ها (پیوند پپتیدی، ساختارهای ۱ تا ۴، توالی‌یابی، واسرشت‌شدن، رسوب‌دهی) | رحیم‌زاده (پارت ۱ و ۲) | ۹۱–۱۰۸ | ۹۹–۱۰۰، ۱۰۲–۱۰۸ | MD 2600–3078 | 3 |
| U06 | هموپروتئین‌ها، میوگلوبین و هموگلوبین (ساختار، حالت T/R، منحنی تفکیک اکسیژن، اثر بور، 2,3-BPG) | نامشخص (جلسه‌ی ۷، گروه ۲) | ۱۰۹–۱۱۸ | ۱۰۹–۱۱۸ | در MD نیست | 2–3 |
| U07 | اسیدهای نوکلئیک (نوکلئوتید، بازها، پیوند فسفودی‌استر، ساختار DNA، انواع RNA) | رحیم‌زاده | ۱۱۹–۱۳۶ | — | MD 3079–3570 | 3 |
| U08 | همانندسازی DNA (انواع همانندسازی، مزلسون–استال، آنزیم‌ها، قطعات اوکازاکی، تلومر) | نامشخص | ۱۳۷–۱۵۱ | ۱۳۷–۱۵۱ | در MD نیست (یک اشاره در خط 3154) | 2–3 |
| U09 | لیپیدها (اسیدهای چرب، TAG/DAG/MAG، فسفولیپیدها، موارد دیگر نیازمند خوانش) | نامشخص | ۱۵۲–۱۷۶ | ۱۵۲–۱۷۶ | در MD نیست (اشاره‌ی جزئی در خط 25) | 3 |
| U10 | آنزیم‌ها (کاتالیزور زیستی، جایگاه فعال، کوفاکتور، پروآنزیم، سینتیک Km/Vmax، مهارکننده‌ها) | فرشیدفر | ۱۷۷–۲۰۲ | ۱۸۶–۲۰۲ | MD 3571–5229 | 4 |
| U11 | ویتامین‌ها (تعریف و تقسیم‌بندی، گروه B، ویتامین C، ویتامین‌های A/D/E/K) | داوودیان | ۲۰۳–۲۴۱ | ۲۰۴–۲۱۴، ۲۲۹–۲۴۱ | MD 5230–6644 | 5–6 |

توضیح: «در MD نیست» یعنی واژه‌ها و عبارت‌های کلیدی واحد در MD پیدا نشد یا فقط یک اشاره‌ی جزئی دارد.

## ۴. پوشش MD نسبت به PDF (صفحات T)

| بازه‌ی پوشش ۲۰-نویسه‌ای | تعداد صفحات T |
|---|---|
| ≥ ۵۰٪ | ۹۴ |
| ۲۰٪ تا ۴۹٪ | ۱۹ |
| کمتر از ۲۰٪ | ۴ |

روش: هر صفحه‌ی PDF با حروف نرمال‌شده به پنجره‌های ۲۰ حرفی تبدیل و با MD مقایسه شد. پوشش پایین در صفحات T معمولاً ناشی از **تفاوت متن** (MD بازنویسی شده، حذف یا جابه‌جایی) است؛ در صفحات G و S این معیار بی‌معنی است.

## ۵. مباحثی که در MD نیستند یا فقط اشاره‌ی جزئی دارند

1. **هموپروتئین‌ها و هموگلوبین (صفحات ۱۰۹–۱۱۸):** صفر تکرار واژه‌ی «هموگلوبین» در MD. محتوا تصویری است.
2. **همانندسازی DNA (صفحات ۱۳۷–۱۵۱):** فقط یک تکرار واژه‌ی «همانندسازی» در MD (خط ۳۱۵۴). محتوا تصویری است.
3. **لیپیدها (صفحات ۱۵۲–۱۷۶):** فقط یک اشاره‌ی جزئی به «لیپیدها» در MD (خط ۲۵). محتوا تصویری است؛ صفحه‌ی ۱۷۶ دست‌نویس است.
4. **هندرسون–هسلباخ، pKa و بافرها (صفحات ۲۲–۳۱):** در MD عبارت «هندرسون» و «pKa» وجود ندارد. بخش‌های ۲۲ و ۲۴–۳۱ تصویری‌اند.
5. **صفحات ۱۰۲–۱۰۸ (ساختار پروتئین، متن خراب):** MD بخش ساختار پروتئین دارد، ولی تطبیق بصری انجام نشده است.

جمع این بخش‌ها حدود **۶۰ صفحه‌ی PDF** است که فقط از طریق خوانش تصویری قابل‌اعتماد می‌شوند.

## ۶. گزارش اختلاف PDF و MD

| کد | نوع | محل | شرح | اقدام پیشنهادی |
|---|---|---|---|---|
| D1 | محتوای فقط تصویری | PDF: ۲۲، ۲۴–۳۱، ۱۰۹–۱۱۸، ۱۳۷–۱۷۶ | MD محتوای این صفحات را ندارد | خوانش تصویری؛ مبنا = PDF |
| D2 | لایه‌ی متن خراب | PDF: ۱۰۲–۱۰۸، ۱۸۶–۲۰۲، ۲۰۴–۲۱۲، ۲۲۹–۲۴۱ | نویسه‌ها جابه‌جا یا ناخوانا؛ مثال ص ۱۰۴: «پز ٍتئیي عوت ؽىل» | خوانش تصویری؛ مقایسه با MD فقط پس از تأیید بصری |
| D3 | حروف ارائه‌ای (Presentation Forms) | PDF: ۷۰–۸۰، ۱۷۹–۱۸۱، ۲۲۶–۲۲۸؛ MD: ۹٬۸۰۴ نویسه | مثل «اﺳﺘﺎد» و «پزﺷکی» | NFKC قبل از پردازش |
| D4 | فاصله‌گذاری شکسته | PDF: ۴۰–۵۴، ۲۲۶–۲۲۷ و موارد پرچم‌دار دیگر | مثل «نی در ا قسمت» | تصحیح پس از خوانش |
| D5 | شکست خط و چسبیدگی کلمات | MD | مثل «خیلیپیش پا افتاده»، «تولیدمی کنند»، «کهدر» | اصلاح فاصله‌ها در Source؛ ثبت تغییر |
| D6 | علائم ساختاری مزاحم | MD: ۱٬۸۳۸ خط ```؛ هدر «پزشکی بهمن ۱۴۰۰/۹۹»؛ شماره‌ی صفحه؛ «P a g e» | PDF: «Created in Master PDF Editor» | حذف (نه محتوا) |
| D7 | نام افراد، گروه و آرم | PDF: ص ۱۰۹ (نام گروه)، ص ۱۳۷/۱۵۲/۱۸۶ (آرم دانشگاه)؛ MD: «گروه جزوه: repartir» | اطلاعات شخصی و آرم | حذف؛ در خروجی نیاید |
| D8 | شکل‌های کتاب اسکن‌شده | PDF: ص ۱۱۳، ۱۱۵–۱۱۷ و نمودارهای ۱۳۷–۱۵۱ | احتمال حق مؤلف | بازسازی با SVG؛ کپی نشود |
| D9 | غلط‌های املایی احتمالی | MD: «اصال» (= اصلاً)، «سنتتیک»، «ناماستاد» | خطای تایپ منبع | اصلاح فقط با ثبت دلیل |
| D10 | تکرار بخش | MD: «مبحث آب-pH-بافر» در خطوط ۳۳۱ و ۵۲۷ | تکرار عنوان | ادغام با ثبت |
| D11 | دامنه‌ی موضوعی | MD دامنه‌ی ناقص نسبت به PDF دارد (واحدهای U06، U08، U09 و بخش‌هایی از U01) | تفاوت کامل | PDF مبنا؛ MD ثانویه |
| D12 | ارجاع کتاب | PDF ص ۴: «کتاب اسمیت»؛ MD خط ۳۵۶۶: «کتاب بیوشیمی دولین» | ارجاع منبع | بررسی در صورت دسترسی؛ بدون فرض |
| D13 | ترتیب و رقم‌ها | تطبیق کامل انجام نشده | — | در QA ثبت شود |
| D14 | بازیابی‌نشده | — | در یادداشت‌های نشست قبلی به‌عنوان اختلاف ثبت بوده، اما در فایل‌های پروژه اثری از آن نیست. محتوایش حدس زده نشده است | بازبینی ص ۱–۲۰ و تطبیق با MD؛ اگر پیدا نشد، از کاربر بپرس |
| D15 | تناقض ترتیب | PDF ص ۸۹ | متن: در هیستیدین ابتدا آمین آلفا (pK₂) و سپس R یونیزه می‌شود. جدول ۳-۱: pK_R = ۶٫۰۰ < pK₂ = ۹٫۱۷ و pI = ۷٫۵۹ با ترتیب «R اول» سازگار است | نیاز به تأیید؛ جدول ملاک محاسبه |
| D16 | برچسب کاور | PDF ص ۳۲ و ۵۵ | کاور ص ۳۲ (جلسه ۱، پارت ۱): «تعداد صفحات ۵»، اما بازه‌ی ۳۲–۳۸ = ۷ صفحه. کاور ص ۵۵ (جلسه ۲، پارت ۱ و ۲): «۱۱»، اما بازه‌ی ۵۵–۶۹ = ۱۵ صفحه | فقط برچسب؛ بازه‌ی واقعی ملاک است |
| D17 | احتمال خطای علمی | PDF ص ۶۵ | متن: «آلفا آمیالز» پیوند a1→a6 را می‌شکند و واحدهای گلوکز را جدا می‌کند. دانش رایج: α-آمیلاز پیوند α1→4 داخلی را می‌شکند، نه نقطه‌ی انشعاب α1→6 را | نیاز به تأیید با هارپر یا لنینجر. شماره‌ی صفحه در یادداشت قبلی ۶۳ بود؛ متن در ص ۶۵ است |
| D18 | خطای تایپی نام | PDF ص ۶۸ | گزینه‌ی ۱: «N-acetylglucosamine + D-glucosaminic acid» احتمالاً D-glucuronic acid است. گزینه‌ی ۳: «D-glucyronic acid» غلط تایپی است | تصویر را بررسی کن؛ ثبت |
| D19 | تناقض طبقه‌بندی | PDF ص ۲۰ | نمک‌ها و الکل‌ها «غیرالکترولیت» خوانده شده‌اند؛ در همان بخش نمک فلزات قلیایی «الکترولیت قوی» است | نیاز به تأیید |
| D20 | عدد مشکوک | PDF ص ۲۴ (جدول ۱-۲، تصویری) | pK کربنیک اسید ۳٫۸۰ آمده؛ pK₁ رایج کربنیک اسید حدود ۶ است | تطبیق با هارپر یا لنینجر |
| D21 | احتمال خطای نام | PDF ص ۸ | «CK_MD» احتمالاً CK-MB (ایزوآنزیم قلبی) است | تصویر را بررسی کن؛ نیاز به تأیید |
| D22 | ناسازگاری اصطلاح | PDF ص ۵۹ | محصول اکسیداسیون گروه الکلی انتهایی (با آلدهید دست‌نخورده) «آلدورونیک» نامیده شده است؛ اصطلاح رایج برای آن «اورونیک اسید» است | نیاز به تأیید |
| D23 | برچسب کاور | PDF ص ۷۰ و ۸۱ | کاور ص ۷۰: جلسه «سوم»، ۱۰ صفحه. کاور ص ۸۱: ۹ صفحه و فیلد جلسه خالی | فقط برچسب؛ بدون اثر بر محتوا |
| D24 | تطبیق منبع | PDF ص ۸۹ (جدول ۳-۱، تصویری) | جدول از منبع لنینجر است؛ محاسبه‌ی pI از pK سازگار است | تطبیق مقادیر با P6 (Lehninger) |

## ۷. طرح پیشنهادی جزوه (تخمینی)

هر مبحث به‌طور پیش‌فرض ۱ تا ۲ صفحه است؛ مباحث بزرگ به زیرمبحث‌هایی ۲ صفحه‌ای تقسیم شده‌اند. مجموع پیشنهادی **۳۸ تا ۴۳ صفحه‌ی A4** (تخمینی؛ نهایی پس از خوانش کامل).

| فصل | عنوان | زیرمبحث‌ها (منبع) | صفحه‌ی خروجی |
|---|---|---|---|
| — | جلد، فهرست، راهنمای رنگ‌ها | — | ۳ |
| ۱ | شناخت بیوشیمی و سلول (U00) | تعریف و شاخه‌ها؛ تفاوت بیوشیمی و شیمی آلی؛ سلول واحد حیات؛ علل بیماری (فیزیکی، شیمیایی، بیولوژیک، کمبود اکسیژن، ژنتیکی، ایمنی، تغذیه، غدد، روانی)؛ کاربرد آزمایش | ۲ |
| ۲ | آب، pH و بافر (U01) | توزیع آب بدن (ICF، ECF، پلاسما، مایع بین‌بافتی)؛ ساختار آب و پیوند هیدروژنی؛ pH و pKa؛ هندرسون–هسلباخ و بافرها (تصویری) | ۳ |
| ۳ | کربوهیدرات‌ها (U02 + U03) | (الف) طبقه‌بندی، آلدوز/کتوز، فیشر و هاورث، کربن کایرال، D/L، آنومر؛ (ب) احیا، اکسیداسیون، پیوند گلیکوزیدی، مالتوز/لاکتوز/ساکارز؛ (ج) نشاسته، گلیکوژن، دکسترانِ، سلولز، کیتین، گلیکوزآمینوگلیکان‌ها | ۶ |
| ۴ | اسیدهای آمینه (U04) | ساختار عمومی، دسته‌بندی زنجیره‌ی جانبی، متیونین و سیستئین، یونیزاسیون، pI، منحنی تیتراسیون | ۳ |
| ۵ | ساختار پروتئین‌ها (U05) | پیوند پپتیدی؛ ساختار ۱ تا ۴؛ روش ادمن؛ زوایای φ/ψ؛ واسرشت‌شدن؛ رسوب‌دهی نمکی | ۳ |
| ۶ | هموپروتئین‌ها و هموگلوبین (U06) | میوگلوبین؛ هموگلوبین (حالت T/R، همکاری)؛ منحنی تفکیک اکسیژن؛ اثر بور؛ 2,3-BPG | ۲–۳ |
| ۷ | اسیدهای نوکلئیک (U07) | نوکلئوزید و نوکلئوتید؛ پورین و پیریمیدین؛ پیوند فسفودی‌استر؛ DNA (B-form)؛ انواع RNA | ۳ |
| ۸ | همانندسازی DNA (U08) | انواع همانندسازی؛ مزلسون–استال؛ آنزیم‌ها؛ قطعات اوکازاکی؛ مراحل آغاز، طویل‌شدن، پایان؛ تلومر | ۲–۳ |
| ۹ | لیپیدها (U09) | تعریف و طبقه‌بندی؛ اسیدهای چرب (cis/trans)؛ TAG/DAG/MAG؛ فسفولیپیدها؛ موارد دیگر (نیازمند خوانش) | ۳ |
| ۱۰ | آنزیم‌ها (U10) | کاتالیزور زیستی؛ جایگاه فعال؛ کوفاکتور و کوآنزیم؛ پروآنزیم؛ سینتیک میکائیلیس–منتن (Km، Vmax)؛ مهارکننده‌ها | ۴ |
| ۱۱ | ویتامین‌ها (U11) | مبانی (تعریف، محلول در آب/چربی، کمبود، مسمومیت)؛ گروه B (B1 تا B12)؛ ویتامین C؛ A، D، E، K | ۵–۶ |
| — | جمع‌بندی و خودآزمایی | یک صفحه‌ی جمع‌بندی و یک صفحه‌ی کلید اعداد (فقط با اعداد تأییدشده) | ۱–۲ |

**نکته:** مسیرهای متابولیک کلاسیک (مثل گلیکولیز یا چرخه‌ی کربس) در PDF و MD پیدا نشد (واژه‌ی «گلیکولیز» صفر بار). بنابراین **نباید** این مسیرها به جزوه افزوده شوند.

## ۸. قواعد منبع و استناد

- اولویت: PDF > MD > منابع ذکرشده در جزوه (Devlin، Smith) > Harper > Lehninger.
- Harper و Lehninger فقط برای بررسی علمی موارد مبهم یا عددهای تردیدبرانگیز استفاده می‌شوند؛ هر ارجاع باید فصل/صفحه‌ی واقعاً بررسی‌شده را داشته باشد.
- در این مرحله هیچ ارجاع کتابی ثبت نشده است.

## ۹. یادداشت‌های کنترلی

- منبع فقط برچسب‌های «نکته» و «سوال» دارد؛ هیچ شاهدی برای «این سؤال امتحان می‌آید» وجود ندارد. از عبارت‌های «نکته مهم»، «تفاوت کلیدی» و «مناسب مرور امتحانی» استفاده شود.
- جزئیات بالینی فقط در حد مفهوم بیوشیمیایی باشد.
- نام دانشجویان، گروه‌ها، کانال‌ها و آرم‌ها در خروجی نیاید.

## ۱۰. جدول صفحه‌به‌صفحه (خلاصه‌ی ledger)

| صفحه | ابعاد (pt) | تصویر | نویسه‌ی متن | وضعیت | واحد | پوشش MD | پرچم‌ها | وضعیت بصری |
|---|---|---|---|---|---|---|---|---|
| ۱ | 612x792 | ۱ | ۱۲۸ | H | U00 | ۳۸٪ | — | cover/opener text-checked |
| ۲ | 612x792 | ۱ | ۱۸۹۲ | T | U00 | ۹۸٪ | — | text-checked; MD-compared |
| ۳ | 612x792 | ۰ | ۲۰۹۱ | T | U00 | ۹۹٪ | — | text-checked; MD-compared |
| ۴ | 612x792 | ۰ | ۱۸۶۷ | T | U00 | ۹۷٪ | — | text-checked; MD-compared |
| ۵ | 612x792 | ۰ | ۲۱۹۰ | T | U00 | ۶۵٪ | — | text-checked; MD-compared |
| ۶ | 612x792 | ۰ | ۱۳۷۶ | T | U00 | ۸۴٪ | — | text-checked; MD-compared |
| ۷ | 612x792 | ۱ | ۱۵۱۷ | T | U00 | ۵۹٪ | — | text-checked; MD-compared |
| ۸ | 612x792 | ۱ | ۱۶۱۱ | T | U00 | ۹۸٪ | — | text-checked; MD-compared |
| ۹ | 612x792 | ۰ | ۲۱۵۰ | T | U00 | ۹۹٪ | — | text-checked; MD-compared |
| ۱۰ | 612x792 | ۵ | ۱۲۷ | S | U00 | ۷۲٪ | — | REQUIRED (visual reading) |
| ۱۱ | 595x842 | ۳ | ۱۰۱ | H | U01 | ۱۰۰٪ | — | cover/opener text-checked |
| ۱۲ | 595x842 | ۲ | ۱۸۳۶ | T | U01 | ۸۹٪ | — | text-checked; MD-compared |
| ۱۳ | 595x842 | ۲ | ۱۶۸۹ | T | U01 | ۹۲٪ | spaced-letters | text-checked; MD-compared |
| ۱۴ | 595x842 | ۵ | ۳۰۶ | T | U01 | ۱۰۰٪ | spaced-letters; short-page | text-checked; MD-compared |
| ۱۵ | 595x842 | ۳ | ۱۰۴۷ | T | U01 | ۹۰٪ | spaced-letters | text-checked; MD-compared |
| ۱۶ | 595x842 | ۴ | ۳۱۰ | T | U01 | ۱۰۰٪ | short-page | text-checked; MD-compared |
| ۱۷ | 595x842 | ۴ | ۲۵۷ | T | U01 | ۸۷٪ | short-page | text-checked; MD-compared |
| ۱۸ | 595x842 | ۴ | ۲۲۱ | T | U01 | ۱۰۰٪ | short-page | text-checked; MD-compared |
| ۱۹ | 595x842 | ۷ | ۲۶۸ | T | U01 | ۸۶٪ | spaced-letters; short-page | text-checked; MD-compared |
| ۲۰ | 595x842 | ۳ | ۴۰۵ | T | U01 | ۱۰۰٪ | — | text-checked; MD-compared |
| ۲۱ | 595x842 | ۳ | ۳۳۱ | T | U01 | ۱۰۰٪ | short-page | text-checked; MD-compared |
| ۲۲ | 595x842 | ۳ | ۱۹ | S | U01 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۲۳ | 595x842 | ۳ | ۹۸ | H | U01 | ۱۰۰٪ | — | cover/opener text-checked |
| ۲۴ | 595x842 | ۴ | ۱۸ | S | U01 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۲۵ | 595x842 | ۴ | ۱۸ | S | U01 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۲۶ | 595x842 | ۴ | ۱۸ | S | U01 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۲۷ | 595x842 | ۴ | ۱۸ | S | U01 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۲۸ | 595x842 | ۴ | ۱۸ | S | U01 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۲۹ | 595x842 | ۴ | ۱۸ | S | U01 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۳۰ | 595x842 | ۴ | ۱۸ | S | U01 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۳۱ | 595x842 | ۲ | ۱۸ | S | U01 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۳۲ | 612x792 | ۸ | ۴۸۰ | H | U02 | ۱۰۰٪ | — | cover/opener text-checked |
| ۳۳ | 612x792 | ۰ | ۲۲۵۳ | T | U02 | ۸۸٪ | — | text-checked; MD-compared |
| ۳۴ | 612x792 | ۲ | ۱۷۲۶ | T | U02 | ۹۰٪ | — | text-checked; MD-compared |
| ۳۵ | 612x792 | ۲ | ۱۷۵۳ | T | U02 | ۷۸٪ | — | text-checked; MD-compared |
| ۳۶ | 612x792 | ۲ | ۱۵۳۰ | T | U02 | ۹۳٪ | — | text-checked; MD-compared |
| ۳۷ | 612x792 | ۳ | ۱۶۱۳ | T | U02 | ۹۸٪ | spaced-letters | text-checked; MD-compared |
| ۳۸ | 612x792 | ۱ | ۷۶۴ | T | U02 | ۱۰۰٪ | spaced-letters | text-checked; MD-compared |
| ۳۹ | 595x842 | ۱ | ۶۴ | H | U02 | ۱۰۰٪ | — | cover/opener text-checked |
| ۴۰ | 612x792 | ۱ | ۸۵۱ | T | U02 | ۶۹٪ | spaced-letters | text-checked; MD-compared |
| ۴۱ | 612x792 | ۰ | ۱۹۱۷ | T | U02 | ۴۴٪ | spaced-letters | text-checked; MD-compared |
| ۴۲ | 612x792 | ۰ | ۱۹۳۳ | T | U02 | ۴۰٪ | spaced-letters | text-checked; MD-compared |
| ۴۳ | 612x792 | ۱ | ۶۰۲ | T | U02 | ۷۲٪ | spaced-letters | text-checked; MD-compared |
| ۴۴ | 612x792 | ۲ | ۵۹۶ | T | U02 | ۶۷٪ | spaced-letters | text-checked; MD-compared |
| ۴۵ | 612x792 | ۱ | ۵۲۴ | T | U02 | ۳۰٪ | spaced-letters | text-checked; MD-compared |
| ۴۶ | 612x792 | ۱ | ۱۲۲۱ | T | U02 | ۳۴٪ | spaced-letters | text-checked; MD-compared |
| ۴۷ | 612x792 | ۰ | ۱۸۶۴ | T | U02 | ۳۸٪ | spaced-letters | text-checked; MD-compared |
| ۴۸ | 612x792 | ۱ | ۹۶۰ | T | U02 | ۲۶٪ | spaced-letters | text-checked; MD-compared |
| ۴۹ | 612x792 | ۰ | ۱۸۴۳ | T | U02 | ۲۹٪ | spaced-letters | text-checked; MD-compared |
| ۵۰ | 612x792 | ۱ | ۱۲۱۸ | T | U02 | ۲۳٪ | spaced-letters | text-checked; MD-compared |
| ۵۱ | 612x792 | ۱ | ۵۸۰ | T | U02 | ۳۹٪ | spaced-letters | text-checked; MD-compared |
| ۵۲ | 612x792 | ۱ | ۳۹۸ | T | U02 | ۵۱٪ | spaced-letters; short-page | text-checked; MD-compared |
| ۵۳ | 612x792 | ۱ | ۹۴۷ | T | U02 | ۶۱٪ | spaced-letters | text-checked; MD-compared |
| ۵۴ | 612x792 | ۱ | ۲۴۹ | T | U02 | ۳۵٪ | spaced-letters; short-page | text-checked; MD-compared |
| ۵۵ | 595x842 | ۱ | ۱۰۸ | H | U03 | ۱۰۰٪ | — | cover/opener text-checked |
| ۵۶ | 595x842 | ۱ | ۹۸۳ | T | U03 | ۱۰۰٪ | — | text-checked; MD-compared |
| ۵۷ | 595x842 | ۲ | ۱۰۹۹ | T | U03 | ۹۴٪ | — | text-checked; MD-compared |
| ۵۸ | 595x842 | ۲ | ۶۱۴ | T | U03 | ۹۵٪ | — | text-checked; MD-compared |
| ۵۹ | 595x842 | ۲ | ۱۰۰۶ | T | U03 | ۹۱٪ | — | text-checked; MD-compared |
| ۶۰ | 595x842 | ۱ | ۷۹۸ | T | U03 | ۸۵٪ | — | text-checked; MD-compared |
| ۶۱ | 595x842 | ۱ | ۱۳۸۶ | T | U03 | ۹۵٪ | — | text-checked; MD-compared |
| ۶۲ | 595x842 | ۲ | ۱۴۵۴ | T | U03 | ۸۲٪ | — | text-checked; MD-compared |
| ۶۳ | 595x842 | ۱ | ۱۰۹۹ | T | U03 | ۱۰۰٪ | spaced-letters | text-checked; MD-compared |
| ۶۴ | 595x842 | ۲ | ۸۰۱ | T | U03 | ۷۷٪ | — | text-checked; MD-compared |
| ۶۵ | 595x842 | ۲ | ۹۷۹ | T | U03 | ۷۷٪ | spaced-letters | text-checked; MD-compared |
| ۶۶ | 595x842 | ۳ | ۶۲۴ | T | U03 | ۶۹٪ | spaced-letters | text-checked; MD-compared |
| ۶۷ | 595x842 | ۱ | ۱۱۹۴ | T | U03 | ۸۸٪ | spaced-letters | text-checked; MD-compared |
| ۶۸ | 595x842 | ۳ | ۶۲۰ | T | U03 | ۱۰۰٪ | — | text-checked; MD-compared |
| ۶۹ | 595x842 | ۰ | ۱۹۰۱ | T | U03 | ۹۸٪ | spaced-letters | text-checked; MD-compared |
| ۷۰ | 595x842 | ۵ | ۲۶۲ | H | U04 | ۹۵٪ | — | cover/opener text-checked |
| ۷۱ | 595x842 | ۲ | ۱۴۹۹ | T | U04 | ۱۰۰٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۷۲ | 595x842 | ۲ | ۱۵۶۱ | T | U04 | ۹۲٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۷۳ | 595x842 | ۳ | ۱۳۳۴ | T | U04 | ۱۰۰٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۷۴ | 595x842 | ۱ | ۱۹۴۷ | T | U04 | ۹۶٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۷۵ | 595x842 | ۴ | ۱۲۹۱ | T | U04 | ۹۵٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۷۶ | 595x842 | ۴ | ۹۱۰ | T | U04 | ۹۳٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۷۷ | 595x842 | ۲ | ۱۸۰۱ | T | U04 | ۸۸٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۷۸ | 595x842 | ۱ | ۱۷۳۳ | T | U04 | ۹۹٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۷۹ | 595x842 | ۲ | ۱۲۲۷ | T | U04 | ۹۵٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۸۰ | 595x842 | ۱ | ۱۱۶۹ | T | U04 | ۸۲٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۸۱ | 612x792 | ۹ | ۲۸۹ | H | U04 | ۱۰۰٪ | — | cover/opener text-checked |
| ۸۲ | 612x792 | ۱ | ۲۰۹۰ | T | U04 | ۲۶٪ | spaced-letters | text-checked; MD-compared |
| ۸۳ | 612x792 | ۲ | ۲۱۷۱ | T | U04 | ۱۸٪ | spaced-letters | text-checked; MD-compared |
| ۸۴ | 612x792 | ۰ | ۲۸۴۰ | T | U04 | ۳۳٪ | spaced-letters | text-checked; MD-compared |
| ۸۵ | 612x792 | ۰ | ۱۱۰۶ | T | U04 | ۲۴٪ | spaced-letters | text-checked; MD-compared |
| ۸۶ | 612x792 | ۱ | ۲۶۰۷ | T | U04 | ۲۴٪ | spaced-letters | text-checked; MD-compared |
| ۸۷ | 612x792 | ۲ | ۱۶۹۷ | T | U04 | ۲۴٪ | spaced-letters | text-checked; MD-compared |
| ۸۸ | 612x792 | ۱ | ۱۷۹۷ | T | U04 | ۳۵٪ | spaced-letters | text-checked; MD-compared |
| ۸۹ | 612x792 | ۲ | ۱۴۹۴ | T | U04 | ۳۵٪ | spaced-letters | text-checked; MD-compared |
| ۹۰ | 612x792 | ۱ | ۱۳۶۱ | T | U04 | ۳۳٪ | spaced-letters | text-checked; MD-compared |
| ۹۱ | 595x842 | ۱ | ۶۵ | H | U05 | ۱۰۰٪ | — | cover/opener text-checked |
| ۹۲ | 595x842 | ۲ | ۱۵۹۱ | T | U05 | ۹۸٪ | — | text-checked; MD-compared |
| ۹۳ | 595x842 | ۲ | ۱۶۹۱ | T | U05 | ۹۸٪ | — | text-checked; MD-compared |
| ۹۴ | 595x842 | ۲ | ۱۵۸۷ | T | U05 | ۹۸٪ | — | text-checked; MD-compared |
| ۹۵ | 595x842 | ۱ | ۱۷۵۷ | T | U05 | ۱۰۰٪ | — | text-checked; MD-compared |
| ۹۶ | 595x842 | ۱ | ۱۸۵۹ | T | U05 | ۱۰۰٪ | — | text-checked; MD-compared |
| ۹۷ | 595x842 | ۱ | ۲۴۰۶ | T | U05 | ۱۰۰٪ | — | text-checked; MD-compared |
| ۹۸ | 595x842 | ۱ | ۶۵ | H | U05 | ۱۰۰٪ | — | cover/opener text-checked |
| ۹۹ | 612x792 | ۲ | ۴۶ | S | U05 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۱۰۰ | 612x792 | ۴ | ۶۵ | S | U05 | ۰٪ | — | REQUIRED (visual reading) |
| ۱۰۱ | 612x792 | ۲ | ۱۵۴ | T | U05 | ۷۷٪ | short-page | text-checked; MD-compared |
| ۱۰۲ | 612x792 | ۲ | ۱۵۳۳ | G | U05 | ۹۹٪ | — | REQUIRED (visual reading) |
| ۱۰۳ | 612x792 | ۲ | ۲۱۰۴ | G | U05 | ۹۲٪ | — | REQUIRED (visual reading) |
| ۱۰۴ | 612x792 | ۳ | ۱۵۰۳ | G | U05 | ۹۵٪ | — | REQUIRED (visual reading) |
| ۱۰۵ | 612x792 | ۰ | ۲۹۹۷ | G | U05 | ۹۵٪ | — | REQUIRED (visual reading) |
| ۱۰۶ | 612x792 | ۱ | ۸۵۶ | G | U05 | ۸۴٪ | — | REQUIRED (visual reading) |
| ۱۰۷ | 612x792 | ۱ | ۱۲۸۲ | G | U05 | ۸۶٪ | — | REQUIRED (visual reading) |
| ۱۰۸ | 612x792 | ۰ | ۷۸۳ | G | U05 | ۶۹٪ | — | REQUIRED (visual reading) |
| ۱۰۹ | 595x842 | ۱ | ۰ | S | U06 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۱۰ | 595x842 | ۱ | ۰ | S | U06 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۱۱ | 595x842 | ۱ | ۰ | S | U06 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۱۲ | 595x842 | ۱ | ۰ | S | U06 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۱۳ | 595x842 | ۱ | ۰ | S | U06 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۱۴ | 595x842 | ۱ | ۰ | S | U06 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۱۵ | 595x842 | ۱ | ۰ | S | U06 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۱۶ | 595x842 | ۱ | ۰ | S | U06 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۱۷ | 595x842 | ۱ | ۰ | S | U06 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۱۸ | 595x842 | ۱ | ۰ | S | U06 | — | — | REQUIRED (visual reading) |
| ۱۱۹ | 595x842 | ۱ | ۱۰۶ | H | U07 | ۷۱٪ | — | cover/opener text-checked |
| ۱۲۰ | 595x842 | ۱ | ۱۹۰۰ | T | U07 | ۹۷٪ | — | text-checked; MD-compared |
| ۱۲۱ | 595x842 | ۲ | ۲۳۸۹ | T | U07 | ۹۸٪ | — | text-checked; MD-compared |
| ۱۲۲ | 595x842 | ۲ | ۲۸۸۱ | T | U07 | ۸۸٪ | — | text-checked; MD-compared |
| ۱۲۳ | 595x842 | ۳ | ۱۸۸۸ | T | U07 | ۱۰۰٪ | — | text-checked; MD-compared |
| ۱۲۴ | 595x842 | ۲ | ۲۱۸۱ | T | U07 | ۹۰٪ | — | text-checked; MD-compared |
| ۱۲۵ | 595x842 | ۱ | ۲۵۱۹ | T | U07 | ۹۲٪ | — | text-checked; MD-compared |
| ۱۲۶ | 595x842 | ۲ | ۱۹۳۰ | T | U07 | ۹۶٪ | — | text-checked; MD-compared |
| ۱۲۷ | 595x842 | ۱۰ | ۱۵۷۲ | H | U07 | ۹۱٪ | — | cover/opener text-checked |
| ۱۲۸ | 595x842 | ۳ | ۱۴۷۷ | T | U07 | ۸۶٪ | presentation-forms(NFKC); spaced-letters | text-checked; MD-compared |
| ۱۲۹ | 595x842 | ۲ | ۱۹۷۷ | T | U07 | ۸۱٪ | presentation-forms(NFKC); spaced-letters | text-checked; MD-compared |
| ۱۳۰ | 595x842 | ۲ | ۱۶۰۷ | T | U07 | ۸۶٪ | — | text-checked; MD-compared |
| ۱۳۱ | 595x842 | ۲ | ۲۲۴۰ | T | U07 | ۸۲٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۱۳۲ | 595x842 | ۳ | ۲۰۵۰ | T | U07 | ۹۶٪ | — | text-checked; MD-compared |
| ۱۳۳ | 595x842 | ۱ | ۲۳۹۶ | T | U07 | ۸۹٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۱۳۴ | 595x842 | ۳ | ۱۶۷۰ | T | U07 | ۸۸٪ | — | text-checked; MD-compared |
| ۱۳۵ | 595x842 | ۳ | ۱۵۷۷ | T | U07 | ۸۷٪ | presentation-forms(NFKC); spaced-letters | text-checked; MD-compared |
| ۱۳۶ | 595x842 | ۱ | ۳۶۹ | T | U07 | ۶۷٪ | presentation-forms(NFKC); short-page | text-checked; MD-compared |
| ۱۳۷ | 595x842 | ۷۱ | ۰ | S | U08 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۳۸ | 595x842 | ۷۰ | ۰ | S | U08 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۳۹ | 595x842 | ۷۱ | ۰ | S | U08 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۴۰ | 595x842 | ۷۰ | ۰ | S | U08 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۴۱ | 595x842 | ۷۱ | ۰ | S | U08 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۴۲ | 595x842 | ۷۱ | ۰ | S | U08 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۴۳ | 595x842 | ۷۰ | ۰ | S | U08 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۴۴ | 595x842 | ۲۰ | ۰ | S | U08 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۴۵ | 595x842 | ۷۳ | ۰ | S | U08 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۴۶ | 595x842 | ۷۳ | ۰ | S | U08 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۴۷ | 595x842 | ۷۱ | ۰ | S | U08 | — | — | REQUIRED (visual reading) |
| ۱۴۸ | 595x842 | ۷۳ | ۰ | S | U08 | — | — | REQUIRED (visual reading) |
| ۱۴۹ | 595x842 | ۷۳ | ۰ | S | U08 | — | — | REQUIRED (visual reading) |
| ۱۵۰ | 595x842 | ۷۳ | ۰ | S | U08 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۵۱ | 595x842 | ۷۳ | ۰ | S | U08 | — | — | REQUIRED (visual reading) |
| ۱۵۲ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۵۳ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۵۴ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۵۵ | 1271x1797 | ۰ | ۰ | E | U09 | — | — | REQUIRED (visual reading) |
| ۱۵۶ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۵۷ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۵۸ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۵۹ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۶۰ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۶۱ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۶۲ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۶۳ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۶۴ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۶۵ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۶۶ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۶۷ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۶۸ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۶۹ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۷۰ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۷۱ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۷۲ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۷۳ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۷۴ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۷۵ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) |
| ۱۷۶ | 1271x1797 | ۱ | ۰ | S | U09 | — | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۷۷ | 595x842 | ۸ | ۱۷۹۸ | H | U10 | ۹۴٪ | — | cover/opener text-checked |
| ۱۷۸ | 595x842 | ۱ | ۱۸۶۴ | T | U10 | ۸۷٪ | — | text-checked; MD-compared |
| ۱۷۹ | 612x792 | ۱ | ۱۲۸۰ | T | U10 | ۰٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۱۸۰ | 612x792 | ۲ | ۵۲۱ | T | U10 | ۱٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۱۸۱ | 612x792 | ۰ | ۳۳۰ | T | U10 | ۰٪ | presentation-forms(NFKC); short-page | text-checked; MD-compared |
| ۱۸۲ | 595x842 | ۰ | ۲۳۲۹ | T | U10 | ۹۴٪ | — | text-checked; MD-compared |
| ۱۸۳ | 595x842 | ۱ | ۲۰۱۸ | T | U10 | ۹۱٪ | — | text-checked; MD-compared |
| ۱۸۴ | 595x842 | ۰ | ۲۱۹۵ | T | U10 | ۹۱٪ | — | text-checked; MD-compared |
| ۱۸۵ | 595x842 | ۰ | ۱۶۴۲ | T | U10 | ۱۰۰٪ | — | text-checked; MD-compared |
| ۱۸۶ | 595x842 | ۱۸ | ۲۶۲۵ | G | U10 | ۱۰۰٪ | — | REQUIRED (visual reading) + thumbnail sampled |
| ۱۸۷ | 595x842 | ۸ | ۲۵۶۷ | G | U10 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۱۸۸ | 595x842 | ۱ | ۲۷۲۵ | G | U10 | ۹۸٪ | — | REQUIRED (visual reading) |
| ۱۸۹ | 595x842 | ۱ | ۲۱۰۴ | G | U10 | ۹۹٪ | — | REQUIRED (visual reading) |
| ۱۹۰ | 595x842 | ۷ | ۲۰۲۶ | G | U10 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۱۹۱ | 595x842 | ۳ | ۱۷۱۹ | G | U10 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۱۹۲ | 595x842 | ۳ | ۲۲۴۲ | G | U10 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۱۹۳ | 595x842 | ۲ | ۲۳۵۹ | G | U10 | ۹۹٪ | — | REQUIRED (visual reading) |
| ۱۹۴ | 595x842 | ۳ | ۲۲۸۵ | G | U10 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۱۹۵ | 595x842 | ۱ | ۲۴۷۲ | G | U10 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۱۹۶ | 595x842 | ۰ | ۲۸۷۹ | G | U10 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۱۹۷ | 595x842 | ۷ | ۳۱۵۶ | G | U10 | ۹۵٪ | — | REQUIRED (visual reading) |
| ۱۹۸ | 595x842 | ۰ | ۲۸۴۰ | G | U10 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۱۹۹ | 595x842 | ۰ | ۲۴۹۰ | G | U10 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۲۰۰ | 595x842 | ۲ | ۲۵۰۹ | G | U10 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۲۰۱ | 595x842 | ۳ | ۱۵۹۷ | G | U10 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۲۰۲ | 595x842 | ۳ | ۱۶۱۶ | G | U10 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۲۰۳ | 595x842 | ۸ | ۲۰۷۳ | H | U11 | ۱۷٪ | — | cover/opener text-checked |
| ۲۰۴ | 595x842 | ۰ | ۲۷۵۵ | G | U11 | ۲۵٪ | — | REQUIRED (visual reading) |
| ۲۰۵ | 595x842 | ۰ | ۲۷۷۱ | G | U11 | ۸٪ | — | REQUIRED (visual reading) + thumbnail sampled |
| ۲۰۶ | 595x842 | ۲ | ۲۲۶۹ | G | U11 | ۲۰٪ | — | REQUIRED (visual reading) |
| ۲۰۷ | 595x842 | ۰ | ۳۰۲۸ | G | U11 | ۲۱٪ | — | REQUIRED (visual reading) |
| ۲۰۸ | 595x842 | ۳ | ۲۱۷۹ | G | U11 | ۲۰٪ | — | REQUIRED (visual reading) |
| ۲۰۹ | 595x842 | ۰ | ۳۱۴۵ | G | U11 | ۱۴٪ | — | REQUIRED (visual reading) |
| ۲۱۰ | 595x842 | ۱ | ۲۶۲۳ | G | U11 | ۲۴٪ | — | REQUIRED (visual reading) |
| ۲۱۱ | 595x842 | ۰ | ۳۲۲۲ | G | U11 | ۱۹٪ | — | REQUIRED (visual reading) |
| ۲۱۲ | 595x842 | ۳ | ۲۳۱۶ | G | U11 | ۱۴٪ | — | REQUIRED (visual reading) |
| ۲۱۳ | 595x842 | ۰ | ۱۰۹ | E | U11 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۲۱۴ | 595x842 | ۰ | ۱۰۹ | E | U11 | ۱۰۰٪ | — | REQUIRED (visual reading) |
| ۲۱۵ | 595x842 | ۶ | ۲۰۰۸ | T | U11 | ۹۳٪ | — | text-checked; MD-compared |
| ۲۱۶ | 595x842 | ۲ | ۱۷۱۴ | T | U11 | ۱۰۰٪ | — | text-checked; MD-compared |
| ۲۱۷ | 595x842 | ۷ | ۱۱۵۹ | T | U11 | ۱۰۰٪ | — | text-checked; MD-compared |
| ۲۱۸ | 595x842 | ۱ | ۲۴۰۶ | T | U11 | ۹۲٪ | — | text-checked; MD-compared |
| ۲۱۹ | 595x842 | ۱ | ۲۲۴۶ | T | U11 | ۹۵٪ | — | text-checked; MD-compared |
| ۲۲۰ | 595x842 | ۳ | ۱۴۹۷ | T | U11 | ۹۲٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۲۲۱ | 595x842 | ۰ | ۲۵۰۳ | T | U11 | ۸۵٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۲۲۲ | 595x842 | ۱ | ۱۲۹۵ | T | U11 | ۸۳٪ | presentation-forms(NFKC) | text-checked; MD-compared |
| ۲۲۳ | 595x842 | ۰ | ۶۹۳ | T | U11 | ۹۵٪ | — | text-checked; MD-compared |
| ۲۲۴ | 595x842 | ۰ | ۲۲۱۲ | T | U11 | ۹۵٪ | — | text-checked; MD-compared |
| ۲۲۵ | 595x842 | ۰ | ۱۲۴۴ | T | U11 | ۱۰۰٪ | — | text-checked; MD-compared |
| ۲۲۶ | 612x792 | ۰ | ۱۸۵۴ | T | U11 | ۲۲٪ | spaced-letters | text-checked; MD-compared |
| ۲۲۷ | 595x842 | ۰ | ۱۴۳۳ | T | U11 | ۵۵٪ | presentation-forms(NFKC); spaced-letters | text-checked; MD-compared |
| ۲۲۸ | 595x842 | ۰ | ۱۴۹ | T | U11 | ۹۹٪ | presentation-forms(NFKC); short-page | text-checked; MD-compared |
| ۲۲۹ | 595x842 | ۱۰ | ۱۲۹۹ | G | U11 | ۵۳٪ | — | REQUIRED (visual reading) + thumbnail sampled |
| ۲۳۰ | 595x842 | ۳ | ۲۰۶۷ | G | U11 | ۳۹٪ | — | REQUIRED (visual reading) |
| ۲۳۱ | 595x842 | ۳ | ۲۶۳۲ | G | U11 | ۳۱٪ | — | REQUIRED (visual reading) |
| ۲۳۲ | 595x842 | ۲ | ۳۰۸۳ | G | U11 | ۴۰٪ | — | REQUIRED (visual reading) |
| ۲۳۳ | 595x842 | ۲ | ۱۲۱۵ | G | U11 | ۶۳٪ | — | REQUIRED (visual reading) |
| ۲۳۴ | 595x842 | ۱ | ۳۳۷۱ | G | U11 | ۵۳٪ | — | REQUIRED (visual reading) |
| ۲۳۵ | 595x842 | ۳ | ۱۸۸۹ | G | U11 | ۲۶٪ | — | REQUIRED (visual reading) |
| ۲۳۶ | 595x842 | ۱ | ۲۲۷۳ | G | U11 | ۷۸٪ | — | REQUIRED (visual reading) |
| ۲۳۷ | 595x842 | ۳ | ۱۹۸۷ | G | U11 | ۸۰٪ | — | REQUIRED (visual reading) |
| ۲۳۸ | 595x842 | ۲ | ۱۷۳۱ | G | U11 | ۸۲٪ | — | REQUIRED (visual reading) |
| ۲۳۹ | 595x842 | ۱ | ۲۵۶۴ | G | U11 | ۶۲٪ | — | REQUIRED (visual reading) |
| ۲۴۰ | 595x842 | ۳ | ۱۷۱۳ | G | U11 | ۲۲٪ | — | REQUIRED (visual reading) |
| ۲۴۱ | 595x842 | ۵ | ۲۴۸۰ | G | U11 | ۲۷٪ | — | REQUIRED (visual reading) |

منبع کامل ستون‌ها: `analysis/page_ledger.csv`.

## ۱۱. یافته‌های نشست دوم (افزوده)

- **صفحه‌ی ۷۶ (تصویری):** گروه قطبی بدون بار پنج عضو دارد: سرین (Ser S)، ترئونین (Thr T)، سیستئین (Cys C)، آسپاراژین (Asn N)، گلوتامین (Gln Q).
- **صفحه‌ی ۸۹ (تصویری):** جدول ۳-۱ (ستون‌های pK₁، pK₂، pK_R، pI برای ۲۰ اسید آمینه). مثال‌های بازبینی: گلیسین (2.34+9.60)/2 = 5.97؛ سیستئین (1.96+8.18)/2 = 5.07؛ آسپارتات (1.88+3.65)/2 = 2.77؛ هیستیدین (6.00+9.17)/2 = 7.59. همه با ستون pI سازگارند. جدول از منبع لنینجر است (P6).
- **کاور صفحه‌ی ۷۰:** «مبحث: ساختار آمینواسید»، جلسه‌ی سوم، ۱۰ صفحه، استاد رحیم‌زاده، گروه D.
- **کاور صفحه‌ی ۸۱:** «مبحث: آمینواسیدها»، ۹ صفحه، استاد رحیم‌زاده، گروه D؛ فیلد جلسه خالی.
- **وضعیت ledger (ستون visual_check):** ۱۱۷ صفحه‌ی T «text-checked; MD-compared»؛ ۱۴ صفحه‌ی H «cover/opener text-checked»؛ ۷۳ صفحه‌ی S/G/E «REQUIRED (visual reading)»؛ ۳۷ صفحه «REQUIRED + thumbnail sampled».
- **OCR خام:** در زمان نگارش ۶۸ از ۱۲۴ صفحه‌ی غیرمتنی OCR شده است؛ فرایند ادامه دارد. OCR نویزی است و ملاک نیست.
- **MD:** سرفصل «مبحث آب-pH-بافر» در خطوط ۳۳۱ و ۵۲۷ است؛ «pKa» و «هندرسون» در MD نیست (بند ۵-۴).
