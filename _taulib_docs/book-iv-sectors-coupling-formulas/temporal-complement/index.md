---
{
  "projection_kind": "taulib_declaration",
  "title": "temporal_complement",
  "permalink": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/temporal-complement/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.CouplingFormulas`.",
  "declaration_id": "TauLib.BookIV.Sectors.CouplingFormulas::temporal_complement",
  "declaration_slug": "temporal-complement",
  "kind": "theorem",
  "name": "temporal_complement",
  "module_name": "TauLib.BookIV.Sectors.CouplingFormulas",
  "module_url": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/",
  "source_line_start": 197,
  "source_line_end": 200,
  "registry_ids": [
    "IV.T01"
  ],
  "related_registry_items": [
    {
      "id": "IV.T01",
      "title": "Temporal Complement",
      "url": "/registry/object/IV.T01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L197-L200",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L197-L200",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookIV/Sectors/CouplingFormulas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L197-L200)
- Source range: L197-L200
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T01` — Temporal Complement

## Immediate Comment / Docstring

```lean
/-- [IV.T01] κ(A;1) + κ(D;1) = 1: the temporal pair exhausts the
    depth-1 coupling budget. Gravity and Weak are complements.

    Proof: ι + (D − ι) = D, so ι/D + (D−ι)/D = 1. -/
```

## Source Excerpt

```lean
theorem temporal_complement :
    kappa_AA.numer + kappa_DD.numer = kappa_AA.denom := by
  simp [kappa_AA, kappa_DD, iota, oneMinusIota, iotaD,
        iota_tau_numer, iota_tau_denom]
```
