---
{
  "projection_kind": "taulib_declaration",
  "title": "temporal_complement_identity",
  "permalink": "/verify/taulib/docs/book-iv-physics-internal-equations/temporal-complement-identity/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.InternalEquations`.",
  "declaration_id": "TauLib.BookIV.Physics.InternalEquations::temporal_complement_identity",
  "declaration_slug": "temporal-complement-identity",
  "kind": "def",
  "name": "temporal_complement_identity",
  "module_name": "TauLib.BookIV.Physics.InternalEquations",
  "module_url": "/verify/taulib/docs/book-iv-physics-internal-equations/",
  "source_line_start": 138,
  "source_line_end": 144,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L138-L144",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.InternalEquations",
        "url": "/verify/taulib/docs/book-iv-physics-internal-equations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L138-L144",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIV.Physics.InternalEquations](/verify/taulib/docs/book-iv-physics-internal-equations/)
- Source path: [`TauLib/BookIV/Physics/InternalEquations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/InternalEquations.lean#L138-L144)
- Source range: L138-L144
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The temporal complement κ_A + κ_D = 1 as an internal identity.
    Ontologically: the weak and gravitational self-couplings exhaust
    the base τ¹ — every α-tick is either weak or gravitational. -/
```

## Source Excerpt

```lean
def temporal_complement_identity : InternalIdentity where
  name := "Temporal complement κ_A + κ_D = 1"
  layer := .InternalPhysics
  source_sector := .A
  target_sector := .D
  is_dimensionless := true
  from_iota_alone := true
```
