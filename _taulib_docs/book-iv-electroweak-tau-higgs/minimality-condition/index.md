---
{
  "projection_kind": "taulib_declaration",
  "title": "MinimalityCondition",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/minimality-condition/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs::MinimalityCondition",
  "declaration_slug": "minimality-condition",
  "kind": "structure",
  "name": "MinimalityCondition",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/",
  "source_line_start": 135,
  "source_line_end": 142,
  "registry_ids": [
    "IV.D137"
  ],
  "related_registry_items": [
    {
      "id": "IV.D137",
      "title": "Minimality Condition",
      "url": "/registry/object/IV.D137/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L135-L142",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L135-L142",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs](/verify/taulib/docs/book-iv-electroweak-tau-higgs/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L135-L142)
- Source range: L135-L142
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D137` — Minimality Condition

## Immediate Comment / Docstring

```lean
/-- [IV.D137] Minimality condition: the first variation of V_n
    vanishes at the physical vacuum. Combined with the positive
    second variation (stability), this characterizes the VEV
    as a strict local minimum modulo the S¹ degeneracy. -/
```

## Source Excerpt

```lean
structure MinimalityCondition where
  /-- First variation vanishes. -/
  first_variation_zero : Bool := true
  /-- Second variation is positive (stability). -/
  second_variation_pos : Bool := true
  /-- The minimum is on the S¹ orbit. -/
  on_circle_orbit : Bool := true
  deriving Repr
```
