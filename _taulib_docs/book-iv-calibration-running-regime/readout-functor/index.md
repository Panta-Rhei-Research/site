---
{
  "projection_kind": "taulib_declaration",
  "title": "ReadoutFunctor",
  "permalink": "/verify/taulib/docs/book-iv-calibration-running-regime/readout-functor/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Calibration.RunningRegime`.",
  "declaration_id": "TauLib.BookIV.Calibration.RunningRegime::ReadoutFunctor",
  "declaration_slug": "readout-functor",
  "kind": "structure",
  "name": "ReadoutFunctor",
  "module_name": "TauLib.BookIV.Calibration.RunningRegime",
  "module_url": "/verify/taulib/docs/book-iv-calibration-running-regime/",
  "source_line_start": 75,
  "source_line_end": 85,
  "registry_ids": [
    "IV.D301"
  ],
  "related_registry_items": [
    {
      "id": "IV.D301",
      "title": "Readout Functor",
      "url": "/registry/object/IV.D301/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L75-L85",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Calibration.RunningRegime",
        "url": "/verify/taulib/docs/book-iv-calibration-running-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L75-L85",
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

- Module: [TauLib.BookIV.Calibration.RunningRegime](/verify/taulib/docs/book-iv-calibration-running-regime/)
- Source path: [`TauLib/BookIV/Calibration/RunningRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Calibration/RunningRegime.lean#L75-L85)
- Source range: L75-L85
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D301` — Readout Functor

## Immediate Comment / Docstring

```lean
/-- [IV.D301] The readout functor R_μ: L_τ → L_obs(μ) sends each
    fixed ontic coupling κ(X;d) to its scale-dependent apparent value.
    R_μ is a homomorphism preserving ordering and complement structure. -/
```

## Source Excerpt

```lean
structure ReadoutFunctor where
  /-- Source: 10 ontic couplings. -/
  source_count : Nat
  source_eq : source_count = 10
  /-- Target: 10 apparent couplings at scale μ. -/
  target_count : Nat
  target_eq : target_count = 10
  /-- Order-preserving. -/
  order_preserving : Bool
  order_true : order_preserving = true
  deriving Repr
```
