---
{
  "projection_kind": "taulib_declaration",
  "title": "t2_echo_time_formulas",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-time-formulas/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::t2_echo_time_formulas",
  "declaration_slug": "t2-echo-time-formulas",
  "kind": "def",
  "name": "t2_echo_time_formulas",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 305,
  "source_line_end": 307,
  "registry_ids": [
    "V.D243"
  ],
  "related_registry_items": [
    {
      "id": "V.D243",
      "title": "T² GW Echo Time Formulas with Frequency Bands",
      "url": "/registry/object/V.D243/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L305-L307",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L305-L307",
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
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L305-L307)
- Source range: L305-L307
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `V.D243` — T² GW Echo Time Formulas with Frequency Bands

## Immediate Comment / Docstring

```lean
/-- [V.D243] T² GW Echo Time Formulas.
    t₊=4GMι_τ/c³ (inner), t₋=4GMι_τ⁻¹/c³ (outer), t₋/t₊=ι_τ⁻²=8.585. -/
```

## Source Excerpt

```lean
def t2_echo_time_formulas : String :=
  "GW echoes: t₊=4GMι_τ/c³, t₋=4GMι_τ⁻¹/c³, ratio t₋/t₊=ι_τ⁻²=8.585. " ++
  "GW150914: t₊=0.417 ms, t₋=3.580 ms, both in LIGO band."
```
