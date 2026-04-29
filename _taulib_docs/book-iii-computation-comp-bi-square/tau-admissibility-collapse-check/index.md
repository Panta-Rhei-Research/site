---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_admissibility_collapse_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-comp-bi-square/tau-admissibility-collapse-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.CompBiSquare`.",
  "declaration_id": "TauLib.BookIII.Computation.CompBiSquare::tau_admissibility_collapse_check",
  "declaration_slug": "tau-admissibility-collapse-check",
  "kind": "def",
  "name": "tau_admissibility_collapse_check",
  "module_name": "TauLib.BookIII.Computation.CompBiSquare",
  "module_url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/",
  "source_line_start": 128,
  "source_line_end": 132,
  "registry_ids": [
    "III.T33"
  ],
  "related_registry_items": [
    {
      "id": "III.T33",
      "title": "τ-Admissibility Collapse",
      "url": "/registry/object/III.T33/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L128-L132",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.CompBiSquare",
        "url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L128-L132",
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

- Module: [TauLib.BookIII.Computation.CompBiSquare](/verify/taulib/docs/book-iii-computation-comp-bi-square/)
- Source path: [`TauLib/BookIII/Computation/CompBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L128-L132)
- Source range: L128-L132
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T33` — τ-Admissibility Collapse

## Immediate Comment / Docstring

```lean
/-- [III.T33] τ-Admissibility Collapse: τ-P_adm = τ-NP_adm.
    Three-step verification:
    (1) Cook-Levin: polynomial bounded tableau
    (2) CRT: witness decomposes into per-prime searches
    (3) Product-Meet: search = construction -/
```

## Source Excerpt

```lean
def tau_admissibility_collapse_check (bound db : TauIdx) : Bool :=
  let cook_levin := tau_admissible_check bound db
  let crt := crt_witness_check bound db
  let collapse := product_meet_collapse_check bound db
  cook_levin && crt && collapse
```
