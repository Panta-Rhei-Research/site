---
{
  "projection_kind": "taulib_declaration",
  "title": "NoBSM",
  "permalink": "/verify/taulib/docs/book-iv-particles-sector-atlas/no-bsm/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SectorAtlas`.",
  "declaration_id": "TauLib.BookIV.Particles.SectorAtlas::NoBSM",
  "declaration_slug": "no-bsm",
  "kind": "structure",
  "name": "NoBSM",
  "module_name": "TauLib.BookIV.Particles.SectorAtlas",
  "module_url": "/verify/taulib/docs/book-iv-particles-sector-atlas/",
  "source_line_start": 272,
  "source_line_end": 283,
  "registry_ids": [
    "IV.R110"
  ],
  "related_registry_items": [
    {
      "id": "IV.R110",
      "title": "No BSM particles",
      "url": "/registry/object/IV.R110/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L272-L283",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.SectorAtlas",
        "url": "/verify/taulib/docs/book-iv-particles-sector-atlas/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L272-L283",
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

- Module: [TauLib.BookIV.Particles.SectorAtlas](/verify/taulib/docs/book-iv-particles-sector-atlas/)
- Source path: [`TauLib/BookIV/Particles/SectorAtlas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L272-L283)
- Source range: L272-L283
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R110` — No BSM particles

## Immediate Comment / Docstring

```lean
/-- [IV.R110] The periodic table of τ-particles contains no BSM particles:
    no supersymmetric partners, no leptoquarks, no right-handed neutrinos,
    no fourth generation, no dark matter candidates with new quantum numbers.
    This is a structural consequence of the Exactly-Four Theorem and
    lemniscate topology. -/
```

## Source Excerpt

```lean
structure NoBSM where
  /-- No supersymmetry. -/
  no_susy : Bool := true
  /-- No leptoquarks. -/
  no_leptoquarks : Bool := true
  /-- No right-handed neutrinos. -/
  no_rh_neutrinos : Bool := true
  /-- No fourth generation. -/
  no_fourth_gen : Bool := true
  /-- No new dark matter candidates. -/
  no_new_dm : Bool := true
  deriving Repr
```
