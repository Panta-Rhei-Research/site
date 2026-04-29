---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_generator_set",
  "permalink": "/verify/taulib/docs/book-iv-particles-sector-atlas/canonical-generator-set/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.SectorAtlas`.",
  "declaration_id": "TauLib.BookIV.Particles.SectorAtlas::canonical_generator_set",
  "declaration_slug": "canonical-generator-set",
  "kind": "def",
  "name": "canonical_generator_set",
  "module_name": "TauLib.BookIV.Particles.SectorAtlas",
  "module_url": "/verify/taulib/docs/book-iv-particles-sector-atlas/",
  "source_line_start": 138,
  "source_line_end": 151,
  "registry_ids": [
    "IV.D194"
  ],
  "related_registry_items": [
    {
      "id": "IV.D194",
      "title": "9-element canonical generator set",
      "url": "/registry/object/IV.D194/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L138-L151",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L138-L151",
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

- Module: [TauLib.BookIV.Particles.SectorAtlas](/verify/taulib/docs/book-iv-particles-sector-atlas/)
- Source path: [`TauLib/BookIV/Particles/SectorAtlas.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/SectorAtlas.lean#L138-L151)
- Source range: L138-L151
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D194` — 9-element canonical generator set

## Immediate Comment / Docstring

```lean
/-- [IV.D194] The 9-element canonical generator set. -/
```

## Source Excerpt

```lean
def canonical_generator_set : List CanonicalGenerator := [
  -- 4 vacuum idempotents
  ⟨"Vac_D", .vacuumIdempotent, some .D⟩,
  ⟨"Vac_A", .vacuumIdempotent, some .A⟩,
  ⟨"Vac_B", .vacuumIdempotent, some .B⟩,
  ⟨"Vac_C", .vacuumIdempotent, some .C⟩,
  -- 4 gap quanta
  ⟨"Gap_D", .gapQuantum, some .D⟩,
  ⟨"Gap_A", .gapQuantum, some .A⟩,
  ⟨"Gap_B", .gapQuantum, some .B⟩,
  ⟨"Gap_C", .gapQuantum, some .C⟩,
  -- 1 crossing generator
  ⟨"iota_tau", .crossingGenerator, some .Omega⟩
]
```
