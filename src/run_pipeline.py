import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(ROOT/'src'/'collect.py')],check=True)
subprocess.run([sys.executable,str(ROOT/'src'/'build_dashboard.py')],check=True)
