---
{
  "projection_kind": "taulib_declaration",
  "title": "ObservableLevel",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/observable-level/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance2::ObservableLevel",
  "declaration_slug": "observable-level",
  "kind": "inductive",
  "name": "ObservableLevel",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/",
  "source_line_start": 223,
  "source_line_end": 227,
  "registry_ids": [
    "IV.P40"
  ],
  "related_registry_items": [
    {
      "id": "IV.P40",
      "title": "Observable Hierarchy",
      "url": "/registry/object/IV.P40/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L223-L227",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.GaugeInvariance2",
        "url": "/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L223-L227",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookIV.Electroweak.GaugeInvariance2](/verify/taulib/docs/book-iv-electroweak-gauge-invariance2/)
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L223-L227)
- Source range: L223-L227
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.P40` — Observable Hierarchy

## Immediate Comment / Docstring

```lean
/-- [IV.P40] EM observable hierarchy: A_μ (gauge-dependent) →
    F_μν (gauge-invariant, local) → Hol(γ) (gauge-invariant, global).
    Each level is more physical; Hol(γ) is the ultimate observable. -/
```

## Source Excerpt

```lean
inductive ObservableLevel where
  | Potential   : ObservableLevel  -- A_μ, gauge-dependent
  | FieldStrength : ObservableLevel  -- F_μν, local invariant
  | Holonomy    : ObservableLevel  -- Hol(γ), global invariant
  deriving Repr, DecidableEq, BEq
```
