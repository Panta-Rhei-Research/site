---
{
  "projection_kind": "taulib_declaration",
  "title": "MadelungRule",
  "permalink": "/verify/taulib/docs/book-iv-particles-periodic-table/madelung-rule/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.PeriodicTable`.",
  "declaration_id": "TauLib.BookIV.Particles.PeriodicTable::MadelungRule",
  "declaration_slug": "madelung-rule",
  "kind": "structure",
  "name": "MadelungRule",
  "module_name": "TauLib.BookIV.Particles.PeriodicTable",
  "module_url": "/verify/taulib/docs/book-iv-particles-periodic-table/",
  "source_line_start": 136,
  "source_line_end": 145,
  "registry_ids": [
    "IV.R140"
  ],
  "related_registry_items": [
    {
      "id": "IV.R140",
      "title": "Madelung rule from T^2 geometry",
      "url": "/registry/object/IV.R140/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L136-L145",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L136-L145",
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
- Source path: [`TauLib/BookIV/Particles/PeriodicTable.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/PeriodicTable.lean#L136-L145)
- Source range: L136-L145
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R140` — Madelung rule from T^2 geometry

## Immediate Comment / Docstring

```lean
/-- [IV.R140] The Madelung rule (subshells fill in order of increasing n+l)
    has no first-principles derivation in orthodox physics.

    In Category τ, the breathing eigenvalue on T² with shape ratio ι_τ is
    E_{n,l} ≈ −1/(n + l·ι_τ)², and since ι_τ ≈ 0.34, the n+l ordering
    emerges naturally from the fiber geometry.

    The subshell filling order is:
    1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p, 6s, 4f, ... -/
```

## Source Excerpt

```lean
structure MadelungRule where
  /-- Ordering parameter: n + l. -/
  ordering_param : String := "n + l"
  /-- Origin: breathing eigenvalue on T² with shape ι_τ. -/
  origin : String := "E_{n,l} ~ -1/(n + l*iota_tau)^2"
  /-- No orthodox first-principles derivation. -/
  no_orthodox_derivation : Bool := true
  /-- Tau-framework: emerges from geometry. -/
  tau_derived : Bool := true
  deriving Repr
```
