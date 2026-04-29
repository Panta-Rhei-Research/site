---
{
  "projection_kind": "taulib_declaration",
  "title": "OrthodoxComparison",
  "permalink": "/verify/taulib/docs/book-iv-particles-periodic-table/orthodox-comparison/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.PeriodicTable`.",
  "declaration_id": "TauLib.BookIV.Particles.PeriodicTable::OrthodoxComparison",
  "declaration_slug": "orthodox-comparison",
  "kind": "structure",
  "name": "OrthodoxComparison",
  "module_name": "TauLib.BookIV.Particles.PeriodicTable",
  "module_url": "/verify/taulib/docs/book-iv-particles-periodic-table/",
  "source_line_start": 361,
  "source_line_end": 370,
  "registry_ids": [
    "IV.R148"
  ],
  "related_registry_items": [
    {
      "id": "IV.R148",
      "title": "Comparison with orthodox physics",
      "url": "/registry/object/IV.R148/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L361-L370",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L361-L370",
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
- Source path: [`TauLib/BookIV/Particles/PeriodicTable.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L361-L370)
- Source range: L361-L370
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R148` — Comparison with orthodox physics

## Immediate Comment / Docstring

```lean
/-- [IV.R148] In orthodox physics, the five rungs (QCD, nuclear, atomic,
    quantum chemistry, condensed matter) are separate disciplines with
    separate formalisms and effective parameters. In Category τ, all five
    are one continuous ascent on T² with derived scale separations
    κ(C) >> κ(B) >> κ(D) from a single master constant. -/
```

## Source Excerpt

```lean
structure OrthodoxComparison where
  /-- Orthodox: separate disciplines. -/
  orthodox_disciplines : Nat := 5
  /-- Tau: one continuous ascent. -/
  tau_unified : Bool := true
  /-- Scale separations derived. -/
  separations_derived : Bool := true
  /-- Single master constant. -/
  single_constant : Bool := true
  deriving Repr
```
