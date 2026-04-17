import ast
import sys
from pathlib import Path

def get_imports(src_dir):
    imports = set()
    for path in Path(src_dir).rglob("*.py"):
        tree = ast.parse(path.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split(".")[0])
    return imports

def get_declared(reqs_file):
    declared = set()
    for line in Path(reqs_file).read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            declared.add(line.lower().split("==")[0].split(">=")[0])
    return declared

imports = get_imports(sys.argv[1])
declared = get_declared(sys.argv[2])

missing = imports - declared
extra = declared - imports

if missing:
    print(f"MISSING in requirements.txt: {missing}")
if extra:
    print(f"EXTRA in requirements.txt: {extra}")
if not missing and not extra:
    print("OK: all imports match requirements.txt")