---
{
  "projection_kind": "taulib_declaration",
  "title": "fast_reconnection_is_iota_sq",
  "permalink": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/fast-reconnection-is-iota-sq/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.FluidMacro.TauMHD`.",
  "declaration_id": "TauLib.BookV.FluidMacro.TauMHD::fast_reconnection_is_iota_sq",
  "declaration_slug": "fast-reconnection-is-iota-sq",
  "kind": "theorem",
  "name": "fast_reconnection_is_iota_sq",
  "module_name": "TauLib.BookV.FluidMacro.TauMHD",
  "module_url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/",
  "source_line_start": 310,
  "source_line_end": 311,
  "registry_ids": [
    "V.T252"
  ],
  "related_registry_items": [
    {
      "id": "V.T252",
      "title": "v_rec = ι_τ² v_A",
      "url": "/registry/object/V.T252/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L310-L311",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.FluidMacro.TauMHD",
        "url": "/verify/taulib/docs/book-v-fluid-macro-tau-mhd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L310-L311",
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

- Module: [TauLib.BookV.FluidMacro.TauMHD](/verify/taulib/docs/book-v-fluid-macro-tau-mhd/)
- Source path: [`TauLib/BookV/FluidMacro/TauMHD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/FluidMacro/TauMHD.lean#L310-L311)
- Source range: L310-L311
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T252` — v_rec = ι_τ² v_A

## Immediate Comment / Docstring

```lean
/-- [V.T252] The fast reconnection rate is ι_τ² v_A.

    In τ-MHD, reconnection is a B-sector topological transition.
    The rate v_rec = κ(B;2) · v_A = ι_τ² · v_A with zero free
    parameters. Matches observed ~0.1 v_A to within 0.6σ. -/
```

## Source Excerpt

```lean
theorem fast_reconnection_is_iota_sq :
    fast_reconnection_rate_tau.free_params = 0 := by native_decide
```
