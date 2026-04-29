---
{
  "projection_kind": "taulib_declaration",
  "title": "OmegaResolution",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/omega-resolution/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::OmegaResolution",
  "declaration_slug": "omega-resolution",
  "kind": "structure",
  "name": "OmegaResolution",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 227,
  "source_line_end": 237,
  "registry_ids": [
    "IV.D133"
  ],
  "related_registry_items": [
    {
      "id": "IV.D133",
      "title": "Coherence Fixing (Ch33)",
      "url": "/registry/object/IV.D133/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L227-L237",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L227-L237",
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
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L227-L237)
- Source range: L227-L237
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D133` — Coherence Fixing (Ch33)

## Immediate Comment / Docstring

```lean
/-- [IV.D133] The ω-sector resolves the singularity at the lemniscate
    crossing point where sectors B and C meet. Without ω, the
    mixing rotation would encounter a topological obstruction at
    the crossing. The Higgs mechanism (ω-sector) smooths this
    singularity, enabling clean boson mass generation. -/
```

## Source Excerpt

```lean
structure OmegaResolution where
  /-- The crossing sector. -/
  crossing : Sector
  /-- Resolved sectors. -/
  resolved_1 : Sector
  resolved_2 : Sector
  /-- Crossing is ω. -/
  crossing_is_omega : crossing = .Omega
  /-- Resolved pair is (B, C). -/
  resolved_is_BC : resolved_1 = .B ∧ resolved_2 = .C
  deriving Repr
```
