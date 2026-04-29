---
{
  "projection_kind": "taulib_declaration",
  "title": "UniversalBH",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/universal-bh/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.CosmicLife.CrossLimit`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.CrossLimit::UniversalBH",
  "declaration_slug": "universal-bh",
  "kind": "structure",
  "name": "UniversalBH",
  "module_name": "TauLib.BookVI.CosmicLife.CrossLimit",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/",
  "source_line_start": 175,
  "source_line_end": 184,
  "registry_ids": [
    "VI.T36"
  ],
  "related_registry_items": [
    {
      "id": "VI.T36",
      "title": "Universal BH = Fully Alive State",
      "url": "/registry/object/VI.T36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L175-L184",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.CosmicLife.CrossLimit",
        "url": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L175-L184",
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

- Module: [TauLib.BookVI.CosmicLife.CrossLimit](/verify/taulib/docs/book-vi-cosmic-life-cross-limit/)
- Source path: [`TauLib/BookVI/CosmicLife/CrossLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L175-L184)
- Source range: L175-L184
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.T36` — Universal BH = Fully Alive State

## Immediate Comment / Docstring

```lean
/-- [VI.T36] Universal BH: colimit of merger net.
    (i) code = ι_τ exactly
    (ii) All defect functionals vanish
    (iii) 7/7 hallmarks at terminal values
    Colimit existence: V.T117 (Saturation Radius Theorem). -/
```

## Source Excerpt

```lean
structure UniversalBH where
  /-- ω-germ code equals ι_τ exactly. -/
  code_is_iota : Bool := true
  /-- All defect functionals (frame + strong) vanish. -/
  all_defects_zero : Bool := true
  /-- All 7 hallmarks satisfied at terminal values. -/
  hallmark_count : Nat
  /-- Exactly 7 hallmarks. -/
  count_eq : hallmark_count = 7
  deriving Repr
```
