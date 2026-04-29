---
{
  "projection_kind": "taulib_declaration",
  "title": "echo_time_inner",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/echo-time-inner/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::echo_time_inner",
  "declaration_slug": "echo-time-inner",
  "kind": "def",
  "name": "echo_time_inner",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 127,
  "source_line_end": 128,
  "registry_ids": [
    "V.T169"
  ],
  "related_registry_items": [
    {
      "id": "V.T169",
      "title": "GW Echo Times t± = 4GM·ι_τ^{±1}/c³",
      "url": "/registry/object/V.T169/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L127-L128",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L127-L128",
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
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L127-L128)
- Source range: L127-L128
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.T169` — GW Echo Times t± = 4GM·ι_τ^{±1}/c³

## Immediate Comment / Docstring

```lean
/-- Inner echo time: t_inner = 4GM·ι_τ/c³ [seconds].
    Corresponds to inner S¹ round-trip on the torus horizon. [V.T169] -/
```

## Source Excerpt

```lean
def echo_time_inner (M_kg : Float) : Float :=
  4.0 * G_Newton * M_kg * iota_float / c_light ^ 3
```
