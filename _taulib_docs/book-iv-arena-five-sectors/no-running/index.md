---
{
  "projection_kind": "taulib_declaration",
  "title": "NoRunning",
  "permalink": "/corpus/taulib/docs/book-iv-arena-five-sectors/no-running/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.FiveSectors`.",
  "declaration_id": "TauLib.BookIV.Arena.FiveSectors::NoRunning",
  "declaration_slug": "no-running",
  "kind": "structure",
  "name": "NoRunning",
  "module_name": "TauLib.BookIV.Arena.FiveSectors",
  "module_url": "/corpus/taulib/docs/book-iv-arena-five-sectors/",
  "source_line_start": 132,
  "source_line_end": 139,
  "registry_ids": [
    "IV.T100"
  ],
  "related_registry_items": [
    {
      "id": "IV.T100",
      "title": "No-Running Principle",
      "url": "/registry/object/IV.T100/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L132-L139",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.FiveSectors",
        "url": "/corpus/taulib/docs/book-iv-arena-five-sectors/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L132-L139",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.Arena.FiveSectors](/corpus/taulib/docs/book-iv-arena-five-sectors/)
- Source path: [`TauLib/BookIV/Arena/FiveSectors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L132-L139)
- Source range: L132-L139
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.T100` — No-Running Principle

## Immediate Comment / Docstring

```lean
/-- [IV.T100] No-Running Principle: coupling constants don't run with energy.
    They are fixed-point readouts of the categorical structure, not
    scale-dependent quantities. β(κ) ≡ 0 for all sector couplings. -/
```

## Source Excerpt

```lean
structure NoRunning where
  /-- β-function vanishes identically. -/
  beta_zero : Bool
  beta_true : beta_zero = true
  /-- Number of fixed couplings. -/
  fixed_count : Nat
  fixed_eq : fixed_count = 15  -- 5 self + 10 cross
  deriving Repr
```
