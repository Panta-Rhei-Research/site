---
{
  "projection_kind": "taulib_declaration",
  "title": "temporal_complement",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/temporal-complement/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.FrameHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.FrameHolonomy::temporal_complement",
  "declaration_slug": "temporal-complement",
  "kind": "theorem",
  "name": "temporal_complement",
  "module_name": "TauLib.BookV.GravityField.FrameHolonomy",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-frame-holonomy/",
  "source_line_start": 261,
  "source_line_end": 263,
  "registry_ids": [
    "V.C01"
  ],
  "related_registry_items": [
    {
      "id": "V.C01",
      "title": "Temporal Complement, revisited",
      "url": "/registry/object/V.C01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L261-L263",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L261-L263",
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
- Source path: [`TauLib/BookV/GravityField/FrameHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/FrameHolonomy.lean#L261-L263)
- Source range: L261-L263
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.C01` — Temporal Complement, revisited

## Immediate Comment / Docstring

```lean
/-- [V.C01] Temporal complement: κ_τ + κ_A = 1.

    The gravity coupling (D-sector, 1 − ι_τ) and the weak coupling
    (A-sector, ι_τ) sum to 1, partitioning the base circle τ¹.

    Cross-multiplied: (iotaD − iota) + iota = iotaD. -/
```

## Source Excerpt

```lean
theorem temporal_complement :
    (iotaD - iota) + iota = iotaD := by
  simp [iotaD, iota, iota_tau_denom, iota_tau_numer]
```
