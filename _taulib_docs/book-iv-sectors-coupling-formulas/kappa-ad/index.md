---
{
  "projection_kind": "taulib_declaration",
  "title": "kappa_AD",
  "permalink": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/kappa-ad/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.CouplingFormulas`.",
  "declaration_id": "TauLib.BookIV.Sectors.CouplingFormulas::kappa_AD",
  "declaration_slug": "kappa-ad",
  "kind": "def",
  "name": "kappa_AD",
  "module_name": "TauLib.BookIV.Sectors.CouplingFormulas",
  "module_url": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/",
  "source_line_start": 152,
  "source_line_end": 157,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L152-L157",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L152-L157",
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
- Source path: [`TauLib/BookIV/Sectors/CouplingFormulas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L152-L157)
- Source range: L152-L157
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- κ(A,D) = ι_τ(1−ι_τ): Weak-Gravity coupling (temporal consistency). -/
```

## Source Excerpt

```lean
def kappa_AD : CouplingFormula where
  sector_i := .A
  sector_j := .D
  numer := iota * oneMinusIota           -- ι × (D − ι)
  denom := iotaD * iotaD                 -- D²
  denom_pos := Nat.mul_pos iotaD_pos iotaD_pos
```
