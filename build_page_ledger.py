# Builds analysis/page_ledger.csv for all 241 pages of biochem_full_241p.pdf
import pymupdf as fitz, re, unicodedata, json, csv, collections
SRC='/home/user/HamsYar_Project/sources/biochem_full_241p.pdf'
doc=fitz.open(SRC)
cov=json.load(open('/home/user/HamsYar_Project/analysis/biochem_md_coverage.json'))
STOP=set('و در به از که این است را با یا می های برای آن ها هم یک شود شده دارد نیست بر تا اگر'.split())
UNITS=[(1,10,'U00','شناخت بیوشیمی و سلول (جلسه ۱، استاد خیاطیان)'),
(11,31,'U01','آب، pH و بافر (دکتر افتخار؛ پارت ۱ و ۲)'),
(32,54,'U02','کربوهیدرات‌ها – جلسه ۱ و پارت ۲ (دکتر رحیم‌زاده)'),
(55,69,'U03','کربوهیدرات‌ها – جلسه ۲ (دکتر رحیم‌زاده)'),
(70,90,'U04','اسیدهای آمینه (دکتر رحیم‌زاده)'),
(91,108,'U05','ساختار پروتئین‌ها (دکتر رحیم‌زاده؛ پارت ۱ و ۲)'),
(109,118,'U06','هموپروتئین‌ها، هموگلوبین و میوگلوبین (جلسه ۷، گروه ۲)'),
(119,136,'U07','اسیدهای نوکلئیک (دکتر رحیم‌زاده)'),
(137,151,'U08','همانندسازی DNA (بخش تصویری)'),
(152,176,'U09','لیپیدها (بخش تصویری، صفحه ۱۷۶ دست‌نویس)'),
(177,185,'U10','آنزیم‌ها – بخش ۱ (دکتر فرشیدفر)'),
(186,202,'U10','آنزیم‌ها – بخش ۲ (دکتر فرشیدفر)'),
(203,225,'U11','ویتامین‌ها – بخش ۱ (دکتر داوودیان)'),
(226,241,'U11','ویتامین‌ها – بخش ۲ (دکتر داوودیان)')]
VISUAL_SAMPLED=set([22]+list(range(24,32))+list(range(109,118))+list(range(137,147))+[150,152,158,164,170,176,186,205,229])
def unit_of(p):
    for a,b,u,_ in UNITS:
        if a<=p<=b: return u
    return '?'

H_SET=set([1,11,23,32,39,55,70,81,91,98,119,127,177,203])
E_SET=set([155,213,214])
G_SET=set(list(range(102,109))+list(range(186,203))+list(range(204,213))+list(range(229,242)))
rows=[]
for i,p in enumerate(doc):
    pg=i+1
    raw=p.get_text()
    nimg=len(p.get_images(full=True))
    n=len(raw.strip())
    pf=sum(1 for c in raw if '\ufb50'<=c<='\ufdff' or '\ufe70'<=c<='\ufeff')
    nk=unicodedata.normalize('NFKC',raw)
    words=re.findall(r'[\u0600-\u06FF]+',nk)
    sr=(sum(1 for w in words if w in STOP)/len(words)) if words else 0.0
    single=sum(1 for w in words if len(w)==1)/len(words) if words else 0.0
    if pg in H_SET: st='H'
    elif pg in E_SET: st='E'
    elif pg in G_SET: st='G'
    elif nimg>0 and n<150: st='S'
    else: st='T'
    flags=[]
    if st=='T' and pf>50: flags.append('presentation-forms(NFKC)')
    if st=='T' and single>0.08: flags.append('spaced-letters')
    if st=='T' and n<400 and st!='H': flags.append('short-page')
    size=f"{round(p.rect.width)}x{round(p.rect.height)}"
    if st in ('S','G','E'): vis='REQUIRED (visual reading)'
    elif st=='H': vis='cover/opener text-checked'
    else: vis='text-checked; MD-compared'
    if pg in VISUAL_SAMPLED: vis+=' + thumbnail sampled'
    rows.append(dict(page=pg,size_pt=size,images=nimg,chars=n,pf_chars=pf,status=st,unit=unit_of(pg),
                     md_coverage=(cov.get(str(pg)) if cov.get(str(pg)) is not None else ''),
                     flags='; '.join(flags),visual_check=vis))
with open('/home/user/HamsYar_Project/analysis/page_ledger.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
cnt=collections.Counter(r['status'] for r in rows)
print('status counts:',dict(cnt))
print('unit counts:',dict(collections.Counter(r['unit'] for r in rows)))
for st in 'THGSE':
    print(st, [r['page'] for r in rows if r['status']==st])
print('visual required:',sum(1 for r in rows if r['visual_check'].startswith('REQUIRED')))
print('spaced/PF flags:',sum(1 for r in rows if r['flags']))
