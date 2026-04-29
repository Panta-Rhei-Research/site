---
{
  "projection_kind": "taulib_declaration",
  "title": "PolaritySign",
  "permalink": "/verify/taulib/docs/book-iv-sectors-sector-parameters/polarity-sign/",
  "summary_short": "`inductive` declaration in `TauLib.BookIV.Sectors.SectorParameters`.",
  "declaration_id": "TauLib.BookIV.Sectors.SectorParameters::PolaritySign",
  "declaration_slug": "polarity-sign",
  "kind": "inductive",
  "name": "PolaritySign",
  "module_name": "TauLib.BookIV.Sectors.SectorParameters",
  "module_url": "/verify/taulib/docs/book-iv-sectors-sector-parameters/",
  "source_line_start": 57,
  "source_line_end": 66,
  "registry_ids": [
    "IV.D01"
  ],
  "related_registry_items": [
    {
      "id": "IV.D01",
      "title": "Sector Physics Template",
      "url": "/registry/object/IV.D01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L57-L66",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.SectorParameters",
        "url": "/verify/taulib/docs/book-iv-sectors-sector-parameters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L57-L66",
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

- Module: [TauLib.BookIV.Sectors.SectorParameters](/verify/taulib/docs/book-iv-sectors-sector-parameters/)
- Source path: [`TauLib/BookIV/Sectors/SectorParameters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L57-L66)
- Source range: L57-L66
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `IV.D01` — Sector Physics Template

## Immediate Comment / Docstring

```lean
/-- [IV.D01] Spectral polarity signature of a sector.
    Determines which boundary characters dominate the sector's physics. -/
```

## Source Excerpt

```lean
inductive PolaritySign where
  /-- χ₊-dominant: multiplicative/spreading characters dominate. -/
  | ChiPlus
  /-- Balanced: equal χ₊ and χ₋ content (pol = 1). -/
  | Balanced
  /-- χ₋-dominant: additive/tightening characters dominate. -/
  | ChiMinus
  /-- Crossing: both lobes active simultaneously (ω-sector only). -/
  | Crossing
  deriving Repr, DecidableEq, BEq
```
