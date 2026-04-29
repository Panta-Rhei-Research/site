---
{
  "projection_kind": "taulib_declaration",
  "title": "toroidal_dominance",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/toroidal-dominance/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.MassDerivation.BreathingModes`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.BreathingModes::toroidal_dominance",
  "declaration_slug": "toroidal-dominance",
  "kind": "theorem",
  "name": "toroidal_dominance",
  "module_name": "TauLib.BookIV.MassDerivation.BreathingModes",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/",
  "source_line_start": 120,
  "source_line_end": 122,
  "registry_ids": [
    "IV.R337"
  ],
  "related_registry_items": [
    {
      "id": "IV.R337",
      "title": "Toroidal dominance",
      "url": "/registry/object/IV.R337/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L120-L122",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.MassDerivation.BreathingModes",
        "url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L120-L122",
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

- Module: [TauLib.BookIV.MassDerivation.BreathingModes](/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/)
- Source path: [`TauLib/BookIV/MassDerivation/BreathingModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L120-L122)
- Source range: L120-L122
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.R337` — Toroidal dominance

## Immediate Comment / Docstring

```lean
/-- [IV.R337] n-axis modes contribute 99.95% of Z(4). -/
```

## Source Excerpt

```lean
theorem toroidal_dominance :
    n_axis_dominant.dominance_lower_bound > 9900 :=
  n_axis_dominant.dominates
```
