# Render non-T pages at 300 dpi and OCR them with tesseract (fas+eng).
# Output: build/ocr/pNNN.txt (plain text), build/ocr/pNNN.tsv (word confidences), build/img/pNNN.png
import csv, subprocess, sys, os, pymupdf
from concurrent.futures import ThreadPoolExecutor
ROOT = "/home/user/HamsYar_Project"
PDF = f"{ROOT}/sources/biochem_full_241p.pdf"
rows = list(csv.DictReader(open(f"{ROOT}/analysis/page_ledger.csv", encoding="utf-8")))
targets = [int(r["page"]) for r in rows if r["status"] != "T"]
doc = pymupdf.open(PDF)
def job(p):
    png = f"{ROOT}/build/img/p{p:03d}.png"
    if not os.path.exists(png):
        pix = doc[p-1].get_pixmap(dpi=300, alpha=False)
        pix.save(png)
    out = f"{ROOT}/build/ocr/p{p:03d}"
    if not os.path.exists(out + ".txt"):
        subprocess.run(["tesseract", png, out, "-l", "fas+eng", "--psm", "3", "-c", "preserve_interword_spaces=1"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        subprocess.run(["tesseract", png, out + "_tsv", "-l", "fas+eng", "--psm", "3", "tsv"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    return p
with ThreadPoolExecutor(max_workers=int(sys.argv[1]) if len(sys.argv) > 1 else 1) as ex:
    done = 0
    for p in ex.map(job, targets):
        done += 1
        if done % 10 == 0 or done == len(targets):
            print(f"ocr done {done}/{len(targets)} (last p{p})", flush=True)
print("ALL_DONE", len(targets), flush=True)
