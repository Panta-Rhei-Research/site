---
{
  "projection_kind": "taulib_declaration",
  "title": "temporal_complement",
  "permalink": "/verify/taulib/docs/book-iv-arena-five-sectors/temporal-complement/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.FiveSectors`.",
  "declaration_id": "TauLib.BookIV.Arena.FiveSectors::temporal_complement",
  "declaration_slug": "temporal-complement",
  "kind": "theorem",
  "name": "temporal_complement",
  "module_name": "TauLib.BookIV.Arena.FiveSectors",
  "module_url": "/verify/taulib/docs/book-iv-arena-five-sectors/",
  "source_line_start": 88,
  "source_line_end": 90,
  "registry_ids": [
    "IV.R225",
    "IV.T99"
  ],
  "related_registry_items": [
    {
      "id": "IV.R225",
      "title": "Physical meaning",
      "url": "/registry/object/IV.R225/"
    },
    {
      "id": "IV.T99",
      "title": "Temporal Complement",
      "url": "/registry/object/IV.T99/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L88-L90",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.FiveSectors",
        "url": "/verify/taulib/docs/book-iv-arena-five-sectors/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L88-L90",
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

- Module: [TauLib.BookIV.Arena.FiveSectors](/verify/taulib/docs/book-iv-arena-five-sectors/)
- Source path: [`TauLib/BookIV/Arena/FiveSectors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L88-L90)
- Source range: L88-L90
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.R225` — Physical meaning
- `IV.T99` — Temporal Complement

## Immediate Comment / Docstring

```lean
/-- [IV.T99] Temporal complement: κ(A) + κ(D) = 1.
    Physical meaning [IV.R225]: temporal resources fully allocated.
    Wraps CouplingFormulas.temporal_complement. -/
```

## Source Excerpt

```lean
theorem temporal_complement :
    kappa_AA.numer + kappa_DD.numer = kappa_AA.denom :=
  Tau.BookIV.Sectors.temporal_complement
```
