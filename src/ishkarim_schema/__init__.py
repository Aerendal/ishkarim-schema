"""
ishkarim_schema — moduł z obszaru schema.

Schematy i walidacja: JSON-Schema, LinkML, SHACL, Spectral, audyt kompletności.

Źródła: 7 katalogów z repozytorium Ishkarim.
"""
from __future__ import annotations

__version__ = "0.1.0"
__area__ = "schema"



MODULES: list[str] = [
    'Audyt kompletności dokumentu z użyciem AST',
    'DocSchema',
    'Harness kompletności dokumentacji i testy CI',
    'JSON-Schema diff z natychmiastowym blokiem CI',
    'Minimalny ślad licencyjny dla asetów GBA',
    'Playbook zarządzania cyklem życia rejestru',
    'Pułapki kotwic i aliasów YAML przy haszowaniu',
]


_REPO_ROOT: str | None = None


def _find_repo_root() -> str:
    """Auto-discover the Ishkarim repo root by walking up from __file__."""
    from pathlib import Path
    p = Path(__file__).resolve().parent
    for _ in range(10):
        if (p / "CATALOG.md").exists() or (p / "CHANGELOG.md").exists():
            return str(p)
        p = p.parent
    return str(Path(__file__).resolve().parents[5])  # fallback


def load_knowledge_index(root: str | None = None) -> list[dict]:
    """
    Zwraca listę rekordów ze wszystkich katalogów-źródeł obszaru.

    Args:
        root: ścieżka do katalogu głównego repozytorium (opcjonalne)

    Returns:
        Lista słowników z kluczami: name, doc_id, maturity, area
    """
    import re
    from pathlib import Path

    if root is None:
        root = _find_repo_root()

    results = []
    for name in MODULES:
        tags_path = Path(root) / name / "TAGS.md"
        if not tags_path.exists():
            continue
        tags = tags_path.read_text(errors="replace")
        doc_id = ""
        maturity = "draft"
        m = re.search(r"^doc_id:\s*(\S+)", tags, re.M)
        if m:
            doc_id = m.group(1)
        m2 = re.search(r"^maturity:\s*(\S+)", tags, re.M)
        if m2:
            maturity = m2.group(1)
        results.append({"name": name, "doc_id": doc_id, "maturity": maturity, "area": "schema"})
    return results


__all__ = ["MODULES", "load_knowledge_index", "__version__", "__area__"]
