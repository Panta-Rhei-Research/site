---
{
  "projection_kind": "taulib_declaration",
  "title": "EMConnectionA",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/emconnection-a/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauMaxwell`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauMaxwell::EMConnectionA",
  "declaration_slug": "emconnection-a",
  "kind": "structure",
  "name": "EMConnectionA",
  "module_name": "TauLib.BookIV.Electroweak.TauMaxwell",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-maxwell/",
  "source_line_start": 96,
  "source_line_end": 105,
  "registry_ids": [
    "IV.D99"
  ],
  "related_registry_items": [
    {
      "id": "IV.D99",
      "title": "EM Connection 1-Form",
      "url": "/registry/object/IV.D99/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L96-L105",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L96-L105",
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
- Source path: [`TauLib/BookIV/Electroweak/TauMaxwell.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauMaxwell.lean#L96-L105)
- Source range: L96-L105
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D99` — EM Connection 1-Form

## Immediate Comment / Docstring

```lean
/-- [IV.D99] EM connection 1-form A = A_μ dx^μ on P_EM.
    In local coordinates: 4 component functions A_0, A_1, A_2, A_3
    where A_0 = scalar potential φ and (A_1,A_2,A_3) = vector potential. -/
```

## Source Excerpt

```lean
structure EMConnectionA where
  /-- Number of components (spacetime dimension). -/
  components : Nat
  comp_eq : components = 4
  /-- Scalar potential component (index 0). -/
  has_scalar_potential : Bool := true
  /-- Vector potential components (indices 1,2,3). -/
  vector_potential_dim : Nat
  vec_eq : vector_potential_dim = 3
  deriving Repr
```
