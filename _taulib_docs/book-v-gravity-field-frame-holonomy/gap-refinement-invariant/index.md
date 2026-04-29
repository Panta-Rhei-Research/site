---
{
  "projection_kind": "taulib_declaration",
  "title": "gap_refinement_invariant",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/gap-refinement-invariant/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::gap_refinement_invariant",
  "declaration_slug": "gap-refinement-invariant",
  "kind": "theorem",
  "name": "gap_refinement_invariant",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 334,
  "source_line_end": 336,
  "registry_ids": [
    "V.P11"
  ],
  "related_registry_items": [
    {
      "id": "V.P11",
      "title": "Gap refinement coherence",
      "url": "/registry/object/V.P11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L334-L336",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.FrameHolonomy",
        "url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L334-L336",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookV.GravityField.FrameHolonomy](/verify/taulib/docs/book-v-gravity-field-frame-holonomy/)
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L334-L336)
- Source range: L334-L336
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P11` — Gap refinement coherence

## Immediate Comment / Docstring

```lean
/-- [V.P11] Total gap refinement invariance: the total holonomy
    around a full loop is κ_τ = 1 − ι_τ, independent of depth n.
    Only the resolution (gap size) changes, not the total phase. -/
```

## Source Excerpt

```lean
theorem gap_refinement_invariant :
    canonical_grav_coupling.kappa_numer = iotaD - iota :=
  canonical_grav_coupling.is_one_minus_iota.1
```
