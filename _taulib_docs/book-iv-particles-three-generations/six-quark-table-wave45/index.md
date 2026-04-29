---
{
  "projection_kind": "taulib_declaration",
  "title": "SixQuarkTableWave45",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/six-quark-table-wave45/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::SixQuarkTableWave45",
  "declaration_slug": "six-quark-table-wave45",
  "kind": "structure",
  "name": "SixQuarkTableWave45",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2964,
  "source_line_end": 2971,
  "registry_ids": [
    "IV.D382"
  ],
  "related_registry_items": [
    {
      "id": "IV.D382",
      "title": "Updated Six-Quark Table (Wave 45)",
      "url": "/registry/object/IV.D382/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2964-L2971",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2964-L2971",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2964-L2971)
- Source range: L2964-L2971
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D382` — Updated Six-Quark Table (Wave 45)

## Immediate Comment / Docstring

```lean
/-- [IV.D382] Updated six-quark table (Wave 45). -/
```

## Source Excerpt

```lean
structure SixQuarkTableWave45 where
  /-- All six quarks sub-1600 ppm. -/
  all_sub_1600 : Bool := true
  /-- Exponents derived (of 7). -/
  exponents_derived : Nat := 7
  /-- Free parameters. -/
  free_params : Nat := 0
  deriving Repr
```
