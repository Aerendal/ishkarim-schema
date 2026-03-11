"""
extracted.py — kod wyekstrahowany z WORK.md dla obszaru schema.

Zawiera 1 fragmentów kodu. Każdy fragment poprzedzony komentarzem
z nazwą katalogu-źródła.
"""
from __future__ import annotations



# ────────────────────────────────────────────────────────────# Source: Pułapki kotwic i aliasów YAML przy haszowaniu
# Wariant Python + ruamel.yaml
from ruamel.yaml import YAML
import hashlib
yaml = YAML()
yaml.sort_base_mapping_type_on_output = True
data = yaml.load(open("config.yml"))
# ... zapis do normalized.yml, hash z bytes
