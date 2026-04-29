---
{
  "projection_kind": "taulib_declaration",
  "title": "ChargConjugation",
  "permalink": "/verify/taulib/docs/book-iv-physics-holonomy-correction/charg-conjugation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Physics.HolonomyCorrection`.",
  "declaration_id": "TauLib.BookIV.Physics.HolonomyCorrection::ChargConjugation",
  "declaration_slug": "charg-conjugation",
  "kind": "structure",
  "name": "ChargConjugation",
  "module_name": "TauLib.BookIV.Physics.HolonomyCorrection",
  "module_url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/",
  "source_line_start": 239,
  "source_line_end": 246,
  "registry_ids": [
    "IV.R12"
  ],
  "related_registry_items": [
    {
      "id": "IV.R12",
      "title": "Charge Conjugation",
      "url": "/registry/object/IV.R12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L239-L246",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.HolonomyCorrection",
        "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L239-L246",
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

- Module: [TauLib.BookIV.Physics.HolonomyCorrection](/verify/taulib/docs/book-iv-physics-holonomy-correction/)
- Source path: [`TauLib/BookIV/Physics/HolonomyCorrection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L239-L246)
- Source range: L239-L246
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R12` — Charge Conjugation

## Immediate Comment / Docstring

```lean
/-- [IV.R12] Charge conjugation kills the first-order holonomy term.

    Under charge conjugation C: α → −α (the U(1) connection reverses).
    The holonomy expansion is:

      Hol(A) = 1 + iα·∮A + (iα)²/2·(∮A)² + ...

    The leading correction (∝ α) averages to zero under C.
    The first surviving correction is ∝ α².

    This is why the Level 1+ formula has π³α² and not π³α. -/
```

## Source Excerpt

```lean
structure ChargConjugation where
  /-- The first surviving order. -/
  surviving_order : Nat := 2
  /-- The killed order. -/
  killed_order : Nat := 1
  /-- Physical mechanism. -/
  mechanism : String := "C: α → −α averages out odd powers"
  deriving Repr
```
