#!/usr/bin/env python3.12
"""
Roda todos os scripts de geração/atualização do site estático em ordem.
Uso: python3.12 scripts/run_all.py
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCRIPTS = ROOT / "scripts"

SCRIPT_ORDER = [
    "01-build_static.py",
    "02-cleanup.py",
    "03-fix_missing.py",
    "04-final_fix.py",
    "05-final_cleanup.py",
    "06-deploy_improvements.py",
    "07-gen_docs.py",
]

PY = sys.executable  # python3.12

print("=" * 70)
print("Fandango em Cananéia - Gerador de site estático")
print("=" * 70)
print()

for i, name in enumerate(SCRIPT_ORDER, 1):
    script = SCRIPTS / name
    if not script.exists():
        print(f"  ⚠ FALTA: {name}")
        continue
    print(f"[{i}/{len(SCRIPT_ORDER)}] Rodando {name}...")
    print("-" * 70)
    result = subprocess.run([PY, str(script)], cwd=ROOT)
    if result.returncode != 0:
        print(f"  ✗ ERRO em {name} (código {result.returncode})")
        sys.exit(1)
    print()

print("=" * 70)
print("✅ Site estático gerado com sucesso!")
print("=" * 70)
print()
print("Próximos passos:")
print("  1. Abra site/index.html no navegador (ou use 'python3 -m http.server' em site/)")
print("  2. Para deploy: copie o conteúdo de site/ para a raiz do servidor web")
print("  3. O .htaccess já configura HTTPS, URLs limpas e redirects 301")
print()
