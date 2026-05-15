---
{
  "projection_kind": "taulib_declaration",
  "title": "t2_echo_time_formulas",
  "permalink": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/t2-echo-time-formulas/",
  "summary_short": "`def` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::t2_echo_time_formulas",
  "declaration_slug": "t2-echo-time-formulas",
  "kind": "def",
  "name": "t2_echo_time_formulas",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 309,
  "source_line_end": 312,
  "registry_ids": [
    "V.D243"
  ],
  "related_registry_items": [
    {
      "id": "V.D243",
      "title": "T² GW Cycle-Delay Time Formulas with Frequency Bands",
      "url": "/registry/object/V.D243/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L309-L312",
  "formal_status": "defined",
  "declaration_role": "docstring/data record",
  "formal_status_label": "docstring/data record",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L309-L312",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "docstring/data record",
      "status": "docstring/data record"
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
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L309-L312)
- Source range: L309-L312
- Kind: `def`
- Public role: `docstring/data record`
- Formal status hint: `docstring/data record`

## Registry Links

- `V.D243` — T² GW Cycle-Delay Time Formulas with Frequency Bands

## Immediate Comment / Docstring

```lean
/-- [V.D243] T² GW Cycle-Delay Time Formulas.
    t₊=4GMι_τ/c³ (inner), t₋=4GMι_τ⁻¹/c³ (outer), t₋/t₊=ι_τ⁻²=8.585. -/
```

## Source Excerpt

```lean
def t2_echo_time_formulas : String :=
  "T² cycle-delay readouts: t₊=4GMι_τ/c³, t₋=4GMι_τ⁻¹/c³, " ++
  "ratio t₋/t₊=ι_τ⁻²=8.585. These are not reflective-surface ECO echoes. " ++
  "GW150914: t₊=0.417 ms, t₋=3.580 ms, both in LIGO band."
```
