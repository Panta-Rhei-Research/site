---
{
  "projection_kind": "taulib_declaration",
  "title": "ExactlyOneDerived",
  "permalink": "/verify/taulib/docs/book-iv-particles-sector-atlas/exactly-one-derived/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SectorAtlas`.",
  "declaration_id": "TauLib.BookIV.Particles.SectorAtlas::ExactlyOneDerived",
  "declaration_slug": "exactly-one-derived",
  "kind": "structure",
  "name": "ExactlyOneDerived",
  "module_name": "TauLib.BookIV.Particles.SectorAtlas",
  "module_url": "/verify/taulib/docs/book-iv-particles-sector-atlas/",
  "source_line_start": 86,
  "source_line_end": 97,
  "registry_ids": [
    "IV.T81"
  ],
  "related_registry_items": [
    {
      "id": "IV.T81",
      "title": "Exactly one derived sector",
      "url": "/registry/object/IV.T81/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L86-L97",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L86-L97",
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
- Source path: [`TauLib/BookIV/Particles/SectorAtlas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L86-L97)
- Source range: L86-L97
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T81` — Exactly one derived sector

## Immediate Comment / Docstring

```lean
/-- [IV.T81] The lemniscate L = S¹ ∨ S¹ has exactly one self-intersection
    point, so the sector decomposition admits exactly one derived sector:
    ω = B ∩ C = γ ∩ η (Higgs/mass mechanism).

    No other pair of primitive sectors produces a derived sector.
    This is topologically rigid: any homeomorphism of L preserves the
    unique wedge point, so the ω-sector cannot be removed. -/
```

## Source Excerpt

```lean
structure ExactlyOneDerived where
  /-- Number of derived sectors. -/
  count : Nat := 1
  /-- The derived sector. -/
  derived : Sector := .Omega
  /-- Parent sectors. -/
  parent_B : Sector := .B
  /-- Parent sectors. -/
  parent_C : Sector := .C
  /-- Topologically rigid. -/
  rigid : Bool := true
  deriving Repr
```
