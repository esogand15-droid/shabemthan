from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display

PAGE_W, PAGE_H = 595.92, 842.88
MARGIN_X = 33.5
CONTENT_W = 528.8
TOP_MARGIN = 17.2

C_BRAND_DARK = HexColor('#0c7a52')
C_BRAND = HexColor('#0f9d68')
C_BAND_START = HexColor('#0c7b53')
C_BAND_END = HexColor('#16b676')
C_HIGHLIGHT = HexColor('#ffd166')
C_TEXT_STRONG = HexColor('#111827')
C_TEXT_HEADING = HexColor('#20242b')
C_TEXT_BODY = HexColor('#374151')
C_TEXT_BODY_ALT = HexColor('#3f4652')
C_TEXT_MUTED = HexColor('#6b7280')
C_SURFACE = HexColor('#fafbfc')
C_SURFACE_LEAD = HexColor('#f6f9f8')
C_LINE = HexColor('#eef0f2')
C_WHITE = HexColor('#ffffff')

BOX_STYLES = {
    'tip': {'bg': HexColor('#fff8e6'), 'border': HexColor('#f5dea0'), 'label_c': HexColor('#9a6b00'), 'title': 'نکته طلایی', 'icon': 'build_assets/png_icons/key.png'},
    'analogy': {'bg': HexColor('#eef5ff'), 'border': HexColor('#bcd7fb'), 'label_c': HexColor('#1d5fb8'), 'title': 'تشبیه', 'icon': 'build_assets/png_icons/target.png'},
    'warning': {'bg': HexColor('#fff1ee'), 'border': HexColor('#f6c3b6'), 'label_c': HexColor('#c1440e'), 'title': 'دام امتحانی', 'icon': 'build_assets/png_icons/warning.png'},
    'mnemonic': {'bg': HexColor('#f4eeff'), 'border': HexColor('#d9c6fb'), 'label_c': HexColor('#6d28d9'), 'title': 'ترفند حفظی', 'icon': 'build_assets/png_icons/bulb.png'}
}

def fa(text):
    if not text:
        return ""
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

def draw_header_exact(c, chapter_pill_str, title_fa, subtitle_fa, icon_png_path):
    c.saveState()
    bar_h = 67.0
    bar_y = PAGE_H - TOP_MARGIN - bar_h
    
    # 1. Gradient background with rounded corners 7pt
    steps = 45
    step_w = CONTENT_W / steps
    r1, g1, b1 = 12/255, 123/255, 83/255
    r2, g2, b2 = 22/255, 182/255, 118/255
    
    # Clip path for rounded rect
    p = c.beginPath()
    p.roundRect(MARGIN_X, bar_y, CONTENT_W, bar_h, 7)
    c.clipPath(p, stroke=0, fill=0)
    
    for i in range(steps):
        frac = i / steps
        r = r1 + (r2 - r1) * frac
        g = g1 + (g2 - g1) * frac
        b = b1 + (b2 - b1) * frac
        c.setFillColorRGB(r, g, b)
        c.rect(MARGIN_X + i * step_w, bar_y, step_w + 1, bar_h, fill=1, stroke=0)
    c.restoreState()
    
    c.saveState()
    # 2. Semi-transparent white icon square on right
    badge_w = 40.0
    badge_h = 40.0
    badge_x = MARGIN_X + CONTENT_W - badge_w - 13.5
    badge_y = bar_y + (bar_h - badge_h) / 2
    
    # fill with white opacity 0.2
    c.setFillColorRGB(1, 1, 1, 0.22)
    c.roundRect(badge_x, badge_y, badge_w, badge_h, 8, fill=1, stroke=0)
    
    # Draw icon image inside
    if icon_png_path:
        img_size = 24.0
        ix = badge_x + (badge_w - img_size) / 2
        iy = badge_y + (badge_h - img_size) / 2
        c.drawImage(icon_png_path, ix, iy, width=img_size, height=img_size, mask='auto')
        
    # 3. Chapter Pill (e.g. "فصل ۱")
    pill_w = 42.0
    pill_h = 16.0
    pill_x = badge_x - pill_w - 10.0
    pill_y = bar_y + bar_h - pill_h - 12.0
    c.setFillColorRGB(1, 1, 1, 0.20)
    c.roundRect(pill_x, pill_y, pill_w, pill_h, 8, fill=1, stroke=0)
    
    c.setFont('Vazirmatn-Bold', 8.5)
    c.setFillColor(C_WHITE)
    c.drawCentredString(pill_x + pill_w / 2, pill_y + 3.8, fa(chapter_pill_str))
    
    # 4. Main Title
    c.setFont('Vazirmatn-ExtraBold', 14.5)
    c.setFillColor(C_WHITE)
    text_right_x = badge_x - 12.0
    c.drawRightString(text_right_x, bar_y + 24.0, fa(title_fa))
    
    # 5. Subtitle
    c.setFont('Vazirmatn-Regular', 8.5)
    c.setFillColorRGB(0.92, 0.96, 0.94)
    c.drawRightString(text_right_x, bar_y + 10.0, fa(subtitle_fa))
    
    c.restoreState()
    return bar_y

def draw_box_exact(c, cur_y, box_type, label, lines, extra_h=0):
    st = BOX_STYLES[box_type]
    c.saveState()
    box_h = 24 + len(lines) * 14.0 + extra_h
    y = cur_y - 8 - box_h
    
    c.setFillColor(st['bg'])
    c.setStrokeColor(st['border'])
    c.setLineWidth(0.75)
    c.roundRect(MARGIN_X, y, CONTENT_W, box_h, 6, fill=1, stroke=1)
    
    # Draw icon on right of title
    icon_p = st['icon']
    icon_sz = 14.0
    c.drawImage(icon_p, MARGIN_X + CONTENT_W - 24, y + box_h - 18, width=icon_sz, height=icon_sz, mask='auto')
    
    c.setFont('Vazirmatn-Bold', 9.2)
    c.setFillColor(st['label_c'])
    c.drawRightString(MARGIN_X + CONTENT_W - 30, y + box_h - 15, fa(label))
    
    c.setFont('Vazirmatn-Regular', 8.8)
    c.setFillColor(C_TEXT_BODY_ALT)
    ty = y + box_h - 18
    for line in lines:
        ty -= 14.0
        c.drawRightString(MARGIN_X + CONTENT_W - 14, ty, fa(line))
        
    c.restoreState()
    return y

def draw_summary_box_exact(c, cur_y, title_fa, bullet_lines):
    c.saveState()
    box_h = 26 + len(bullet_lines) * 15.0
    y = cur_y - 10 - box_h
    c.setFillColor(C_BRAND_DARK)
    c.roundRect(MARGIN_X, y, CONTENT_W, box_h, 7, fill=1, stroke=0)
    
    # Icon pin
    c.drawImage('build_assets/png_icons/pin.png', MARGIN_X + CONTENT_W - 24, y + box_h - 20, width=15, height=15, mask='auto')
    
    c.setFont('Vazirmatn-ExtraBold', 10.0)
    c.setFillColor(C_WHITE)
    c.drawRightString(MARGIN_X + CONTENT_W - 30, y + box_h - 17, fa(f"جمع‌بندی فصل در یک نگاه"))
    
    c.setFont('Vazirmatn-Regular', 8.8)
    c.setFillColor(C_WHITE)
    ty = y + box_h - 19
    for line in bullet_lines:
        ty -= 15.0
        # Draw small star
        c.drawImage('build_assets/png_icons/star.png', MARGIN_X + CONTENT_W - 22, ty + 1, width=10, height=10, mask='auto')
        c.drawRightString(MARGIN_X + CONTENT_W - 28, ty, fa(line))
        
    c.restoreState()
    return y

print("New exact components defined successfully!")
