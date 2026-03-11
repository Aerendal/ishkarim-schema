"""
extracted.py — fragmenty kodu z WORK.md dla obszaru schema.

UWAGA: To są fragmenty referencyjne wyekstrahowane z notatek badawczych.
Mogą wymagać dostosowania przed użyciem w produkcji.

Zawiera 1 fragmentów. Każdy poprzedzony komentarzem ze źródłem.
"""
# ruff: noqa
# type: ignore
from __future__ import annotations

# Source: Pułapki kotwic i aliasów YAML przy haszowaniu
# Wariant Python + ruamel.yaml
from ruamel.yaml import YAML
import hashlib
yaml = YAML()
yaml.sort_base_mapping_type_on_output = True
data = yaml.load(open("config.yml"))
# ... zapis do normalized.yml, hash z bytes
