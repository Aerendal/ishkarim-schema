# ishkarim-schema

> **Schematy i walidacja — JSON-Schema, LinkML, SHACL, Spectral jako bramki CI**

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![CPU-only](https://img.shields.io/badge/CPU-only-orange)]()

## Problem, który rozwiązujemy

- Automatyczna walidacja dokumentów przed ingestem do bazy wiedzy
- Bramki CI które odrzucają niekompletne dane (schema-as-policy)
- Indukcja schematu z przykładów (AutoSchemaKG) — schemat bez ręcznego pisania

Pełna lista → [docs/PROBLEMS.md](docs/PROBLEMS.md)

## Szybki start

```bash
# Instalacja
pip install -e projects/ishkarim-schema

# Demo (10 sekund)
python projects/ishkarim-schema/demo.py
```

## Użycie w kodzie

```python
import ishkarim_schema as m

# Wszystkie 7 katalogi wiedzy obszaru 'schema'
docs = m.load_knowledge_index()
print(f"{len(docs)} katalogów | obszar: {m.__area__}")

# Narzędzia pomocnicze
from ishkarim_schema.utils import read_work_md, extract_tags, extract_python_blocks
```

## Dla kogo

- Data pipeline z gwarancją jakości wejścia (garbage-in prevention)
- API gateway który waliduje żądania przed przetwarzaniem
- Knowledge base governance — każdy dokument musi przejść schema check w CI

## Dokumentacja

| Plik | Zawartość |
|------|-----------|
| [docs/PROBLEMS.md](docs/PROBLEMS.md) | Co rozwiązuje / czego nie / znane problemy |
| [docs/api.md](docs/api.md) | Dokumentacja API |
| [docs/overview.md](docs/overview.md) | Przegląd obszaru |
| [docs/sources.md](docs/sources.md) | Źródłowe katalogi wiedzy |
| [MODULES.md](MODULES.md) | Pełny indeks 7 katalogów |

## Testy i benchmarki

```bash
# Testy jednostkowe
pytest tests/test_schema.py -v

# Testy domenowe (z prawdziwymi danymi)
pytest tests/test_schema_domain.py -v

# Benchmarki wydajnościowe
python benchmarks/bench_schema.py --quick
```

## Struktura projektu

```
ishkarim-schema/
├── demo.py                    ← uruchom mnie
├── pyproject.toml
├── README.md
├── MODULES.md                 ← 7 katalogów-źródeł
├── docs/
│   ├── PROBLEMS.md            ← co rozwiązuje / czego nie
│   ├── api.md                 ← dokumentacja API
│   ├── overview.md
│   └── sources.md
├── src/ishkarim_schema/
│   ├── __init__.py            ← MODULES list + load_knowledge_index()
│   ├── utils.py               ← read_work_md, extract_tags, extract_python_blocks
│   └── snippets/              ← kod z WORK.md (referencyjny)
├── tests/
│   ├── test_schema.py         ← testy jednostkowe
│   └── test_schema_domain.py  ← testy domenowe
└── benchmarks/
    └── bench_schema.py        ← benchmarki wydajnościowe
```

## Ograniczenia

> ⚠️ To projekt **referencyjny** — wzorce i wiedza, nie gotowa biblioteka produkcyjna.
> Przed wdrożeniem produkcyjnym przeczytaj [docs/PROBLEMS.md](docs/PROBLEMS.md).

---

*Część ekosystemu [Ishkarim](../../README.md) — 7 katalogów wiedzy obszaru `schema`*
*Wygenerowano: 2026-03-11 | `scripts/build_projects.py` + `scripts/enrich_projects.py`*
