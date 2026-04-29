---
{
  "projection_kind": "taulib_declaration",
  "title": "RegimeReadoutMap",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-coupling/regime-readout-map/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongCoupling`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongCoupling::RegimeReadoutMap",
  "declaration_slug": "regime-readout-map",
  "kind": "structure",
  "name": "RegimeReadoutMap",
  "module_name": "TauLib.BookIV.Strong.StrongCoupling",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-coupling/",
  "source_line_start": 251,
  "source_line_end": 258,
  "registry_ids": [
    "IV.D186"
  ],
  "related_registry_items": [
    {
      "id": "IV.D186",
      "title": "Regime readout map",
      "url": "/registry/object/IV.D186/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L251-L258",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongCoupling",
        "url": "/verify/taulib/docs/book-iv-strong-strong-coupling/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L251-L258",
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

- Module: [TauLib.BookIV.Strong.StrongCoupling](/verify/taulib/docs/book-iv-strong-strong-coupling/)
- Source path: [`TauLib/BookIV/Strong/StrongCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L251-L258)
- Source range: L251-L258
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D186` — Regime readout map

## Immediate Comment / Docstring

```lean
/-- [IV.D186] Read_S[R]: H_partial -> R_R, extracting the measured
    value of an ontic coupling in a specific regime. -/
```

## Source Excerpt

```lean
structure RegimeReadoutMap where
  /-- Source: boundary algebra. -/
  source : String := "H_partial"
  /-- Target: real numbers in regime metric. -/
  target : String := "R_R (reals in regime metric)"
  /-- Depends on regime selector. -/
  regime_dependent : Bool := true
  deriving Repr
```
