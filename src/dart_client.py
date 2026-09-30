import os,time
import requests
BASE='https://opendart.fss.or.kr/api'; CORP_CODE='00121288'
class DartError(RuntimeError): pass
def _get(path,params,timeout=60):
 key=os.getenv('DART_API_KEY')
 if not key: raise DartError('DART_API_KEY is not set')
 r=requests.get(f'{BASE}/{path}',params={'crtfc_key':key,**params},headers={'User-Agent':'MY_monami-DART-agent/1.0'},timeout=timeout); r.raise_for_status(); return r
def api_json(path,params):
 d=_get(path,params).json()
 if str(d.get('status'))!='000': raise DartError(f"DART {d.get('status')}: {d.get('message')}")
 return d
def disclosure_list(bgn_de,end_de,detail):
 rows=[]; page=1
 while True:
  d=api_json('list.json',{'corp_code':CORP_CODE,'bgn_de':bgn_de,'end_de':end_de,'pblntf_ty':'A','pblntf_detail_ty':detail,'last_reprt_at':'Y','sort':'date','sort_mth':'asc','page_no':page,'page_count':100}); rows+=d.get('list',[])
  if page>=int(d.get('total_page',1)): break
  page+=1; time.sleep(.12)
 return rows
def financials(year,reprt_code,fs_div='CFS'):
 return api_json('fnlttSinglAcntAll.json',{'corp_code':CORP_CODE,'bsns_year':str(year),'reprt_code':reprt_code,'fs_div':fs_div}).get('list',[])
def download_document(rcept_no,out_path):
 r=_get('document.xml',{'rcept_no':rcept_no},timeout=120); out_path.parent.mkdir(parents=True,exist_ok=True); out_path.write_bytes(r.content); return out_path
