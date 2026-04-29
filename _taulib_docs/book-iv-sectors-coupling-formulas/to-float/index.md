---
{
  "projection_kind": "taulib_declaration",
  "title": "CouplingFormula.toFloat",
  "permalink": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/to-float/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.CouplingFormulas`.",
  "declaration_id": "TauLib.BookIV.Sectors.CouplingFormulas::CouplingFormula.toFloat",
  "declaration_slug": "to-float",
  "kind": "def",
  "name": "CouplingFormula.toFloat",
  "module_name": "TauLib.BookIV.Sectors.CouplingFormulas",
  "module_url": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/",
  "source_line_start": 75,
  "source_line_end": 89,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L75-L89",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.CouplingFormulas",
        "url": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L75-L89",
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

- Module: [TauLib.BookIV.Sectors.CouplingFormulas](/verify/taulib/docs/book-iv-sectors-coupling-formulas/)
- Source path: [`TauLib/BookIV/Sectors/CouplingFormulas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L75-L89)
- Source range: L75-L89
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Coupling formula as Float. -/
```

## Source Excerpt

```lean
def CouplingFormula.toFloat (c : CouplingFormula) : Float :=
  Float.ofNat c.numer / Float.ofNat c.denom

-- ============================================================
-- ABBREVIATIONS FOR READABILITY
-- ============================================================

-- ι = 341304, D = 1000000 (from SectorParameters)
-- (1 − ι/D) = (D − ι)/D = 658541/10⁶

/-- (D − ι) = 1000000 − 341304 = 658541. -/
private abbrev oneMinusIota : Nat := iotaD - iota   -- 658541

/-- (D + ι) = 1000000 + 341304 = 1341304. -/
private abbrev onePlusIota : Nat := iotaD + iota    -- 1341304
```
