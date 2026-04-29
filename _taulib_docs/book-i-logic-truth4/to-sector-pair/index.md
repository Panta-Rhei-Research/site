---
{
  "projection_kind": "taulib_declaration",
  "title": "Truth4.toSectorPair",
  "permalink": "/verify/taulib/docs/book-i-logic-truth4/to-sector-pair/",
  "summary_short": "`def` declaration in `TauLib.BookI.Logic.Truth4`.",
  "declaration_id": "TauLib.BookI.Logic.Truth4::Truth4.toSectorPair",
  "declaration_slug": "to-sector-pair",
  "kind": "def",
  "name": "Truth4.toSectorPair",
  "module_name": "TauLib.BookI.Logic.Truth4",
  "module_url": "/verify/taulib/docs/book-i-logic-truth4/",
  "source_line_start": 269,
  "source_line_end": 273,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L269-L273",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Logic.Truth4",
        "url": "/verify/taulib/docs/book-i-logic-truth4/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L269-L273",
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

- Module: [TauLib.BookI.Logic.Truth4](/verify/taulib/docs/book-i-logic-truth4/)
- Source path: [`TauLib/BookI/Logic/Truth4.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Logic/Truth4.lean#L269-L273)
- Source range: L269-L273
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Map Truth4 to sector pairs: T = (1,1), F = (0,0), B = (1,0), N = (0,1).
    Links Truth4 to the split-complex idempotent structure from BipolarAlgebra. -/
```

## Source Excerpt

```lean
def Truth4.toSectorPair : Truth4 -> Tau.Polarity.SectorPair
  | T => { b_sector := 1, c_sector := 1 }
  | F => { b_sector := 0, c_sector := 0 }
  | B => Tau.Polarity.e_plus_sector
  | N => Tau.Polarity.e_minus_sector
```
