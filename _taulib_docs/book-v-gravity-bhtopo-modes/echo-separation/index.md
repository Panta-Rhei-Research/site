---
{
  "projection_kind": "taulib_declaration",
  "title": "echo_separation",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-separation/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::echo_separation",
  "declaration_slug": "echo-separation",
  "kind": "def",
  "name": "echo_separation",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 132,
  "source_line_end": 133,
  "registry_ids": [
    "V.R373"
  ],
  "related_registry_items": [
    {
      "id": "V.R373",
      "title": "LIGO Echo Window: Δt = 4GM(1-ι_τ²)/(c³·ι_τ)",
      "url": "/registry/object/V.R373/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L132-L133",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L132-L133",
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L132-L133)
- Source range: L132-L133
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.R373` — LIGO Echo Window: Δt = 4GM(1-ι_τ²)/(c³·ι_τ)

## Immediate Comment / Docstring

```lean
/-- Echo separation: Δt = t_outer - t_inner = 4GM(ι_τ⁻¹ - ι_τ)/c³ [seconds].
    Lab values: M=30 M_☉ → 1.5303 ms; M=62 M_☉ → 3.1626 ms. [V.R373] -/
```

## Source Excerpt

```lean
def echo_separation (M_kg : Float) : Float :=
  echo_time_outer M_kg - echo_time_inner M_kg
```
