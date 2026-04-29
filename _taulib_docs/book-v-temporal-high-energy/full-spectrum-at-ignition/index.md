---
{
  "projection_kind": "taulib_declaration",
  "title": "full_spectrum_at_ignition",
  "permalink": "/verify/taulib/docs/book-v-temporal-high-energy/full-spectrum-at-ignition/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Temporal.HighEnergy`.",
  "declaration_id": "TauLib.BookV.Temporal.HighEnergy::full_spectrum_at_ignition",
  "declaration_slug": "full-spectrum-at-ignition",
  "kind": "theorem",
  "name": "full_spectrum_at_ignition",
  "module_name": "TauLib.BookV.Temporal.HighEnergy",
  "module_url": "/verify/taulib/docs/book-v-temporal-high-energy/",
  "source_line_start": 74,
  "source_line_end": 79,
  "registry_ids": [
    "V.P05"
  ],
  "related_registry_items": [
    {
      "id": "V.P05",
      "title": "Mode Counting at Early Depths",
      "url": "/registry/object/V.P05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L74-L79",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Temporal.HighEnergy",
        "url": "/verify/taulib/docs/book-v-temporal-high-energy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L74-L79",
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

- Module: [TauLib.BookV.Temporal.HighEnergy](/verify/taulib/docs/book-v-temporal-high-energy/)
- Source path: [`TauLib/BookV/Temporal/HighEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Temporal/HighEnergy.lean#L74-L79)
- Source range: L74-L79
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P05` — Mode Counting at Early Depths

## Immediate Comment / Docstring

```lean
/-- [V.P05] At the ignition depth, all 5 sector spectral labels are
    present in the boundary holonomy algebra.

    This is verified by the holonomy generator list from Book IV,
    which covers all 5 sectors. At n_ign, the algebra first achieves
    full sector differentiation. -/
```

## Source Excerpt

```lean
theorem full_spectrum_at_ignition :
    -- All 5 generators are present
    holonomy_generators.length = 5 ∧
    -- All 5 sectors covered
    (holonomy_generators.map (·.sector)).length = 5 :=
  generator_adequacy
```
