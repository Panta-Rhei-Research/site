---
{
  "projection_kind": "taulib_declaration",
  "title": "remark_sector_separation",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/remark-sector-separation/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.TauHiggs`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs::remark_sector_separation",
  "declaration_slug": "remark-sector-separation",
  "kind": "def",
  "name": "remark_sector_separation",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/",
  "source_line_start": 303,
  "source_line_end": 304,
  "registry_ids": [
    "IV.R34"
  ],
  "related_registry_items": [
    {
      "id": "IV.R34",
      "title": "Coherence Fixing vs Mass Generation",
      "url": "/registry/object/IV.R34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L303-L304",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L303-L304",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs](/verify/taulib/docs/book-iv-electroweak-tau-higgs/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs.lean#L303-L304)
- Source range: L303-L304
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R34` — Coherence Fixing vs Mass Generation

## Immediate Comment / Docstring

```lean
/-- [IV.R34] The Higgs mechanism determines SECTOR SEPARATION
    (which sectors acquire mass via coupling to the VEV), NOT
    mass origin itself. Mass originates from the breathing operator
    on T² (Book IV Part III). The Higgs mechanism tells us which
    particles couple to the VEV and therefore which particles get
    mass from the EW sector.

    This distinction resolves the conceptual confusion in the SM
    where the Higgs "gives mass" — in τ, it mediates the assignment
    of mass to sectors, while mass itself is a fiber-geometric quantity. -/
```

## Source Excerpt

```lean
def remark_sector_separation : String :=
  "Higgs determines sector separation (mass assignment), not mass origin (breathing operator on T2)"
```
