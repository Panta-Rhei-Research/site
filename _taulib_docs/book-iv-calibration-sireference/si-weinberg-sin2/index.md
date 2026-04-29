---
{
  "projection_kind": "taulib_declaration",
  "title": "si_weinberg_sin2",
  "permalink": "/verify/taulib/docs/book-iv-calibration-sireference/si-weinberg-sin2/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Calibration.SIReference`.",
  "declaration_id": "TauLib.BookIV.Calibration.SIReference::si_weinberg_sin2",
  "declaration_slug": "si-weinberg-sin2",
  "kind": "def",
  "name": "si_weinberg_sin2",
  "module_name": "TauLib.BookIV.Calibration.SIReference",
  "module_url": "/verify/taulib/docs/book-iv-calibration-sireference/",
  "source_line_start": 174,
  "source_line_end": 179,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L174-L179",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L174-L179",
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
- Source path: [`TauLib/BookIV/Calibration/SIReference.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/SIReference.lean#L174-L179)
- Source range: L174-L179
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Weinberg angle: sin²θ_W = 0.23121(4) (on-shell, CODATA 2022).
    τ-candidate: κ(A,D) = ι_τ(1−ι_τ) ≈ 0.2249.
    Stored as 23121 / 100000. -/
```

## Source Excerpt

```lean
def si_weinberg_sin2 : SIConstant where
  name := "Weinberg angle sin²θ_W"
  numer := 23121
  denom := 100000
  denom_pos := by omega
  is_exact := false
```
