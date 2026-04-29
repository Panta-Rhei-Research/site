---
{
  "projection_kind": "taulib_declaration",
  "title": "g_from_iota_squared",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/g-from-iota-squared/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::g_from_iota_squared",
  "declaration_slug": "g-from-iota-squared",
  "kind": "theorem",
  "name": "g_from_iota_squared",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 301,
  "source_line_end": 306,
  "registry_ids": [
    "V.T22"
  ],
  "related_registry_items": [
    {
      "id": "V.T22",
      "title": "G derivation --- V.D02",
      "url": "/registry/object/V.T22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L301-L306",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L301-L306",
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
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L301-L306)
- Source range: L301-L306
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T22` — G derivation --- V.D02

## Immediate Comment / Docstring

```lean
/-- [V.T22] G_τ = (c³/ℏ) · ι_τ²: the gravitational constant is
    proportional to ι_τ² with the Planck-unit prefactor.
    Verified: iota * iota > 0 (positive coupling). -/
```

## Source Excerpt

```lean
theorem g_from_iota_squared :
    g_tau_from_shape.iota_sq_num > 0 ∧
    g_tau_from_shape.iota_sq_den > 0 := by
  constructor
  · simp [g_tau_from_shape, iota, iota_tau_numer]
  · exact g_tau_from_shape.denom_pos
```
