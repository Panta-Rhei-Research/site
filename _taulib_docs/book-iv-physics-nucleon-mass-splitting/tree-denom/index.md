---
{
  "projection_kind": "taulib_declaration",
  "title": "tree_denom",
  "permalink": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/tree-denom/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.NucleonMassSplitting`.",
  "declaration_id": "TauLib.BookIV.Physics.NucleonMassSplitting::tree_denom",
  "declaration_slug": "tree-denom",
  "kind": "def",
  "name": "tree_denom",
  "module_name": "TauLib.BookIV.Physics.NucleonMassSplitting",
  "module_url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/",
  "source_line_start": 221,
  "source_line_end": 221,
  "registry_ids": [
    "IV.T141"
  ],
  "related_registry_items": [
    {
      "id": "IV.T141",
      "title": "Proton-Neutron Mass Difference — Tree Level [SUPERSEDED]",
      "url": "/registry/object/IV.T141/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L221-L221",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.NucleonMassSplitting",
        "url": "/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L221-L221",
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

- Module: [TauLib.BookIV.Physics.NucleonMassSplitting](/verify/taulib/docs/book-iv-physics-nucleon-mass-splitting/)
- Source path: [`TauLib/BookIV/Physics/NucleonMassSplitting.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/NucleonMassSplitting.lean#L221-L221)
- Source range: L221-L221
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.T141` — Proton-Neutron Mass Difference — Tree Level [SUPERSEDED]

## Immediate Comment / Docstring

```lean
/-- [IV.T141] Tree-level denominator: 2 · √3_denom · ι_τ⁶_denom. -/
```

## Source Excerpt

```lean
def tree_denom : Nat := 2 * sqrt3_denom * iota6_denom
```
