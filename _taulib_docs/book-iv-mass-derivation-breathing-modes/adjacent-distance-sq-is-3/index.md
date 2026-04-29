---
{
  "projection_kind": "taulib_declaration",
  "title": "adjacent_distance_sq_is_3",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/adjacent-distance-sq-is-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.MassDerivation.BreathingModes`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.BreathingModes::adjacent_distance_sq_is_3",
  "declaration_slug": "adjacent-distance-sq-is-3",
  "kind": "theorem",
  "name": "adjacent_distance_sq_is_3",
  "module_name": "TauLib.BookIV.MassDerivation.BreathingModes",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-breathing-modes/",
  "source_line_start": 161,
  "source_line_end": 163,
  "registry_ids": [
    "IV.T115"
  ],
  "related_registry_items": [
    {
      "id": "IV.T115",
      "title": "Three-fold distance squared",
      "url": "/registry/object/IV.T115/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L161-L163",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L161-L163",
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
- Source path: [`TauLib/BookIV/MassDerivation/BreathingModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/BreathingModes.lean#L161-L163)
- Source range: L161-L163
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T115` — Three-fold distance squared

## Immediate Comment / Docstring

```lean
/-- [IV.T115] d²=3 from |1 − e^{2πi/3}|² = (3/2)² + (√3/2)² = 3. -/
```

## Source Excerpt

```lean
theorem adjacent_distance_sq_is_3 :
    omega_real_sq + omega_imag_sq = 3 * omega_denom :=
  threefold_distance_sq
```
