---
{
  "projection_kind": "taulib_declaration",
  "title": "echo_time_inner",
  "permalink": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/echo-time-inner/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::echo_time_inner",
  "declaration_slug": "echo-time-inner",
  "kind": "def",
  "name": "echo_time_inner",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 131,
  "source_line_end": 132,
  "registry_ids": [
    "V.T169"
  ],
  "related_registry_items": [
    {
      "id": "V.T169",
      "title": "GW Cycle-Delay Times t± = 4GM·ι_τ^{±1}/c³",
      "url": "/registry/object/V.T169/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L131-L132",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L131-L132",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L131-L132)
- Source range: L131-L132
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `V.T169` — GW Cycle-Delay Times t± = 4GM·ι_τ^{±1}/c³

## Immediate Comment / Docstring

```lean
/-- Inner cycle-delay time: t_inner = 4GM·ι_τ/c³ [seconds].
    Corresponds to inner S¹ round-trip on the torus horizon. This is a
    topology-readout delay, not an exotic-compact-object reflective-surface
    echo. The declaration name is kept for public API stability. [V.T169] -/
```

## Source Excerpt

```lean
def echo_time_inner (M_kg : Float) : Float :=
  4.0 * G_Newton * M_kg * iota_float / c_light ^ 3
```
