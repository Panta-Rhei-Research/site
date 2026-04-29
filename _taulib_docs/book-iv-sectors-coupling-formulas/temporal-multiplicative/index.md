---
{
  "projection_kind": "taulib_declaration",
  "title": "temporal_multiplicative",
  "permalink": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/temporal-multiplicative/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.CouplingFormulas`.",
  "declaration_id": "TauLib.BookIV.Sectors.CouplingFormulas::temporal_multiplicative",
  "declaration_slug": "temporal-multiplicative",
  "kind": "theorem",
  "name": "temporal_multiplicative",
  "module_name": "TauLib.BookIV.Sectors.CouplingFormulas",
  "module_url": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/",
  "source_line_start": 216,
  "source_line_end": 220,
  "registry_ids": [
    "IV.T02"
  ],
  "related_registry_items": [
    {
      "id": "IV.T02",
      "title": "Temporal Multiplicative Closure",
      "url": "/registry/object/IV.T02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L216-L220",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L216-L220",
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
- Source path: [`TauLib/BookIV/Sectors/CouplingFormulas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L216-L220)
- Source range: L216-L220
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T02` — Temporal Multiplicative Closure

## Immediate Comment / Docstring

```lean
/-- [IV.T02] κ(A,D) = κ(A;1) · κ(D;1): the temporal cross-coupling
    is exactly the product of the two temporal self-couplings.
    This means the temporal pair is "multiplicatively closed."

    Proof: ι(D−ι)/D² = (ι/D)·((D−ι)/D). -/
```

## Source Excerpt

```lean
theorem temporal_multiplicative :
    kappa_AD.numer * (kappa_AA.denom * kappa_DD.denom) =
    kappa_AA.numer * kappa_DD.numer * kappa_AD.denom := by
  simp [kappa_AD, kappa_AA, kappa_DD, iota, oneMinusIota, iotaD,
        iota_tau_numer, iota_tau_denom]
```
