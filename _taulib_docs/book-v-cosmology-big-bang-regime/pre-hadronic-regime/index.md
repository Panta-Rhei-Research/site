---
{
  "projection_kind": "taulib_declaration",
  "title": "PreHadronicRegime",
  "permalink": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/pre-hadronic-regime/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BigBangRegime`.",
  "declaration_id": "TauLib.BookV.Cosmology.BigBangRegime::PreHadronicRegime",
  "declaration_slug": "pre-hadronic-regime",
  "kind": "structure",
  "name": "PreHadronicRegime",
  "module_name": "TauLib.BookV.Cosmology.BigBangRegime",
  "module_url": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/",
  "source_line_start": 109,
  "source_line_end": 118,
  "registry_ids": [
    "V.D153"
  ],
  "related_registry_items": [
    {
      "id": "V.D153",
      "title": "Pre-Hadronic Regime",
      "url": "/registry/object/V.D153/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L109-L118",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BigBangRegime",
        "url": "/verify/taulib/docs/book-v-cosmology-big-bang-regime/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L109-L118",
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

- Module: [TauLib.BookV.Cosmology.BigBangRegime](/verify/taulib/docs/book-v-cosmology-big-bang-regime/)
- Source path: [`TauLib/BookV/Cosmology/BigBangRegime.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BigBangRegime.lean#L109-L118)
- Source range: L109-L118
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D153` — Pre-Hadronic Regime

## Immediate Comment / Docstring

```lean
/-- [V.D153] Pre-hadronic regime: the interval of α-ticks from the
    temporal opening α₁ to the neutron threshold L_N.

    During this regime:
    - All sector couplings are near-maximal
    - No stable hadrons exist yet
    - The τ-Einstein equation governs evolution -/
```

## Source Excerpt

```lean
structure PreHadronicRegime where
  /-- Starting tick (always 1). -/
  start_tick : Nat
  /-- Ending tick (neutron threshold). -/
  end_tick : Nat
  /-- Start is 1. -/
  start_is_one : start_tick = 1
  /-- End is after start. -/
  end_after_start : end_tick > start_tick
  deriving Repr
```
