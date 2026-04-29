---
{
  "projection_kind": "taulib_declaration",
  "title": "lepton_number_not_conserved",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/lepton-number-not-conserved/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.MajoranaStructure`.",
  "declaration_id": "TauLib.BookIV.Electroweak.MajoranaStructure::lepton_number_not_conserved",
  "declaration_slug": "lepton-number-not-conserved",
  "kind": "def",
  "name": "lepton_number_not_conserved",
  "module_name": "TauLib.BookIV.Electroweak.MajoranaStructure",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/",
  "source_line_start": 183,
  "source_line_end": 187,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L183-L187",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.MajoranaStructure",
        "url": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L183-L187",
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

- Module: [TauLib.BookIV.Electroweak.MajoranaStructure](/verify/taulib/docs/book-iv-electroweak-majorana-structure/)
- Source path: [`TauLib/BookIV/Electroweak/MajoranaStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L183-L187)
- Source range: L183-L187
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Lepton number is not a gauge charge in Category τ.
    It is not associated with any of the 5 generators or 5 sectors.
    The A-sector (weak) does not carry a U(1)_L gauge symmetry. -/
```

## Source Excerpt

```lean
def lepton_number_not_conserved : String :=
  "L is not a sector holonomy in Category tau. " ++
  "The 5 generators (alpha, pi, gamma, eta, omega) produce 5 sector holonomies; " ++
  "none of them is lepton number. L is an approximate kinematic label at low energy. " ++
  "Neutrino masses (Majorana) explicitly break L by 2 units per interaction."
```
