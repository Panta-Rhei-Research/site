---
{
  "projection_kind": "taulib_declaration",
  "title": "ParityViolation",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/parity-violation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakChirality`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality::ParityViolation",
  "declaration_slug": "parity-violation",
  "kind": "structure",
  "name": "ParityViolation",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/",
  "source_line_start": 212,
  "source_line_end": 219,
  "registry_ids": [
    "IV.D114"
  ],
  "related_registry_items": [
    {
      "id": "IV.D114",
      "title": "Parity Operator",
      "url": "/registry/object/IV.D114/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L212-L219",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakChirality",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L212-L219",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality](/verify/taulib/docs/book-iv-electroweak-weak-chirality/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L212-L219)
- Source range: L212-L219
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D114` — Parity Operator

## Immediate Comment / Docstring

```lean
/-- [IV.D114] Parity violation measure V(S) for sector S:
    V = 0 for parity-preserving, V = 100 for maximal violation.
    The weak sector has V = 100 (couples only to left-handed fermions). -/
```

## Source Excerpt

```lean
structure ParityViolation where
  /-- Sector. -/
  sector : Sector
  /-- Violation measure: 0 (preserving) or 100 (maximal), scaled. -/
  violation : Nat
  /-- Bounded by 100. -/
  bounded : violation ≤ 100
  deriving Repr
```
