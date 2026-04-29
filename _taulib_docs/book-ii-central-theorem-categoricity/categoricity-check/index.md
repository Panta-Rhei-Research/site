---
{
  "projection_kind": "taulib_declaration",
  "title": "categoricity_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-categoricity/categoricity-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.Categoricity`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.Categoricity::categoricity_check",
  "declaration_slug": "categoricity-check",
  "kind": "def",
  "name": "categoricity_check",
  "module_name": "TauLib.BookII.CentralTheorem.Categoricity",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/",
  "source_line_start": 184,
  "source_line_end": 190,
  "registry_ids": [
    "II.T42"
  ],
  "related_registry_items": [
    {
      "id": "II.T42",
      "title": "Categoricity",
      "url": "/registry/object/II.T42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L184-L190",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L184-L190",
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
- Source path: [`TauLib/BookII/CentralTheorem/Categoricity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L184-L190)
- Source range: L184-L190
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T42` — Categoricity

## Immediate Comment / Docstring

```lean
/-- [II.T42] Categoricity check: verify that tau^3 is uniquely determined.

    Three components of uniqueness:
    1. Primorial tower is unique (primes are unique)
    2. ABCD chart round-trips perfectly (hyperfactorization is canonical)
    3. Tower coherence is deterministic (reduce is a well-defined function) -/
```

## Source Excerpt

```lean
def categoricity_check (db bound : TauIdx) : Bool :=
  -- 1. Primorial tower uniqueness
  primorial_unique_check db &&
  -- 2. ABCD chart round-trip
  abcd_roundtrip_check bound &&
  -- 3. Reduction determinism: reduce is well-defined
  reduction_determinism_check db bound
```
