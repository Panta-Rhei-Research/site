---
{
  "projection_kind": "taulib_declaration",
  "title": "z_mixing",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/z-mixing/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy2::z_mixing",
  "declaration_slug": "z-mixing",
  "kind": "theorem",
  "name": "z_mixing",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/",
  "source_line_start": 164,
  "source_line_end": 170,
  "registry_ids": [
    "IV.P60"
  ],
  "related_registry_items": [
    {
      "id": "IV.P60",
      "title": "Z Field Composition",
      "url": "/registry/object/IV.P60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L164-L170",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L164-L170",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy2](/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L164-L170)
- Source range: L164-L170
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P60` — Z Field Composition

## Immediate Comment / Docstring

```lean
/-- [IV.P60] The Z boson is a mixture of W3 and B (hypercharge):
    Z = cos(theta_W) * W3 - sin(theta_W) * B.
    The photon is the orthogonal combination:
    A = sin(theta_W) * W3 + cos(theta_W) * B.
    Structural: two input fields (W3, B) produce two output fields (Z, gamma). -/
```

## Source Excerpt

```lean
theorem z_mixing :
    -- Two input gauge fields mix to two output fields
    (1 + 1 : Nat) = 2 ∧
    -- The mixing is parameterized by one angle
    weinberg_angle.sin2_numer > 0 ∧
    weinberg_angle.sin2_numer < weinberg_angle.sin2_denom := by
  simp [weinberg_angle]
```
