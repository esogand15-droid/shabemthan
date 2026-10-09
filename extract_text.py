# Build clean per-page text: T pages from PDF text layer; other pages from OCR (fas+eng).
# Output: build/text/pNNN.txt (normalized) and build/text/index.json (method, chars, ocr_conf)
import csv, json, os, re, unicodedata, pymupdf
ROOT = "/home/user/HamsYar_Project"
rows = {int(r["page"]): r for r in csv.DictReader(open(f"{ROOT}/analysis/page_ledger.csv", encoding="utf-8"))}
doc = pymupdf.open(f"{ROOT}/sources/biochem_full_241p.pdf")
AR_DIG = str.maketrans("٠١٢٣٤٥٦٧٨٩", "۰۱۲۳۴۵۶۷۸۹")
def norm(s):
    s = unicodedata.normalize("NFKC", s)          # presentation forms -> base letters
    s = s.replace("\u064A", "\u06CC").replace("\u0643", "\u06A9")  # Arabic yeh/kaf -> Persian
    s = s.replace("\u0640", "")                  # tatweel
    s = s.translate(AR_DIG)
    s = s.replace("\u00a0", " ").replace("\u200b", "")
    return s
def tsv_conf(path):
    if not os.path.exists(path): return None
    confs = []
    with open(path, encoding="utf-8", errors="ignore") as f:
        next(f, None)
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) == 12 and parts[10] not in ("-1", ""):
                try:
                    c = float(parts[10])
                    if parts[11].strip(): confs.append(c)
                except ValueError: pass
    return round(sum(confs) / len(confs), 1) if confs else None
index = {}
for p in range(1, 242):
    r = rows[p]
    if r["status"] == "T":
        raw = doc[p-1].get_text("text")
        method = "pdf-text-layer"; conf = None
    else:
        ocr = f"{ROOT}/build/ocr/p{p:03d}.txt"
        raw = open(ocr, encoding="utf-8").read() if os.path.exists(ocr) else ""
        method = "tesseract-fas+eng" if raw.strip() else "none"
        conf = tsv_conf(f"{ROOT}/build/ocr/p{p:03d}_tsv.tsv")
    txt = norm(raw).strip()
    open(f"{ROOT}/build/text/p{p:03d}.txt", "w", encoding="utf-8").write(txt + "\n")
    index[p] = {"status": r["status"], "unit": r["unit"], "method": method, "chars": len(txt), "ocr_conf": conf}
json.dump(index, open(f"{ROOT}/build/text/index.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
import collections
by = collections.defaultdict(int)
for p, v in index.items(): by[v["unit"]] += v["chars"]
print("chars per unit:", dict(sorted(by.items())), "total", sum(by.values()))
print("empty pages:", [p for p, v in index.items() if v["chars"] < 30])
