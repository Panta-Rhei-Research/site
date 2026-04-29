---
{
  "projection_kind": "taulib_declaration",
  "title": "uniqueness_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-categoricity/uniqueness-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.Categoricity`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.Categoricity::uniqueness_check",
  "declaration_slug": "uniqueness-check",
  "kind": "def",
  "name": "uniqueness_check",
  "module_name": "TauLib.BookII.CentralTheorem.Categoricity",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/",
  "source_line_start": 236,
  "source_line_end": 239,
  "registry_ids": [
    "II.C02"
  ],
  "related_registry_items": [
    {
      "id": "II.C02",
      "title": "Uniqueness of Category Tau",
      "url": "/registry/object/II.C02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L236-L239",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.Categoricity",
        "url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L236-L239",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookII.CentralTheorem.Categoricity](/verify/taulib/docs/book-ii-central-theorem-categoricity/)
- Source path: [`TauLib/BookII/CentralTheorem/Categoricity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L236-L239)
- Source range: L236-L239
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.C02` — Uniqueness of Category Tau

## Immediate Comment / Docstring

```lean
/-- [II.C02] Uniqueness check: tau is discovered, not constructed.

    Combines:
    1. Categoricity: the axioms force a unique structure
    2. Moduli singleton: no deformations exist
    3. Liouville dodge: the structure is genuinely different from
       the classical complex case -/
```

## Source Excerpt

```lean
def uniqueness_check (db bound : TauIdx) : Bool :=
  categoricity_check db bound &&
  moduli_singleton_check bound &&
  liouville_dodge_check
```
