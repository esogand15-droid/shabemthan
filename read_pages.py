# Print normalized page text for reading. usage: read_pages.py START END [max_chars]
import sys, re, json
ROOT = "/home/user/HamsYar_Project"
idx = json.load(open(f"{ROOT}/build/text/index.json", encoding="utf-8"))
a, b = int(sys.argv[1]), int(sys.argv[2])
maxc = int(sys.argv[3]) if len(sys.argv) > 3 else 60000
out = []
for p in range(a, b + 1):
    t = open(f"{ROOT}/build/text/p{p:03d}.txt", encoding="utf-8").read()
    meta = idx[str(p)]
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    t = t.replace("\n", " ")
    t = re.sub(r"\s{2,}", " ", t)
    out.append(f"=== p{p} [{meta['status']}|{meta['method']}] ===\n{t.strip()}")
s = "\n".join(out)
print(s[:maxc])
if len(s) > maxc: print(f"...[TRUNCATED at {maxc} of {len(s)}; re-run with smaller range]")
