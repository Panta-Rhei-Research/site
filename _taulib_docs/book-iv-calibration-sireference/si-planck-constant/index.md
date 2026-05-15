---
{
  "projection_kind": "taulib_declaration",
  "title": "si_planck_constant",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-sireference/si-planck-constant/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.SIReference`.",
  "declaration_id": "TauLib.BookIV.Calibration.SIReference::si_planck_constant",
  "declaration_slug": "si-planck-constant",
  "kind": "def",
  "name": "si_planck_constant",
  "module_name": "TauLib.BookIV.Calibration.SIReference",
  "module_url": "/corpus/taulib/docs/book-iv-calibration-sireference/",
  "source_line_start": 85,
  "source_line_end": 90,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L85-L90",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.SIReference",
        "url": "/corpus/taulib/docs/book-iv-calibration-sireference/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L85-L90",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookIV.Calibration.SIReference](/corpus/taulib/docs/book-iv-calibration-sireference/)
- Source path: [`TauLib/BookIV/Calibration/SIReference.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L85-L90)
- Source range: L85-L90
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Planck constant: h = 6.626 070 15 × 10⁻³⁴ J·s (EXACT).
    Tier I structural constant: minimal action quantum.
    Stored as 662607015 / 10⁴² (numer = h × 10⁴²). -/
```

## Source Excerpt

```lean
def si_planck_constant : SIConstant where
  name := "Planck constant h"
  numer := 662607015
  denom := 1000000000000000000000000000000000000000000  -- 10⁴²
  denom_pos := by omega
  is_exact := true
```
