---
{
  "projection_kind": "taulib_declaration",
  "title": "si_boltzmann",
  "permalink": "/corpus/taulib/docs/book-iv-calibration-sireference/si-boltzmann/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.SIReference`.",
  "declaration_id": "TauLib.BookIV.Calibration.SIReference::si_boltzmann",
  "declaration_slug": "si-boltzmann",
  "kind": "def",
  "name": "si_boltzmann",
  "module_name": "TauLib.BookIV.Calibration.SIReference",
  "module_url": "/corpus/taulib/docs/book-iv-calibration-sireference/",
  "source_line_start": 105,
  "source_line_end": 110,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L105-L110",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L105-L110",
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
- Source path: [`TauLib/BookIV/Calibration/SIReference.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L105-L110)
- Source range: L105-L110
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Boltzmann constant: k_B = 1.380 649 × 10⁻²³ J/K (EXACT).
    Tier II physical constant: entropy–energy bridge.
    Stored as 1380649 / 10²⁹ (numer = k_B × 10²⁹). -/
```

## Source Excerpt

```lean
def si_boltzmann : SIConstant where
  name := "Boltzmann constant k_B"
  numer := 1380649
  denom := 100000000000000000000000000000  -- 10²⁹
  denom_pos := by omega
  is_exact := true
```
