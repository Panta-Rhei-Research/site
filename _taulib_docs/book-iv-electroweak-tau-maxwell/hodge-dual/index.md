---
{
  "projection_kind": "taulib_declaration",
  "title": "HodgeDual",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/hodge-dual/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::HodgeDual",
  "declaration_slug": "hodge-dual",
  "kind": "structure",
  "name": "HodgeDual",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 178,
  "source_line_end": 185,
  "registry_ids": [
    "IV.D102"
  ],
  "related_registry_items": [
    {
      "id": "IV.D102",
      "title": "Hodge Dual of F",
      "url": "/registry/object/IV.D102/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L178-L185",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauMaxwell",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L178-L185",
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

- Module: [TauLib.BookIV.Electroweak.TauMaxwell](/verify/taulib/docs/book-iv-electroweak-tau-maxwell/)
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L178-L185)
- Source range: L178-L185
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D102` — Hodge Dual of F

## Immediate Comment / Docstring

```lean
/-- [IV.D102] Hodge dual *F: the dual 2-form exchanging E ↔ B.
    *F_μν = (1/2)ε_μνρσ F^{ρσ}. EM duality: (E,B) → (B,-E). -/
```

## Source Excerpt

```lean
structure HodgeDual where
  /-- The dual is also a 2-form. -/
  is_two_form : Bool := true
  /-- E ↔ B exchange (with sign). -/
  exchanges_eb : Bool := true
  /-- **F = -F in 4D Lorentzian. -/
  double_dual_minus : Bool := true
  deriving Repr
```
