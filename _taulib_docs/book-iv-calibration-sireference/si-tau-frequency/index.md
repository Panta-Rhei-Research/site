---
{
  "projection_kind": "taulib_declaration",
  "title": "si_tau_frequency",
  "permalink": "/verify/taulib/docs/book-iv-calibration-sireference/si-tau-frequency/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.SIReference`.",
  "declaration_id": "TauLib.BookIV.Calibration.SIReference::si_tau_frequency",
  "declaration_slug": "si-tau-frequency",
  "kind": "def",
  "name": "si_tau_frequency",
  "module_name": "TauLib.BookIV.Calibration.SIReference",
  "module_url": "/verify/taulib/docs/book-iv-calibration-sireference/",
  "source_line_start": 248,
  "source_line_end": 253,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L248-L253",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.SIReference",
        "url": "/verify/taulib/docs/book-iv-calibration-sireference/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L248-L253",
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

- Module: [TauLib.BookIV.Calibration.SIReference](/verify/taulib/docs/book-iv-calibration-sireference/)
- Source path: [`TauLib/BookIV/Calibration/SIReference.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L248-L253)
- Source range: L248-L253
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- τ frequency scale: H = R·f_e ≈ 2.2714 × 10²³ Hz.
    Neutron de Broglie frequency.
    In the τ-framework: determined once R and c, h are fixed.
    Stored as 22714 / 10⁻¹⁹ → actually: 22714 × 10¹⁹.
    Better encoding: H_numer = 22714, H_scale = 10¹⁹ (multiply to get Hz). -/
```

## Source Excerpt

```lean
def si_tau_frequency : SIConstant where
  name := "τ frequency scale H"
  numer := 22714           -- × 10¹⁹ Hz
  denom := 10              -- so numer/denom = 2271.4, multiply by 10²⁰ for Hz
  denom_pos := by omega    -- We use a convention: value_Hz = numer/denom × 10²⁰
  is_exact := false
```
