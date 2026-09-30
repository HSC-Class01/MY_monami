import os,json,io,zipfile,datetime
from pathlib import Path
import pandas as pd
from dart_client import disclosure_list,financials,download_document
from analyze import period_record,add_ratios
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'data'; RAW=DATA/'raw_reports'
def save_json(p,o): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,ensure_ascii=False,indent=2),encoding='utf-8')
def extract_legacy_zip(zp,year,period):
 out=[]
 try:
  with zipfile.ZipFile(zp) as z:
   for n in z.namelist():
    if not n.lower().endswith(('.xml','.html','.htm')): continue
    try:
     raw=z.read(n); txt=raw.decode('utf-8','ignore')
     if not any(k in txt for k in ['매출액','영업이익','자산총계','부채총계','자본총계']): continue
     for t in pd.read_html(io.BytesIO(raw)):
      for _,row in t.astype(str).iterrows():
       s=' '.join(row.tolist())
       if any(k in s for k in ['매출액','영업이익','자산총계','부채총계','자본총계']): out.append({'source':n,'row':row.tolist()})
    except Exception: pass
 except Exception: pass
 save_json(DATA/f'legacy_extract_{year}_{period}.json',out)
def main():
 if not os.getenv('DART_API_KEY'): raise SystemExit('DART_API_KEY secret is required.')
 RAW.mkdir(parents=True,exist_ok=True); disclosures=[]
 for detail,period in [('A001','annual'),('A002','half'),('A003','quarter')]:
  for r in disclosure_list('20100101','20991231',detail):
   r['period_group']=period; disclosures.append(r); year=int(r['rcept_dt'][:4])
   if os.getenv('SAVE_RAW_REPORTS','true').lower()=='true':
    p=RAW/str(year)/f"{r['rcept_no']}_{period}.zip"
    if not p.exists():
     download_document(r['rcept_no'],p)
     if year<2015: extract_legacy_zip(p,year,period)
 save_json(DATA/'disclosures.json',disclosures); records=[]
 for year in range(2015,datetime.datetime.now().year+1):
  for period,code in [('annual','11011'),('half','11012'),('quarter1','11013'),('quarter3','11014')]:
   for fs in ['CFS','OFS']:
    try:
     rs=financials(year,code,fs)
     if rs: records.append(period_record(rs,year,period,fs))
    except Exception as e: print('skip',year,period,fs,e)
 df=pd.DataFrame(records)
 if not df.empty:
  df['fs_rank']=df.fs_div.map({'CFS':0,'OFS':1}).fillna(9); df=df.sort_values(['year','period','fs_rank']).drop_duplicates(['year','period']).drop(columns='fs_rank'); df=add_ratios(df); df.to_json(DATA/'financials.json',orient='records',force_ascii=False,indent=2); df.to_csv(DATA/'financials.csv',index=False,encoding='utf-8-sig')
 else: (DATA/'financials.json').write_text('[]',encoding='utf-8')
if __name__=='__main__': main()
