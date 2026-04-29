---
{
  "projection_kind": "taulib_declaration",
  "title": "tension_monotone",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/tension-monotone/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TOVPhaseBoundary`.",
  "declaration_id": "TauLib.BookV.GravityField.TOVPhaseBoundary::tension_monotone",
  "declaration_slug": "tension-monotone",
  "kind": "theorem",
  "name": "tension_monotone",
  "module_name": "TauLib.BookV.GravityField.TOVPhaseBoundary",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/",
  "source_line_start": 198,
  "source_line_end": 200,
  "registry_ids": [
    "V.T45"
  ],
  "related_registry_items": [
    {
      "id": "V.T45",
      "title": "Tension Monotonicity",
      "url": "/registry/object/V.T45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L198-L200",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L198-L200",
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

- Module: [TauLib.BookV.GravityField.TOVPhaseBoundary](/verify/taulib/docs/book-v-gravity-field-tovphase-boundary/)
- Source path: [`TauLib/BookV/GravityField/TOVPhaseBoundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TOVPhaseBoundary.lean#L198-L200)
- Source range: L198-L200
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T45` — Tension Monotonicity

## Immediate Comment / Docstring

```lean
/-- [V.T45] Tension monotonicity: on the S^2 branch, the tension
    increases monotonically with mass above the Chandrasekhar threshold.

    Structural recording: for M1 < M2, T_S2(M1) < T_S2(M2). -/
```

## Source Excerpt

```lean
theorem tension_monotone :
    "T_S2(M1) < T_S2(M2) when M1 < M2 above M_Ch" =
    "T_S2(M1) < T_S2(M2) when M1 < M2 above M_Ch" := rfl
```
