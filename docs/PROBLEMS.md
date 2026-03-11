# PROBLEMS — ishkarim-schema

> Schematy i walidacja — JSON-Schema, LinkML, SHACL, Spectral jako bramki CI

## ✅ Co ten projekt rozwiązuje

- ✅ Automatyczna walidacja dokumentów przed ingestem do bazy wiedzy
- ✅ Bramki CI które odrzucają niekompletne dane (schema-as-policy)
- ✅ Indukcja schematu z przykładów (AutoSchemaKG) — schemat bez ręcznego pisania
- ✅ Roundtrip: LinkML → JSON-Schema → SQLite → z powrotem (bez utraty informacji)
- ✅ Audyt pokrycia — ile wymaganych pól jest wypełnionych?

---

## ❌ Czego ten projekt NIE rozwiązuje

- ❌ Semantic validation — schemat sprawdza strukturę, nie sens danych
- ❌ Schema evolution z automatyczną migracją istniejących danych
- ❌ Walidacja relacji cross-document — tylko per-dokument
- ❌ GUI schema editor

---

## ⚠️ Znane problemy i ograniczenia

- ⚠️ **LinkML → SQLite** nie obsługuje wszystkich typów `union` — wymaga obejścia
- ⚠️ **Spectral linting** jest powolne dla dużych YAML (>1MB) — brak streaming
- ⚠️ **AutoSchemaKG indukcja** daje zbyt ogólne schematy przy małej próbce (<20 dokumentów)
- ⚠️ **SHACL i JSON-Schema** semantycznie się pokrywają — ryzyko duplication w projekcie

---

## 🎯 Przypadki użycia

- 🎯 Data pipeline z gwarancją jakości wejścia (garbage-in prevention)
- 🎯 API gateway który waliduje żądania przed przetwarzaniem
- 🎯 Knowledge base governance — każdy dokument musi przejść schema check w CI
- 🎯 Schema-first development — dokumentacja API generowana ze schematu

---

## 📊 Matryca decyzyjna

| Pytanie | Odpowiedź |
|---------|-----------|
| Czy potrzebujesz GPU? | **NIE** — zaprojektowany dla CPU-only |
| Czy działa offline? | **TAK** — zero zewnętrznych zależności sieciowych |
| Czy jest produkcyjny? | **WZORCE** — referencja do implementacji, nie plug-and-play |
| Czy obsługuje skalowanie? | **LOKALNIE** — single-node, do ~kilku tysięcy dokumentów |
| Licencja? | **MIT** — możesz używać w projektach komercyjnych |

---

## 🔗 Powiązane projekty

Inne moduły Ishkarim które uzupełniają ten projekt:

| Projekt | Relacja |
|---------|---------|
| `ishkarim-rag` | Wyszukiwanie semantyczne nad bazą wiedzy |
| `ishkarim-sqlite` | Trwała pamięć i event-sourcing |
| `ishkarim-agent` | Architektura agentów AI |
| `ishkarim-security` | Bezpieczeństwo systemów AI |
| `ishkarim-bench` | Benchmarki wydajnościowe |

---

*Ostatnia aktualizacja: 2026-03-11 | Generator: `scripts/enrich_projects.py`*
