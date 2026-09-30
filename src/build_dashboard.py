import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'data'; OUT=ROOT/'dashboard'
def main():
 rows=json.loads((DATA/'financials.json').read_text(encoding='utf-8')) if (DATA/'financials.json').exists() else []
 peers=json.loads((DATA/'peerfirms.json').read_text(encoding='utf-8'))
 OUT.mkdir(exist_ok=True); (OUT/'data.json').write_text(json.dumps({'company':{'name':'모나미','ticker':'005360','corp_code':'00121288'},'rows':rows,'peers':peers},ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__': main()
