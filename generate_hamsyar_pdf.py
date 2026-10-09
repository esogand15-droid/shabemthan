import sys, os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display

# 1. Register fonts
pdfmetrics.registerFont(TTFont('Vazirmatn-Regular', 'fonts/ttf/Vazirmatn-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Vazirmatn-Medium', 'fonts/ttf/Vazirmatn-Medium.ttf'))
pdfmetrics.registerFont(TTFont('Vazirmatn-Bold', 'fonts/ttf/Vazirmatn-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Vazirmatn-ExtraBold', 'fonts/ttf/Vazirmatn-ExtraBold.ttf'))
pdfmetrics.registerFont(TTFont('LiberationSans-Regular', 'fonts/liberation/LiberationSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('LiberationSans-Bold', 'fonts/liberation/LiberationSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))

# Dimensions
PAGE_W, PAGE_H = 595.92, 842.88
MARGIN_X = 33.5
CONTENT_W = 528.8
TOP_MARGIN = 17.2

# Color Palette
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

# Box styles
BOX_STYLES = {
    'tip': {'bg': HexColor('#fff8e6'), 'border': HexColor('#f5dea0'), 'label_c': HexColor('#9a6b00'), 'title': 'نکته طلایی'},
    'analogy': {'bg': HexColor('#eef5ff'), 'border': HexColor('#bcd7fb'), 'label_c': HexColor('#1d5fb8'), 'title': 'تشبیه مفهومی'},
    'warning': {'bg': HexColor('#fff1ee'), 'border': HexColor('#f6c3b6'), 'label_c': HexColor('#c1440e'), 'title': 'دام امتحانی'},
    'mnemonic': {'bg': HexColor('#f4eeff'), 'border': HexColor('#d9c6fb'), 'label_c': HexColor('#6d28d9'), 'title': 'ترفند حفظی'}
}

def fa(text):
    if not text:
        return ""
    # reshape and apply bidi
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

def draw_header(c, chapter_num_str, title_fa, subtitle_fa):
    # Chapter header bar
    c.saveState()
    bar_h = 67.0
    bar_y = PAGE_H - TOP_MARGIN - bar_h
    
    # Gradient simulation using slices
    steps = 40
    step_w = PAGE_W / steps
    r1, g1, b1 = 12/255, 123/255, 83/255
    r2, g2, b2 = 22/255, 182/255, 118/255
    
    c.rect(0, bar_y, PAGE_W, bar_h, fill=1, stroke=0)
    for i in range(steps):
        frac = i / steps
        r = r1 + (r2 - r1) * frac
        g = g1 + (g2 - g1) * frac
        b = b1 + (b2 - b1) * frac
        c.setFillColorRGB(r, g, b)
        c.rect(i * step_w, bar_y, step_w + 1, bar_h, fill=1, stroke=0)
        
    # Emoji / badge box on right
    c.setFillColor(C_WHITE)
    badge_x = PAGE_W - MARGIN_X - 44
    badge_y = bar_y + (bar_h - 44)/2
    c.roundRect(badge_x, badge_y, 44, 44, 6, fill=0, stroke=1)
    
    # Chapter pill
    c.setFont('Vazirmatn-ExtraBold', 8)
    pill_text = fa(chapter_num_str)
    c.drawRightString(PAGE_W - MARGIN_X - 54, bar_y + 44, pill_text)
    
    # Title
    c.setFont('Vazirmatn-ExtraBold', 13.5)
    c.drawRightString(PAGE_W - MARGIN_X - 54, bar_y + 24, fa(title_fa))
    
    # Subtitle
    c.setFont('Vazirmatn-Regular', 8.5)
    c.setFillColorRGB(0.9, 0.95, 0.92)
    c.drawRightString(PAGE_W - MARGIN_X - 54, bar_y + 10, fa(subtitle_fa))
    
    c.restoreState()
    return bar_y

def draw_lead(c, cur_y, lead_text):
    c.saveState()
    lead_h = 52.0
    y = cur_y - 12 - lead_h
    # background box
    c.setFillColor(C_SURFACE_LEAD)
    c.roundRect(MARGIN_X, y, CONTENT_W, lead_h, 5, fill=1, stroke=0)
    # right bar
    c.setFillColor(C_BRAND)
    c.rect(MARGIN_X + CONTENT_W - 3, y, 3, lead_h, fill=1, stroke=0)
    
    # text
    c.setFont('Vazirmatn-Medium', 10.0)
    c.setFillColor(C_TEXT_BODY)
    c.drawRightString(MARGIN_X + CONTENT_W - 12, y + 30, fa(lead_text[0]))
    if len(lead_text) > 1:
        c.setFont('Vazirmatn-Regular', 9.2)
        c.setFillColor(C_TEXT_MUTED)
        c.drawRightString(MARGIN_X + CONTENT_W - 12, y + 10, fa(lead_text[1]))
    c.restoreState()
    return y

def draw_section_title(c, cur_y, title_text):
    c.saveState()
    y = cur_y - 16
    c.setFillColor(C_BRAND)
    c.rect(MARGIN_X + CONTENT_W - 3, y - 2, 3, 14, fill=1, stroke=0)
    c.setFont('Vazirmatn-Bold', 10.5)
    c.setFillColor(C_BRAND_DARK)
    c.drawRightString(MARGIN_X + CONTENT_W - 10, y, fa(title_text))
    c.restoreState()
    return y - 6

def draw_paragraph(c, cur_y, text_lines, font_size=9.8, line_h=15.5):
    c.saveState()
    c.setFont('Vazirmatn-Regular', font_size)
    c.setFillColor(C_TEXT_BODY)
    y = cur_y
    for line in text_lines:
        y -= line_h
        c.drawRightString(MARGIN_X + CONTENT_W, y, fa(line))
    c.restoreState()
    return y

def draw_box(c, cur_y, box_type, label, lines, extra_h=0):
    st = BOX_STYLES[box_type]
    c.saveState()
    box_h = 28 + len(lines) * 15.0 + extra_h
    y = cur_y - 8 - box_h
    # bg & border
    c.setFillColor(st['bg'])
    c.setStrokeColor(st['border'])
    c.setLineWidth(0.75)
    c.roundRect(MARGIN_X, y, CONTENT_W, box_h, 6, fill=1, stroke=1)
    
    # label
    c.setFont('Vazirmatn-Bold', 10.0)
    c.setFillColor(st['label_c'])
    c.drawRightString(MARGIN_X + CONTENT_W - 10, y + box_h - 14, fa(f"● {label}:"))
    
    # content
    c.setFont('Vazirmatn-Regular', 9.2)
    c.setFillColor(C_TEXT_BODY_ALT)
    ty = y + box_h - 16
    for line in lines:
        ty -= 15.0
        c.drawRightString(MARGIN_X + CONTENT_W - 14, ty, fa(line))
        
    c.restoreState()
    return y

def draw_table(c, cur_y, headers, rows, col_widths, row_h=21.0, font_sz=8.8):
    c.saveState()
    tbl_h = (len(rows) + 1) * row_h
    y = cur_y - 8 - tbl_h
    
    # Header row
    c.setFillColor(C_BRAND)
    c.roundRect(MARGIN_X, y + tbl_h - row_h, CONTENT_W, row_h, 4, fill=1, stroke=0)
    c.setFont('Vazirmatn-Bold', font_sz + 0.2)
    c.setFillColor(C_WHITE)
    
    cur_x = MARGIN_X + CONTENT_W
    for i, h in enumerate(headers):
        w = col_widths[i]
        c.drawRightString(cur_x - 6, y + tbl_h - row_h + (row_h - font_sz)/2, fa(h))
        cur_x -= w
        
    # Rows
    c.setFont('Vazirmatn-Regular', font_sz)
    for r_idx, row in enumerate(rows):
        ry = y + tbl_h - (r_idx + 2) * row_h
        if r_idx % 2 == 1:
            c.setFillColor(C_SURFACE)
            c.rect(MARGIN_X, ry, CONTENT_W, row_h, fill=1, stroke=0)
            
        cur_x = MARGIN_X + CONTENT_W
        for c_idx, cell in enumerate(row):
            w = col_widths[c_idx]
            if c_idx == 0:
                c.setFont('Vazirmatn-Bold', font_sz)
                c.setFillColor(C_BRAND_DARK)
            else:
                c.setFont('Vazirmatn-Regular', font_sz)
                c.setFillColor(C_TEXT_BODY)
            
            # Smart check if cell text overflows column width
            t_fa = fa(cell)
            txt_w = pdfmetrics.stringWidth(t_fa, 'Vazirmatn-Regular' if c_idx > 0 else 'Vazirmatn-Bold', font_sz)
            cell_pad = 6
            if txt_w > w - 10:
                # slightly smaller font if overflowing cell
                c.setFont('Vazirmatn-Regular' if c_idx > 0 else 'Vazirmatn-Bold', font_sz - 0.7)
                cell_pad = 3
                
            c.drawRightString(cur_x - cell_pad, ry + (row_h - font_sz)/2, t_fa)
            cur_x -= w
            
        # border bottom
        c.setStrokeColor(C_LINE)
        c.setLineWidth(0.5)
        c.line(MARGIN_X, ry, MARGIN_X + CONTENT_W, ry)
        
    c.restoreState()
    return y

def draw_chapter_summary(c, cur_y, title_fa, bullet_lines):
    c.saveState()
    box_h = 24 + len(bullet_lines) * 13.5
    y = cur_y - 10 - box_h
    c.setFillColor(C_BRAND_DARK)
    c.roundRect(MARGIN_X, y, CONTENT_W, box_h, 6, fill=1, stroke=0)
    
    # Title
    c.setFont('Vazirmatn-Bold', 9.2)
    c.setFillColor(C_HIGHLIGHT)
    c.drawRightString(MARGIN_X + CONTENT_W - 12, y + box_h - 15, fa(f"★ جمع‌بندی طلایی {title_fa}:"))
    
    # Lines
    c.setFont('Vazirmatn-Medium', 8.2)
    c.setFillColor(C_WHITE)
    ty = y + box_h - 17
    for line in bullet_lines:
        ty -= 13.5
        c.drawRightString(MARGIN_X + CONTENT_W - 16, ty, fa(f"✓  {line}"))
        
    c.restoreState()
    return y

print("Canvas helper components defined.")
