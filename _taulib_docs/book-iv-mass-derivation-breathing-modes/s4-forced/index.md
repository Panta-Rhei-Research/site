---
{
  "projection_kind": "taulib_declaration",
  "title": "s4_forced",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/s4-forced/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.MassDerivation.BreathingModes`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.BreathingModes::s4_forced",
  "declaration_slug": "s4-forced",
  "kind": "theorem",
  "name": "s4_forced",
  "module_name": "TauLib.BookIV.MassDerivation.BreathingModes",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/",
  "source_line_start": 133,
  "source_line_end": 135,
  "registry_ids": [
    "IV.R338"
  ],
  "related_registry_items": [
    {
      "id": "IV.R338",
      "title": "Structural origin of the exponent 7",
      "url": "/registry/object/IV.R338/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L133-L135",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L133-L135",
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
- Source path: [`TauLib/BookIV/MassDerivation/BreathingModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L133-L135)
- Source range: L133-L135
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.R338` — Structural origin of the exponent 7

## Immediate Comment / Docstring

```lean
/-- [IV.R338] s=4 forced by mass operator: 1−2s = −7 → s = 4. -/
```

## Source Excerpt

```lean
theorem s4_forced :
    ∀ (s : Nat), (1 : Int) - 2 * (s : Int) = -7 → s = 4 :=
  s4_unique_from_neg7
```
