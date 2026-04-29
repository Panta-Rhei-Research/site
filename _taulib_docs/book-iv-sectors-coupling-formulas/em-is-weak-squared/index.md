---
{
  "projection_kind": "taulib_declaration",
  "title": "em_is_weak_squared",
  "permalink": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/em-is-weak-squared/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Sectors.CouplingFormulas`.",
  "declaration_id": "TauLib.BookIV.Sectors.CouplingFormulas::em_is_weak_squared",
  "declaration_slug": "em-is-weak-squared",
  "kind": "theorem",
  "name": "em_is_weak_squared",
  "module_name": "TauLib.BookIV.Sectors.CouplingFormulas",
  "module_url": "/verify/taulib/docs/book-iv-sectors-coupling-formulas/",
  "source_line_start": 228,
  "source_line_end": 231,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L228-L231",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L228-L231",
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
- Source path: [`TauLib/BookIV/Sectors/CouplingFormulas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/CouplingFormulas.lean#L228-L231)
- Source range: L228-L231
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [IV.P03a] κ(B;2) = κ(A;1)²: EM self-coupling equals Weak squared.
    Proof: ι²/D² = (ι/D)². -/
```

## Source Excerpt

```lean
theorem em_is_weak_squared :
    kappa_BB.numer * (kappa_AA.denom * kappa_AA.denom) =
    (kappa_AA.numer * kappa_AA.numer) * kappa_BB.denom := by
  simp [kappa_BB, kappa_AA, iota, iotaD, iota_tau_numer, iota_tau_denom]
```
