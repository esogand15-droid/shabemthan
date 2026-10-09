import sys, os
from render_pages import build_pdf
from render_ch1_to_ch6 import draw_ch1_to_ch6
from render_ch7_to_ch12 import draw_ch7_to_ch12
from render_ch13_to_ch14 import draw_ch13_to_ch14

OUTPUT_PDF = "HamsYar_Biochemistry_Night_Before_Exam.pdf"

print("Starting complete 40-page booklet compilation...")
c = build_pdf(OUTPUT_PDF)
draw_ch1_to_ch6(c)
draw_ch7_to_ch12(c)
draw_ch13_to_ch14(c)
c.save()

print(f"SUCCESS: {OUTPUT_PDF} generated successfully!")
