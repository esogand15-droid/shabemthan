# -*- coding: utf-8 -*-
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
import arabic_reshaper
from bidi.algorithm import get_display

def fa(text):
    if not text:
        return ""
    reshaped = arabic_reshaper.reshape(str(text))
    return get_display(reshaped)

def wrap_persian_text(text, font_name, font_size, max_width):
    """Wraps Persian text into lines that fit within max_width."""
    # Strip badge prefixes before measuring
    clean_text = str(text)
    for b in ['[CHECK]', '[CROSS]', '[UP]', '[DOWN]', '[EQUAL]']:
        clean_text = clean_text.replace(b, '').strip()
        
    words = clean_text.split()
    if not words:
        return []
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        w = pdfmetrics.stringWidth(fa(test_line), font_name, font_size)
        if w <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
                current_line = [word]
            else:
                lines.append(word)
                current_line = []
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def draw_cell_badge(c, cx, cy, badge_type):
    """
    Renders vector check/cross badges in table cells.
    badge_type: 'CHECK', 'CROSS', 'UP', 'DOWN', 'EQUAL'
    """
    c.saveState()
    r = 6.2
    if badge_type == 'CHECK':
        c.setFillColor(HexColor('#10b981'))
        c.circle(cx, cy, r, fill=1, stroke=0)
        c.setStrokeColor(HexColor('#ffffff'))
        c.setLineWidth(1.4)
        p = c.beginPath()
        p.moveTo(cx - 3.2, cy - 0.2)
        p.lineTo(cx - 0.8, cy - 2.6)
        p.lineTo(cx + 3.4, cy + 2.8)
        c.drawPath(p, fill=0, stroke=1)
    elif badge_type == 'CROSS':
        c.setFillColor(HexColor('#ef4444'))
        c.circle(cx, cy, r, fill=1, stroke=0)
        c.setStrokeColor(HexColor('#ffffff'))
        c.setLineWidth(1.4)
        p = c.beginPath()
        p.moveTo(cx - 2.5, cy - 2.5)
        p.lineTo(cx + 2.5, cy + 2.5)
        p.moveTo(cx - 2.5, cy + 2.5)
        p.lineTo(cx + 2.5, cy - 2.5)
        c.drawPath(p, fill=0, stroke=1)
    elif badge_type == 'UP':
        c.setFillColor(HexColor('#dcfce7'))
        c.setStrokeColor(HexColor('#22c55e'))
        c.roundRect(cx - 15, cy - 6, 30, 12, 3, fill=1, stroke=1)
        c.setFillColor(HexColor('#15803d'))
        c.setFont("Vazirmatn-Bold", 6.8)
        c.drawCentredString(cx, cy - 2.5, fa("افزایش ▲"))
    elif badge_type == 'DOWN':
        c.setFillColor(HexColor('#fee2e2'))
        c.setStrokeColor(HexColor('#ef4444'))
        c.roundRect(cx - 15, cy - 6, 30, 12, 3, fill=1, stroke=1)
        c.setFillColor(HexColor('#b91c1c'))
        c.setFont("Vazirmatn-Bold", 6.8)
        c.drawCentredString(cx, cy - 2.5, fa("کاهش ▼"))
    elif badge_type == 'EQUAL':
        c.setFillColor(HexColor('#f3f4f6'))
        c.setStrokeColor(HexColor('#9ca3af'))
        c.roundRect(cx - 15, cy - 6, 30, 12, 3, fill=1, stroke=1)
        c.setFillColor(HexColor('#4b5563'))
        c.setFont("Vazirmatn-Bold", 6.8)
        c.drawCentredString(cx, cy - 2.5, fa("ثابت ━"))
    c.restoreState()

def draw_table_multiline(c, cur_y, headers, rows, col_widths, margin_x=34, content_w=528.8, font_sz=8.0, row_h=19.0, **kwargs):
    """
    Renders a table with:
    - Smart text wrapping
    - Vector badges for [CHECK], [CROSS], [UP], [DOWN], [EQUAL]
    - Concise visual pills and crisp contrast
    """
    from test_new_components import C_BRAND, C_WHITE, C_SURFACE, C_BRAND_DARK, C_TEXT_BODY, C_LINE
    c.saveState()
    
    # 1. Precalculate row heights and wrapped lines
    header_lines = []
    header_h = 20.0
    for i, h in enumerate(headers):
        lines = wrap_persian_text(h, 'Vazirmatn-Bold', font_sz + 0.2, col_widths[i] - 10)
        header_lines.append(lines)
        h_needed = max(20.0, len(lines) * 11.0 + 8.0)
        if h_needed > header_h:
            header_h = h_needed
            
    prepared_rows = []
    row_heights = []
    for r_idx, row in enumerate(rows):
        r_lines = []
        max_h = 19.0
        for c_idx, cell in enumerate(row):
            raw_cell = str(cell)
            badge = None
            for b in ['[CHECK]', '[CROSS]', '[UP]', '[DOWN]', '[EQUAL]']:
                if raw_cell.startswith(b):
                    badge = b[1:-1]
                    raw_cell = raw_cell[len(b):].strip()
                    break
            
            f_name = 'Vazirmatn-Bold' if c_idx == 0 else 'Vazirmatn-Regular'
            avail_w = col_widths[c_idx] - (24 if badge in ['CHECK', 'CROSS'] else 10)
            lines = wrap_persian_text(raw_cell, f_name, font_sz, avail_w)
            r_lines.append((badge, lines))
            needed = max(19.0, len(lines) * 10.5 + 8.0)
            if needed > max_h:
                max_h = needed
        prepared_rows.append(r_lines)
        row_heights.append(max_h)
        
    total_tbl_h = header_h + sum(row_heights)
    y = cur_y - 6 - total_tbl_h
    
    # Draw Header
    header_top = y + total_tbl_h
    c.setFillColor(C_BRAND)
    c.roundRect(margin_x, header_top - header_h, content_w, header_h, 3.5, fill=1, stroke=0)
    c.setFont('Vazirmatn-Bold', font_sz + 0.2)
    c.setFillColor(C_WHITE)
    
    cur_x = margin_x + content_w
    for i, lines in enumerate(header_lines):
        w = col_widths[i]
        line_start_y = header_top - 6 - font_sz
        if len(lines) == 1:
            line_start_y = header_top - (header_h - font_sz) / 2 - font_sz * 0.8
        for l_idx, line in enumerate(lines):
            c.drawRightString(cur_x - 5, line_start_y - l_idx * 11.0, fa(line))
        cur_x -= w
        
    # Draw Rows
    cur_row_top = header_top - header_h
    for r_idx, (r_lines, rh) in enumerate(zip(prepared_rows, row_heights)):
        ry = cur_row_top - rh
        if r_idx % 2 == 1:
            c.setFillColor(C_SURFACE)
            c.rect(margin_x, ry, content_w, rh, fill=1, stroke=0)
            
        cur_x = margin_x + content_w
        for c_idx, (badge, lines) in enumerate(r_lines):
            w = col_widths[c_idx]
            cell_mid_y = ry + rh / 2.0
            
            # Badge handling
            text_x = cur_x - 5
            if badge in ['UP', 'DOWN', 'EQUAL'] and not lines:
                # Standalone pill centered in cell
                draw_cell_badge(c, cur_x - w / 2.0, cell_mid_y, badge)
            elif badge in ['CHECK', 'CROSS']:
                if not lines:
                    # Standalone icon centered
                    draw_cell_badge(c, cur_x - w / 2.0, cell_mid_y, badge)
                else:
                    # Icon on right side of cell, followed by short label
                    draw_cell_badge(c, cur_x - 11, cell_mid_y, badge)
                    text_x = cur_x - 22
                    
            if lines:
                if c_idx == 0:
                    c.setFont('Vazirmatn-Bold', font_sz)
                    c.setFillColor(C_BRAND_DARK)
                else:
                    c.setFont('Vazirmatn-Regular', font_sz)
                    c.setFillColor(C_TEXT_BODY)
                    
                line_start_y = cur_row_top - 5 - font_sz
                if len(lines) == 1:
                    line_start_y = cur_row_top - (rh - font_sz) / 2 - font_sz * 0.75
                for l_idx, line in enumerate(lines):
                    c.drawRightString(text_x, line_start_y - l_idx * 10.5, fa(line))
            cur_x -= w
            
        # border bottom
        c.setStrokeColor(C_LINE)
        c.setLineWidth(0.4)
        c.line(margin_x, ry, margin_x + content_w, ry)
        cur_row_top = ry
        
    c.restoreState()
    return y

def draw_flow_diagram(c, cur_y, steps, title_fa=None, box_h=35, margin_x=34, content_w=528.8):
    """
    Renders an RTL horizontal process flow diagram with clear wrapped text.
    """
    from test_new_components import (
        C_BRAND_DARK, C_BRAND, C_SURFACE, C_LINE, C_HIGHLIGHT, C_TEXT_BODY, fa
    )
    c.saveState()
    y_start = cur_y - 3
    if title_fa:
        c.setFont("Vazirmatn-Bold", 8.2)
        c.setFillColor(C_BRAND_DARK)
        c.drawRightString(margin_x + content_w - 4, y_start - 6, fa(title_fa))
        y_start -= 15
        
    n = len(steps)
    gap = 13
    total_gaps = gap * (n - 1)
    box_w = (content_w - total_gaps) / n
    box_y = y_start - box_h - 2
    
    for i in range(n):
        x = margin_x + content_w - (i + 1) * box_w - i * gap
        
        c.setFillColor(HexColor('#FFFFFF'))
        c.setStrokeColor(C_LINE)
        c.setLineWidth(0.8)
        c.roundRect(x, box_y, box_w, box_h, 3, fill=1, stroke=1)
        
        c.setFillColor(C_BRAND)
        c.rect(x + box_w - 3.0, box_y, 3.0, box_h, fill=1, stroke=0)
        
        step_title, step_desc = steps[i]
        c.setFont("Vazirmatn-Bold", 7.5)
        c.setFillColor(C_BRAND_DARK)
        tx_title = fa(step_title)
        c.drawCentredString(x + box_w / 2.0 - 1.5, box_y + box_h - 11.0, tx_title)
        
        # Wrap description if needed
        desc_lines = wrap_persian_text(step_desc, "Vazirmatn-Regular", 6.2, box_w - 8)
        c.setFont("Vazirmatn-Regular", 6.2)
        c.setFillColor(C_TEXT_BODY)
        if len(desc_lines) == 1:
            c.drawCentredString(x + box_w / 2.0 - 1.5, box_y + 8.5, fa(desc_lines[0]))
        elif len(desc_lines) >= 2:
            c.drawCentredString(x + box_w / 2.0 - 1.5, box_y + 12.0, fa(desc_lines[0]))
            c.drawCentredString(x + box_w / 2.0 - 1.5, box_y + 4.5, fa(desc_lines[1]))
        
        if i < n - 1:
            arrow_start_x = x - 2
            arrow_end_x = x - gap + 2
            arrow_mid_y = box_y + box_h / 2.0
            
            c.setStrokeColor(C_HIGHLIGHT)
            c.setLineWidth(1.3)
            c.line(arrow_start_x, arrow_mid_y, arrow_end_x + 3.5, arrow_mid_y)
            
            c.setFillColor(C_HIGHLIGHT)
            p = c.beginPath()
            p.moveTo(arrow_end_x, arrow_mid_y)
            p.lineTo(arrow_end_x + 4.5, arrow_mid_y + 3)
            p.lineTo(arrow_end_x + 4.5, arrow_mid_y - 3)
            p.close()
            c.drawPath(p, fill=0, stroke=1)
            
    c.restoreState()
    return box_y - 8

print("test_helpers.py successfully updated with vector badges and clean multiline tables!")
