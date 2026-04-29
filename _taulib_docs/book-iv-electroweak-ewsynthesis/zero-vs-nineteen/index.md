---
{
  "projection_kind": "taulib_declaration",
  "title": "ZeroVsNineteen",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/zero-vs-nineteen/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWSynthesis`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWSynthesis::ZeroVsNineteen",
  "declaration_slug": "zero-vs-nineteen",
  "kind": "structure",
  "name": "ZeroVsNineteen",
  "module_name": "TauLib.BookIV.Electroweak.EWSynthesis",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/",
  "source_line_start": 251,
  "source_line_end": 258,
  "registry_ids": [
    "IV.P79"
  ],
  "related_registry_items": [
    {
      "id": "IV.P79",
      "title": "Framework Comparison",
      "url": "/registry/object/IV.P79/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L251-L258",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWSynthesis",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewsynthesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L251-L258",
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

- Module: [TauLib.BookIV.Electroweak.EWSynthesis](/verify/taulib/docs/book-iv-electroweak-ewsynthesis/)
- Source path: [`TauLib/BookIV/Electroweak/EWSynthesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWSynthesis.lean#L251-L258)
- Source range: L251-L258
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P79` — Framework Comparison

## Immediate Comment / Docstring

```lean
/-- [IV.P79] The τ-framework determines all 9 EW quantities with
    zero free parameters, compared to the Standard Model's 19.

    SM free parameters include: 3 gauge couplings, 6 quark masses,
    3 lepton masses, 4 CKM parameters, 1 QCD vacuum angle, 1 Higgs
    mass, 1 Higgs VEV = 19 total.

    The τ-framework replaces all 19 with derivations from ι_τ. -/
```

## Source Excerpt

```lean
structure ZeroVsNineteen where
  /-- τ free parameters. -/
  tau_params : Nat := 0
  /-- SM free parameters. -/
  sm_params : Nat := 19
  /-- Reduction factor. -/
  reduction : String := "19 to 0 (complete)"
  deriving Repr
```
