---
{
  "projection_kind": "taulib_declaration",
  "title": "MasterConstant",
  "permalink": "/verify/taulib/docs/book-iv-arena-tau3-arena/master-constant/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Arena.Tau3Arena`.",
  "declaration_id": "TauLib.BookIV.Arena.Tau3Arena::MasterConstant",
  "declaration_slug": "master-constant",
  "kind": "structure",
  "name": "MasterConstant",
  "module_name": "TauLib.BookIV.Arena.Tau3Arena",
  "module_url": "/verify/taulib/docs/book-iv-arena-tau3-arena/",
  "source_line_start": 126,
  "source_line_end": 135,
  "registry_ids": [
    "IV.D255"
  ],
  "related_registry_items": [
    {
      "id": "IV.D255",
      "title": "Master constant iota_tau",
      "url": "/registry/object/IV.D255/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L126-L135",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.Tau3Arena",
        "url": "/verify/taulib/docs/book-iv-arena-tau3-arena/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L126-L135",
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

- Module: [TauLib.BookIV.Arena.Tau3Arena](/verify/taulib/docs/book-iv-arena-tau3-arena/)
- Source path: [`TauLib/BookIV/Arena/Tau3Arena.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/Tau3Arena.lean#L126-L135)
- Source range: L126-L135
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D255` — Master constant iota_tau

## Immediate Comment / Docstring

```lean
/-- [IV.D255] The master constant ι_τ = 2/(π+e) ≈ 0.341304.
    Represented as the Nat pair (341304, 1000000) from TauLib.Boundary.Iota.
    All couplings, masses, and constants derive from this single number. -/
```

## Source Excerpt

```lean
structure MasterConstant where
  /-- Numerator at scale 10⁶. -/
  numer : Nat
  /-- Denominator at scale 10⁶. -/
  denom : Nat
  /-- The specific values. -/
  numer_eq : numer = iota_tau_numer
  denom_eq : denom = iota_tau_denom
  /-- Denominator positive. -/
  denom_pos : denom > 0
```
