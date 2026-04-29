---
{
  "projection_kind": "taulib_declaration",
  "title": "coupling_formula",
  "permalink": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/coupling-formula-l269/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.CouplingFormulas`.",
  "declaration_id": "TauLib.BookIV.Sectors.CouplingFormulas::coupling_formula",
  "declaration_slug": "coupling-formula-l269",
  "kind": "def",
  "name": "coupling_formula",
  "module_name": "TauLib.BookIV.Sectors.CouplingFormulas",
  "module_url": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/",
  "source_line_start": 269,
  "source_line_end": 287,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L269-L287",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L269-L287",
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
- Source path: [`TauLib/BookIV/Sectors/CouplingFormulas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L269-L287)
- Source range: L269-L287
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Retrieve the coupling formula for a sector pair.
    Symmetric: coupling(i,j) = coupling(j,i). -/
```

## Source Excerpt

```lean
def coupling_formula (si sj : Sector) : CouplingFormula :=
  let (a, b) := if si.toNat ≤ sj.toNat then (si, sj) else (sj, si)
  match a, b with
  | .D, .D => kappa_DD
  | .D, .A => kappa_AD
  | .D, .B => kappa_BD
  | .D, .C => kappa_CD
  | .D, .Omega => kappa_DD   -- D-ω coupling defaults to D self-coupling
  | .A, .A => kappa_AA
  | .A, .B => kappa_AB
  | .A, .C => kappa_AC
  | .A, .Omega => kappa_AA   -- A-ω defaults to A self-coupling
  | .B, .B => kappa_BB
  | .B, .C => kappa_BC
  | .B, .Omega => kappa_BC   -- B-ω = B-C (ω = B∩C)
  | .C, .C => kappa_CC
  | .C, .Omega => kappa_BC   -- C-ω = B-C
  | .Omega, .Omega => kappa_BC  -- ω self-coupling = B-C crossing
  | _, _ => kappa_DD            -- unreachable: ordering guarantees a ≤ b
```
