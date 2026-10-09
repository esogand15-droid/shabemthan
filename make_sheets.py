# usage: make_sheets.py "1,10,11,..." [per_sheet=6] [page_width_px=520]
# Writes build/sheets/sheet_<first>-<last>.png, 3 columns x 2 rows (6 per sheet), labelled with page numbers.
import sys, pymupdf
from PIL import Image, ImageDraw, ImageFont
ROOT = "/home/user/HamsYar_Project"
pages = [int(x) for x in sys.argv[1].split(",")]
per = int(sys.argv[2]) if len(sys.argv) > 2 else 6
pw = int(sys.argv[3]) if len(sys.argv) > 3 else 520
doc = pymupdf.open(f"{ROOT}/sources/biochem_full_241p.pdf")
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
except Exception:
    font = ImageFont.load_default()
for s in range(0, len(pages), per):
    chunk = pages[s:s+per]
    ims = []
    for p in chunk:
        pix = doc[p-1].get_pixmap(dpi=96, alpha=False)
        im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        h = int(im.height * pw / im.width)
        ims.append(im.resize((pw, h), Image.LANCZOS))
    cols = 3
    rows = (len(ims) + cols - 1) // cols
    cell_h = max(i.height for i in ims) + 34
    sheet = Image.new("RGB", (cols * (pw + 12) + 12, rows * (cell_h + 12) + 12), (120, 120, 120))
    d = ImageDraw.Draw(sheet)
    for k, (p, im) in enumerate(zip(chunk, ims)):
        r, c = divmod(k, cols)
        x = 12 + c * (pw + 12); y = 12 + r * (cell_h + 12)
        d.rectangle([x, y, x + pw, y + 30], fill=(15, 157, 104))
        d.text((x + 8, y + 3), f"p{p}", fill=(255, 255, 255), font=font)
        sheet.paste(im, (x, y + 32))
    out = f"{ROOT}/build/sheets/sheet_{chunk[0]:03d}-{chunk[-1]:03d}.png"
    sheet.save(out, optimize=True)
    print(out, sheet.size)
