---
{
  "projection_kind": "taulib_declaration",
  "title": "QEDCorrections",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/qedcorrections/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::QEDCorrections",
  "declaration_slug": "qedcorrections",
  "kind": "structure",
  "name": "QEDCorrections",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 452,
  "source_line_end": 461,
  "registry_ids": [
    "IV.P49"
  ],
  "related_registry_items": [
    {
      "id": "IV.P49",
      "title": "Perturbative Expansion in alpha",
      "url": "/registry/object/IV.P49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L452-L461",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L452-L461",
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
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L452-L461)
- Source range: L452-L461
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P49` — Perturbative Expansion in alpha

## Immediate Comment / Docstring

```lean
/-- [IV.P49] Quantum corrections as power series in α:
    tree-level → one-loop (α) → two-loop (α²) → ...
    The series is asymptotic; convergence controlled by α ≈ 1/137. -/
```

## Source Excerpt

```lean
structure QEDCorrections where
  /-- Coupling constant inverse (≈ 137). -/
  alpha_inverse_approx : Nat
  inv_range : alpha_inverse_approx > 130 ∧ alpha_inverse_approx < 140
  /-- Series is asymptotic (not convergent). -/
  is_asymptotic : Bool := true
  /-- Leading correction order. -/
  leading_order : Nat
  order_eq : leading_order = 1  -- one-loop
  deriving Repr
```
