---
{
  "projection_kind": "taulib_declaration",
  "title": "pred_electron_mass",
  "permalink": "/verify/taulib/docs/book-v-cosmology-falsification-pack/pred-electron-mass/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.FalsificationPack`.",
  "declaration_id": "TauLib.BookV.Cosmology.FalsificationPack::pred_electron_mass",
  "declaration_slug": "pred-electron-mass",
  "kind": "def",
  "name": "pred_electron_mass",
  "module_name": "TauLib.BookV.Cosmology.FalsificationPack",
  "module_url": "/verify/taulib/docs/book-v-cosmology-falsification-pack/",
  "source_line_start": 142,
  "source_line_end": 147,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L142-L147",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.FalsificationPack",
        "url": "/verify/taulib/docs/book-v-cosmology-falsification-pack/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L142-L147",
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

- Module: [TauLib.BookV.Cosmology.FalsificationPack](/verify/taulib/docs/book-v-cosmology-falsification-pack/)
- Source path: [`TauLib/BookV/Cosmology/FalsificationPack.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L142-L147)
- Source range: L142-L147
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Q1: Electron mass at 0.025 ppm. -/
```

## Source Excerpt

```lean
def pred_electron_mass : TestablePrediction where
  name := "Q1: m_e = 0.510999 MeV (0.025 ppm)"
  level := .Quantitative
  description := "From R = iota^(-7) - (sqrt3 + pi^3*alpha^2)*iota^(-2)"
  status := "Matches CODATA to 0.025 ppm"
  currently_testable := true
```
