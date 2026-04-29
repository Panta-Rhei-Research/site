---
{
  "projection_kind": "taulib_declaration",
  "title": "BHABPhase",
  "permalink": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/bhabphase/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.MergerNormalForm`.",
  "declaration_id": "TauLib.BookV.Cosmology.MergerNormalForm::BHABPhase",
  "declaration_slug": "bhabphase",
  "kind": "structure",
  "name": "BHABPhase",
  "module_name": "TauLib.BookV.Cosmology.MergerNormalForm",
  "module_url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/",
  "source_line_start": 245,
  "source_line_end": 252,
  "registry_ids": [
    "V.P100"
  ],
  "related_registry_items": [
    {
      "id": "V.P100",
      "title": "BH gravitational Aharonov--Bohm phase",
      "url": "/registry/object/V.P100/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L245-L252",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L245-L252",
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
- Source path: [`TauLib/BookV/Cosmology/MergerNormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L245-L252)
- Source range: L245-L252
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P100` — BH gravitational Aharonov--Bohm phase

## Immediate Comment / Docstring

```lean
/-- [V.P100] BH gravitational Aharonov-Bohm phase:
    Φ_BH = G·M / ι_τ = (c³/ℏ) · ι_τ · M.

    The phase is proportional to M and inversely proportional to ι_τ.
    It is detectable (in principle) via gravitational interference. -/
```

## Source Excerpt

```lean
structure BHABPhase where
  /-- Mass index (scaled). -/
  mass_index : Nat
  /-- Mass positive. -/
  mass_pos : mass_index > 0
  /-- Phase is proportional to M. -/
  proportional_to_mass : Bool := true
  deriving Repr
```
