import pandas as pd
ALIASES={'revenue':['매출액','수익(매출액)','영업수익'],'gross_profit':['매출총이익'],'operating_income':['영업이익','영업이익(손실)'],'net_income':['당기순이익','당기순이익(손실)'],'cash':['현금및현금성자산','현금및현금성자산 및 단기금융상품'],'receivables':['매출채권','매출채권 및 기타채권'],'inventory':['재고자산'],'current_assets':['유동자산'],'current_liabilities':['유동부채'],'assets':['자산총계'],'liabilities':['부채총계'],'equity':['자본총계'],'borrowings':['단기차입금','장기차입금','유동성장기차입금','사채','장기차입금및사채'],'interest_expense':['이자비용'],'cfo':['영업활동으로 인한 현금흐름','영업활동현금흐름'],'capex':['유형자산의 취득','유형자산 취득','유형자산의 취득액']}
def num(x):
 try:
  s=str(x).replace(',','').replace(' ',''); return None if s in ('','nan','None','-','—') else float(s)
 except: return None
def pick(rows,key):
 for row in rows:
  nm=str(row.get('account_nm','')).strip()
  if any(a==nm or a in nm for a in ALIASES[key]): return num(row.get('thstrm_add_amount') or row.get('thstrm_amount'))
 return None
def period_record(rows,year,period,fs_div):
 d={'year':int(year),'period':period,'fs_div':fs_div}
 for k in ALIASES:d[k]=pick(rows,k)
 return d
def safe(a,b): return None if a is None or b in (None,0) else a/b
def add_ratios(df):
 df=df.sort_values(['year','period']).copy()
 for c in ALIASES: df[c]=pd.to_numeric(df[c],errors='coerce')
 df['gross_margin']=df.apply(lambda r:safe(r.gross_profit,r.revenue)*100,axis=1); df['operating_margin']=df.apply(lambda r:safe(r.operating_income,r.revenue)*100,axis=1); df['net_margin']=df.apply(lambda r:safe(r.net_income,r.revenue)*100,axis=1)
 df['current_ratio']=df.apply(lambda r:safe(r.current_assets,r.current_liabilities)*100,axis=1); df['debt_ratio']=df.apply(lambda r:safe(r.liabilities,r.equity)*100,axis=1); df['equity_ratio']=df.apply(lambda r:safe(r.equity,r.assets)*100,axis=1); df['debt_dependence']=df.apply(lambda r:safe(r.borrowings,r.assets)*100,axis=1)
 df['net_debt']=df.apply(lambda r:(r.borrowings-r.cash) if pd.notna(r.borrowings) and pd.notna(r.cash) else None,axis=1); df['interest_coverage']=df.apply(lambda r:safe(r.operating_income,r.interest_expense),axis=1); df['fcf']=df.apply(lambda r:(r.cfo-r.capex) if pd.notna(r.cfo) and pd.notna(r.capex) else None,axis=1); df['cfo_net_income']=df.apply(lambda r:safe(r.cfo,r.net_income),axis=1)
 df['revenue_growth']=df.groupby('period')['revenue'].pct_change()*100; df['avg_assets']=df.groupby('period')['assets'].transform(lambda s:(s+s.shift(1))/2); df['avg_equity']=df.groupby('period')['equity'].transform(lambda s:(s+s.shift(1))/2)
 df['roa']=df.apply(lambda r:safe(r.net_income,r.avg_assets)*100,axis=1); df['roe']=df.apply(lambda r:safe(r.net_income,r.avg_equity)*100,axis=1); df['asset_turnover']=df.apply(lambda r:safe(r.revenue,r.avg_assets),axis=1); return df
