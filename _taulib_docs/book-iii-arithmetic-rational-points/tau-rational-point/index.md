---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRationalPoint",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-rational-points/tau-rational-point/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Arithmetic.RationalPoints`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.RationalPoints::TauRationalPoint",
  "declaration_slug": "tau-rational-point",
  "kind": "structure",
  "name": "TauRationalPoint",
  "module_name": "TauLib.BookIII.Arithmetic.RationalPoints",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-rational-points/",
  "source_line_start": 41,
  "source_line_end": 44,
  "registry_ids": [
    "III.D59"
  ],
  "related_registry_items": [
    {
      "id": "III.D59",
      "title": "τ-Rational Point",
      "url": "/registry/object/III.D59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L41-L44",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.RationalPoints",
        "url": "/verify/taulib/docs/book-iii-arithmetic-rational-points/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L41-L44",
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

- Module: [TauLib.BookIII.Arithmetic.RationalPoints](/verify/taulib/docs/book-iii-arithmetic-rational-points/)
- Source path: [`TauLib/BookIII/Arithmetic/RationalPoints.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L41-L44)
- Source range: L41-L44
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `III.D59` — τ-Rational Point

## Immediate Comment / Docstring

```lean
/-- [III.D59] τ-rational point: stabilizes at finite primorial depth. -/
```

## Source Excerpt

```lean
structure TauRationalPoint where
  value : TauIdx
  stable_depth : TauIdx  -- depth at which it stabilizes
  deriving Repr, DecidableEq, BEq
```
