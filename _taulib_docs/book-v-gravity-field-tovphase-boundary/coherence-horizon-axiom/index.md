---
{
  "projection_kind": "taulib_declaration",
  "title": "CoherenceHorizonAxiom",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/coherence-horizon-axiom/",
  "summary_short": "`structure` declaration in `TauLib.BookV.GravityField.TOVPhaseBoundary`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVPhaseBoundary::CoherenceHorizonAxiom",
  "declaration_slug": "coherence-horizon-axiom",
  "kind": "structure",
  "name": "CoherenceHorizonAxiom",
  "module_name": "TauLib.BookV.GravityField.TOVPhaseBoundary",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/",
  "source_line_start": 149,
  "source_line_end": 156,
  "registry_ids": [
    "V.C04"
  ],
  "related_registry_items": [
    {
      "id": "V.C04",
      "title": "TOV Limit",
      "url": "/registry/object/V.C04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L149-L156",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TOVPhaseBoundary",
        "url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L149-L156",
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

- Module: [TauLib.BookV.GravityField.TOVPhaseBoundary](/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/)
- Source path: [`TauLib/BookV/GravityField/TOVPhaseBoundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L149-L156)
- Source range: L149-L156
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.C04` — TOV Limit

## Immediate Comment / Docstring

```lean
/-- [V.C04] Coherence horizon is well-defined, finite, and positive.

    This is conjectural because the full proof requires solving
    the tension functional minimization on both topology branches
    simultaneously, which depends on the neutron star equation
    of state at nuclear densities. -/
```

## Source Excerpt

```lean
structure CoherenceHorizonAxiom where
  /-- The horizon exists. -/
  horizon : CoherenceHorizon
  /-- It is finite (bounded from above). -/
  is_finite : Bool := true
  /-- Scope: conjectural. -/
  scope : String := "conjectural"
  deriving Repr
```
