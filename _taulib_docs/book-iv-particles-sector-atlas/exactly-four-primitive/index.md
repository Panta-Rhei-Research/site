---
{
  "projection_kind": "taulib_declaration",
  "title": "ExactlyFourPrimitive",
  "permalink": "/verify/taulib/docs/book-iv-particles-sector-atlas/exactly-four-primitive/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.SectorAtlas`.",
  "declaration_id": "TauLib.BookIV.Particles.SectorAtlas::ExactlyFourPrimitive",
  "declaration_slug": "exactly-four-primitive",
  "kind": "structure",
  "name": "ExactlyFourPrimitive",
  "module_name": "TauLib.BookIV.Particles.SectorAtlas",
  "module_url": "/verify/taulib/docs/book-iv-particles-sector-atlas/",
  "source_line_start": 56,
  "source_line_end": 65,
  "registry_ids": [
    "IV.T80"
  ],
  "related_registry_items": [
    {
      "id": "IV.T80",
      "title": "Exactly four primitive forces (physical reading)",
      "url": "/registry/object/IV.T80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L56-L65",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L56-L65",
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
- Source path: [`TauLib/BookIV/Particles/SectorAtlas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L56-L65)
- Source range: L56-L65
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T80` — Exactly four primitive forces (physical reading)

## Immediate Comment / Docstring

```lean
/-- [IV.T80] The boundary holonomy algebra admits exactly four linearly
    independent primitive sector characters, instantiating at E₁ as:
    1. D = Gravity (α-generator)
    2. A = Weak (π-generator)
    3. B = EM (γ-generator)
    4. C = Strong (η-generator)

    No fifth primitive sector exists and no GUT unification reduces
    this count. The four-ness is a topological invariant of L = S¹ ∨ S¹. -/
```

## Source Excerpt

```lean
structure ExactlyFourPrimitive where
  /-- Number of primitive sectors. -/
  count : Nat := 4
  /-- Sectors are: D, A, B, C. -/
  sectors : List Sector := [.D, .A, .B, .C]
  /-- Each is linearly independent. -/
  independent : Bool := true
  /-- No fifth sector. -/
  no_fifth : Bool := true
  deriving Repr
```
