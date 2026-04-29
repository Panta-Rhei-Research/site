---
{
  "projection_kind": "taulib_declaration",
  "title": "MixingCompatibility",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/mixing-compatibility/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::MixingCompatibility",
  "declaration_slug": "mixing-compatibility",
  "kind": "structure",
  "name": "MixingCompatibility",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 182,
  "source_line_end": 190,
  "registry_ids": [
    "IV.D131"
  ],
  "related_registry_items": [
    {
      "id": "IV.D131",
      "title": "Mixing Compatibility",
      "url": "/registry/object/IV.D131/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L182-L190",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWMixing",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L182-L190",
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

- Module: [TauLib.BookIV.Electroweak.EWMixing](/verify/taulib/docs/book-iv-electroweak-ewmixing/)
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L182-L190)
- Source range: L182-L190
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D131` — Mixing Compatibility

## Immediate Comment / Docstring

```lean
/-- [IV.D131] A sector pair is mixing-compatible if:
    1. One sector has balanced polarity (= sector A, unique).
    2. The other has χ₊-dominant polarity on the fiber (= sector B).
    3. Their cross-coupling κ(A,B) is nonzero.

    These conditions ensure that the neutral component of the balanced
    sector can rotate into the χ₊-dominant sector. -/
```

## Source Excerpt

```lean
structure MixingCompatibility where
  /-- First sector (must be balanced). -/
  balanced : Sector
  /-- Second sector (must be χ₊-dominant, fiber). -/
  chi_plus_fiber : Sector
  /-- Balanced is A. -/
  balanced_is_A : balanced = .A
  /-- χ₊-fiber is B. -/
  chi_plus_is_B : chi_plus_fiber = .B
```
