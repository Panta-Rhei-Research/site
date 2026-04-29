---
{
  "projection_kind": "taulib_declaration",
  "title": "CovalentBond",
  "permalink": "/verify/taulib/docs/book-iv-particles-periodic-table/covalent-bond/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.PeriodicTable`.",
  "declaration_id": "TauLib.BookIV.Particles.PeriodicTable::CovalentBond",
  "declaration_slug": "covalent-bond",
  "kind": "structure",
  "name": "CovalentBond",
  "module_name": "TauLib.BookIV.Particles.PeriodicTable",
  "module_url": "/verify/taulib/docs/book-iv-particles-periodic-table/",
  "source_line_start": 214,
  "source_line_end": 221,
  "registry_ids": [
    "IV.D205"
  ],
  "related_registry_items": [
    {
      "id": "IV.D205",
      "title": "Covalent bond",
      "url": "/registry/object/IV.D205/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L214-L221",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.PeriodicTable",
        "url": "/verify/taulib/docs/book-iv-particles-periodic-table/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L214-L221",
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

- Module: [TauLib.BookIV.Particles.PeriodicTable](/verify/taulib/docs/book-iv-particles-periodic-table/)
- Source path: [`TauLib/BookIV/Particles/PeriodicTable.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L214-L221)
- Source range: L214-L221
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D205` — Covalent bond

## Immediate Comment / Docstring

```lean
/-- [IV.D205] A covalent bond of order k: k electron winding modes on T²
    contribute simultaneously to shell closure of both atoms.
    - k=1: single bond (e.g., H₂)
    - k=2: double bond (e.g., O=O)
    - k=3: triple bond (e.g., N≡N)

    Bond strength increases with k via mode-overlap integrals. -/
```

## Source Excerpt

```lean
structure CovalentBond where
  /-- Bond order. -/
  order : Nat
  /-- Example molecule. -/
  example_mol : String
  /-- Order is 1, 2, or 3. -/
  order_valid : order ≥ 1 ∧ order ≤ 3
  deriving Repr
```
