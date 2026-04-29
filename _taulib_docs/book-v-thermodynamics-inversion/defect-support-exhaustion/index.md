---
{
  "projection_kind": "taulib_declaration",
  "title": "defect_support_exhaustion",
  "permalink": "/verify/taulib/docs/book-v-thermodynamics-inversion/defect-support-exhaustion/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Thermodynamics.Inversion`.",
  "declaration_id": "TauLib.BookV.Thermodynamics.Inversion::defect_support_exhaustion",
  "declaration_slug": "defect-support-exhaustion",
  "kind": "theorem",
  "name": "defect_support_exhaustion",
  "module_name": "TauLib.BookV.Thermodynamics.Inversion",
  "module_url": "/verify/taulib/docs/book-v-thermodynamics-inversion/",
  "source_line_start": 216,
  "source_line_end": 217,
  "registry_ids": [
    "V.C05"
  ],
  "related_registry_items": [
    {
      "id": "V.C05",
      "title": "Defect support exhaustion",
      "url": "/registry/object/V.C05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L216-L217",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Thermodynamics.Inversion",
        "url": "/verify/taulib/docs/book-v-thermodynamics-inversion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L216-L217",
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

- Module: [TauLib.BookV.Thermodynamics.Inversion](/verify/taulib/docs/book-v-thermodynamics-inversion/)
- Source path: [`TauLib/BookV/Thermodynamics/Inversion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Thermodynamics/Inversion.lean#L216-L217)
- Source range: L216-L217
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.C05` — Defect support exhaustion

## Immediate Comment / Docstring

```lean
/-- [V.C05] Defect support exhaustion: starting from any initial
    configuration, defect support contracts geometrically and the
    total defect support summed over all depths is finite.

    The exhaustion is guaranteed by the geometric contraction
    with factor (1 - iota_tau) < 1. -/
```

## Source Excerpt

```lean
theorem defect_support_exhaustion :
    contraction_numer < contraction_denom := contraction_lt_one
```
