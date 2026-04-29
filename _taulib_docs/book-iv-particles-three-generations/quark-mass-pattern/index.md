---
{
  "projection_kind": "taulib_declaration",
  "title": "QuarkMassPattern",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/quark-mass-pattern/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::QuarkMassPattern",
  "declaration_slug": "quark-mass-pattern",
  "kind": "structure",
  "name": "QuarkMassPattern",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 300,
  "source_line_end": 309,
  "registry_ids": [
    "IV.P121"
  ],
  "related_registry_items": [
    {
      "id": "IV.P121",
      "title": "Quark mass pattern",
      "url": "/registry/object/IV.P121/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L300-L309",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L300-L309",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L300-L309)
- Source range: L300-L309
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P121` — Quark mass pattern

## Immediate Comment / Docstring

```lean
/-- [IV.P121] Six quark masses follow approximate ι_τ power laws.
    Scope: conjectural — reproduces ordering and scale, not high-precision.

    Exponents (×10, for integer representation):
    u ≈ 5.8, d ≈ 5.0, c ≈ −0.30, s ≈ 2.2, t ≈ −4.5, b ≈ −1.5 -/
```

## Source Excerpt

```lean
structure QuarkMassPattern where
  /-- Scope label. -/
  scope : String := "tau-effective"
  /-- Correctly reproduces mass ordering within generations. -/
  ordering_correct : Bool := true
  /-- Correctly reproduces generation hierarchy. -/
  hierarchy_correct : Bool := true
  /-- Digit-level predictions: NO. -/
  digit_level : Bool := false
  deriving Repr
```
