---
{
  "projection_kind": "taulib_declaration",
  "title": "RingdownMode",
  "permalink": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/ringdown-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.MergerNormalForm`.",
  "declaration_id": "TauLib.BookV.Cosmology.MergerNormalForm::RingdownMode",
  "declaration_slug": "ringdown-mode",
  "kind": "structure",
  "name": "RingdownMode",
  "module_name": "TauLib.BookV.Cosmology.MergerNormalForm",
  "module_url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/",
  "source_line_start": 108,
  "source_line_end": 121,
  "registry_ids": [
    "V.D175"
  ],
  "related_registry_items": [
    {
      "id": "V.D175",
      "title": "Ringdown mode",
      "url": "/registry/object/V.D175/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L108-L121",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.MergerNormalForm",
        "url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L108-L121",
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

- Module: [TauLib.BookV.Cosmology.MergerNormalForm](/verify/taulib/docs/book-v-cosmology-merger-normal-form/)
- Source path: [`TauLib/BookV/Cosmology/MergerNormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L108-L121)
- Source range: L108-L121
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D175` — Ringdown mode

## Immediate Comment / Docstring

```lean
/-- [V.D175] Ringdown mode: the n-th quasi-normal mode of a merged
    excision, characterized by amplitude, damping rate, and frequency.

    r_n(t) = A_n · exp(−σ_n·t) · cos(ω_n·t + φ_n)

    Damping rate σ_n > 0 for all n ≥ 1. -/
```

## Source Excerpt

```lean
structure RingdownMode where
  /-- Mode number (≥ 1). -/
  mode_number : Nat
  /-- Mode number positive. -/
  mode_pos : mode_number > 0
  /-- Amplitude (scaled). -/
  amplitude : Nat
  /-- Damping rate (scaled, strictly positive). -/
  damping_rate : Nat
  /-- Damping positive. -/
  damping_pos : damping_rate > 0
  /-- Frequency (scaled). -/
  frequency : Nat
  deriving Repr
```
