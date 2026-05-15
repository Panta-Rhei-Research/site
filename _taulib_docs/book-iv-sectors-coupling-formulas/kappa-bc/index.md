---
{
  "projection_kind": "taulib_declaration",
  "title": "kappa_BC",
  "permalink": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/kappa-bc/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.CouplingFormulas`.",
  "declaration_id": "TauLib.BookIV.Sectors.CouplingFormulas::kappa_BC",
  "declaration_slug": "kappa-bc",
  "kind": "def",
  "name": "kappa_BC",
  "module_name": "TauLib.BookIV.Sectors.CouplingFormulas",
  "module_url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/",
  "source_line_start": 160,
  "source_line_end": 165,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L160-L165",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.CouplingFormulas",
        "url": "/corpus/taulib/docs/book-iv-sectors-coupling-formulas/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L160-L165",
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

- Module: [TauLib.BookIV.Sectors.CouplingFormulas](/corpus/taulib/docs/book-iv-sectors-coupling-formulas/)
- Source path: [`TauLib/BookIV/Sectors/CouplingFormulas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L160-L165)
- Source range: L160-L165
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- κ(B,C) = ι_τ³/(1+ι_τ): EM-Strong = Higgs/mass crossing. -/
```

## Source Excerpt

```lean
def kappa_BC : CouplingFormula where
  sector_i := .B
  sector_j := .C
  numer := iota * iota * iota * iotaD
  denom := iotaD * iotaD * iotaD * onePlusIota
  denom_pos := Nat.mul_pos (Nat.mul_pos (Nat.mul_pos iotaD_pos iotaD_pos) iotaD_pos) onePlusIota_pos
```
