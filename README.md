# ishkarim-schema

> Schematy i walidacja: JSON-Schema, LinkML, SHACL, Spectral, audyt kompletności.

## Instalacja

```bash
pip install -e projects/ishkarim-schema
```

Lub lokalnie z tego repozytorium:

```bash
cd projects/ishkarim-schema
pip install -e ".[dev]"
```

## Użycie

```python
import ishkarim_schema as m

# Lista dostępnych modułów
print(m.MODULES)

# Wczytaj indeks wiedzy
docs = m.load_knowledge_index()
```

## Obszar tematyczny

Ten projekt agreguje wiedzę z **7 katalogów** obszaru `schema`:

- `Audyt kompletności dokumentu z użyciem AST`
- `DocSchema`
- `Harness kompletności dokumentacji i testy CI`
- `JSON-Schema diff z natychmiastowym blokiem CI`
- `Minimalny ślad licencyjny dla asetów GBA`
- `Playbook zarządzania cyklem życia rejestru`
- `Pułapki kotwic i aliasów YAML przy haszowaniu`

## Przykładowe źródła

### Audyt kompletności dokumentu z użyciem AST

# WORK: Audyt kompletności dokumentu z użyciem AST
## 0-Metadane
- Katalog: Audyt kompletności dokumentu z użyciem AST
- Pliki: 16 (bez placeholderów)
- Tagi: AST, audyt-dokumentów, kompletność, Pandoc, mdast, remark, JSON-Schema, CI, SQLite, SARIF, bramki-jakości, docs-as-code, Python-CLI, linting

### DocSchema

# DocSchema
## 0-Metadane
- Pliki: 9 (PROJ-DOCSCHEMA.md, PROJECT.md, README.md, SDRS-ADE-PLAN.md, SELF-DEVELOPMENT.md, WORK.md, INDEX.md, pyproject.toml, docschema_cli.py + podkatalogi src/, docs/, model/, sections/, templates/, tests/)
- Tagi: docs-as-code, schema, validation, governance, generation, traceability, metamodel, CLI, Python
- Status: done

### Harness kompletności dokumentacji i testy CI

# WORK: Harness kompletności dokumentacji i testy CI
## 0-Metadane
- Katalog: Harness kompletności dokumentacji i testy CI
- Pliki: 19 (bez placeholderów)
- Tagi: ci, documentation-quality, openapi, json-schema, spectral, oasdiff, sarif, vale, linting, breaking-changes, determinism, github-actions


## Struktura projektu

```
ishkarim-schema/
├── pyproject.toml        # installable package
├── README.md
├── MODULES.md            # pełny indeks 7 katalogów-źródeł
├── src/
│   └── ishkarim_schema/
│       ├── __init__.py   # publiczne API
│       ├── utils.py      # wspólne narzędzia
│       └── *.py          # kod wyekstrahowany z WORK.md
├── tests/
│   ├── __init__.py
│   └── test_schema.py
└── docs/
    ├── overview.md
    └── sources.md
```

## Testy

```bash
pytest projects/ishkarim-schema/tests/ -v
```

## Źródło danych

Katalogi źródłowe znajdują się w katalogu głównym repozytorium Ishkarim.
Każdy katalog zawiera `WORK.md` (notatki badawcze) i `TAGS.md` (metadane).

---
*Wygenerowano automatycznie przez `scripts/build_projects.py`*
