---
{
  "projection_kind": "taulib_declaration",
  "title": "ForbiddenTransitions",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/forbidden-transitions/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::ForbiddenTransitions",
  "declaration_slug": "forbidden-transitions",
  "kind": "structure",
  "name": "ForbiddenTransitions",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 251,
  "source_line_end": 258,
  "registry_ids": [
    "IV.R125"
  ],
  "related_registry_items": [
    {
      "id": "IV.R125",
      "title": "Forbidden transitions",
      "url": "/registry/object/IV.R125/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L251-L258",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.BetaDecay",
        "url": "/verify/taulib/docs/book-iv-particles-beta-decay/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L251-L258",
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

- Module: [TauLib.BookIV.Particles.BetaDecay](/verify/taulib/docs/book-iv-particles-beta-decay/)
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L251-L258)
- Source range: L251-L258
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R125` — Forbidden transitions

## Immediate Comment / Docstring

```lean
/-- [IV.R125] Transitions with Δl = 0 (e.g., 2s → 1s) are "forbidden"
    because the winding number difference cannot be absorbed by a single
    photon mode. They require higher-order holonomy corrections
    (quadrupole or magnetic dipole). -/
```

## Source Excerpt

```lean
structure ForbiddenTransitions where
  /-- Forbidden: Δl = 0 transitions. -/
  delta_l_zero : Bool := true
  /-- Requires higher-order correction. -/
  requires_higher_order : Bool := true
  /-- Example: 2s → 1s. -/
  example_transition : String := "2s -> 1s"
  deriving Repr
```
