---
{
  "projection_kind": "taulib_declaration",
  "title": "UVFiniteness",
  "permalink": "/verify/taulib/docs/book-iv-coda-laws-as-structure/uvfiniteness/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.LawsAsStructure`.",
  "declaration_id": "TauLib.BookIV.Coda.LawsAsStructure::UVFiniteness",
  "declaration_slug": "uvfiniteness",
  "kind": "structure",
  "name": "UVFiniteness",
  "module_name": "TauLib.BookIV.Coda.LawsAsStructure",
  "module_url": "/verify/taulib/docs/book-iv-coda-laws-as-structure/",
  "source_line_start": 197,
  "source_line_end": 210,
  "registry_ids": [
    "IV.P145"
  ],
  "related_registry_items": [
    {
      "id": "IV.P145",
      "title": "UV finiteness",
      "url": "/registry/object/IV.P145/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L197-L210",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.LawsAsStructure",
        "url": "/verify/taulib/docs/book-iv-coda-laws-as-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L197-L210",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Coda.LawsAsStructure](/verify/taulib/docs/book-iv-coda-laws-as-structure/)
- Source path: [`TauLib/BookIV/Coda/LawsAsStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/LawsAsStructure.lean#L197-L210)
- Source range: L197-L210
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P145` — UV finiteness

## Immediate Comment / Docstring

```lean
/-- [IV.P145] Every morphism in tau^3 is UV-finite: loop integrals are
    sums over intermediate addresses at tower level n with at most
    prod_{p <= p_n} p terms, each well-defined and finite.

    No continuum regularization (dimensional regularization, Pauli-Villars,
    zeta-function regularization) is needed or meaningful.

    UV divergences in orthodox QFT arise from summing over a continuum;
    in tau the sum is always over a finite set at each tower level. -/
```

## Source Excerpt

```lean
structure UVFiniteness where
  /-- Finite sum at each tower level. -/
  finite_at_each_level : Bool := true
  /-- Bound: at most prod_{p <= p_n} p terms. -/
  bound : String := "prod_{p <= p_n} p"
  /-- No dimensional regularization needed. -/
  no_dim_reg : Bool := true
  /-- No Pauli-Villars needed. -/
  no_pauli_villars : Bool := true
  /-- No zeta-function regularization needed. -/
  no_zeta_reg : Bool := true
  /-- Source of orthodoxy UV divergence: continuum sum. -/
  orthodoxy_source : String := "summing over continuum (uncountable modes)"
  deriving Repr
```
