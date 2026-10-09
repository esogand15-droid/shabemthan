import json,sys,collections
spans=json.load(open(sys.argv[1]))
pages=[int(x) for x in sys.argv[2].split(',')] if len(sys.argv)>2 else sorted(map(int,spans.keys()))
short=lambda f: f.replace('Vazirmatn-','V-').replace('LiberationSans','LibSans').replace('DejaVuSans','DejaVu')
for pg in pages:
    sp=spans[str(pg)]
    # group by rounded y center
    rows=collections.defaultdict(list)
    for s in sp:
        yc=round((s['bbox'][1]+s['bbox'][3])/2/3)
        rows[yc].append(s)
    print(f"##### PAGE {pg}  spans={len(sp)}")
    for yc in sorted(rows):
        r=sorted(rows[yc],key=lambda s:-s['bbox'][0])  # RTL: right first
        y0=min(s['bbox'][1] for s in r); x0=min(s['bbox'][0] for s in r); x1=max(s['bbox'][2] for s in r)
        txt=' '.join(s['t'] for s in r)
        meta=set(f"{short(s['font'])}/{s['size']}/{s['color']}" for s in r)
        print(f"y{y0:6.1f} x{x0:6.1f}-{x1:6.1f} | {txt[:150]}  || {'; '.join(sorted(meta))[:120]}")
