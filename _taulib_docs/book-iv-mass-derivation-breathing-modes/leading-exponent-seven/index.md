---
{
  "projection_kind": "taulib_declaration",
  "title": "leading_exponent_seven",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/leading-exponent-seven/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.MassDerivation.BreathingModes`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.BreathingModes::leading_exponent_seven",
  "declaration_slug": "leading-exponent-seven",
  "kind": "theorem",
  "name": "leading_exponent_seven",
  "module_name": "TauLib.BookIV.MassDerivation.BreathingModes",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/",
  "source_line_start": 128,
  "source_line_end": 130,
  "registry_ids": [
    "IV.T114"
  ],
  "related_registry_items": [
    {
      "id": "IV.T114",
      "title": "Leading exponent -7",
      "url": "/registry/object/IV.T114/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L128-L130",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L128-L130",
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
- Source path: [`TauLib/BookIV/MassDerivation/BreathingModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L128-L130)
- Source range: L128-L130
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T114` — Leading exponent -7

## Immediate Comment / Docstring

```lean
/-- [IV.T114] Leading term ∝ ι_τ^{-7} (exponent = 1−2×4 = −7). -/
```

## Source Excerpt

```lean
theorem leading_exponent_seven :
    chowla_selberg_s4.leading_exp = -7 :=
  leading_exponent_is_neg7
```
