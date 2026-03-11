#!/usr/bin/env python3
"""
demo.py — demo ishkarim-schema

Schematy i walidacja — JSON-Schema, LinkML, SHACL, Spectral jako bramki CI

Uruchomienie:
    python projects/ishkarim-schema/demo.py
"""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).parents[0] / "src"))
import ishkarim_schema as m
from ishkarim_schema.utils import extract_tags

docs = m.load_knowledge_index()
root = pathlib.Path(__file__).parents[2]

print(f"Schema/Walidacja — {len(docs)} katalogów wiedzy\n")
print("Przykładowe audyty tagów (pierwsze 5 katalogów):")
for doc in docs[:5]:
    tags = extract_tags(root / doc["name"])
    coverage = len([v for v in tags.values() if v]) / max(len(tags), 1)
    print(f"  {doc['name'][:50]:50s}  pokrycie: {coverage:.0%}")

