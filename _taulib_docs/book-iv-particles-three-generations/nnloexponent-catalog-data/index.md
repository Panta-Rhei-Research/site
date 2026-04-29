---
{
  "projection_kind": "taulib_declaration",
  "title": "NNLOExponentCatalogData",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/nnloexponent-catalog-data/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::NNLOExponentCatalogData",
  "declaration_slug": "nnloexponent-catalog-data",
  "kind": "structure",
  "name": "NNLOExponentCatalogData",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2131,
  "source_line_end": 2138,
  "registry_ids": [
    "IV.D367"
  ],
  "related_registry_items": [
    {
      "id": "IV.D367",
      "title": "NNLO Exponent Catalog: 7 Window-Universal Corrections",
      "url": "/registry/object/IV.D367/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2131-L2138",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2131-L2138",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2131-L2138)
- Source range: L2131-L2138
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D367` — NNLO Exponent Catalog: 7 Window-Universal Corrections

## Immediate Comment / Docstring

```lean
/-- [IV.D367] NNLO exponent catalog structure (formalized). -/
```

## Source Excerpt

```lean
structure NNLOExponentCatalogData where
  /-- Number of catalog entries. -/
  n_entries : Nat := 7
  /-- Number of entries using Window universality. -/
  n_window_universal : Nat := 7
  /-- W₃(4) value appearing in all entries. -/
  w3_4_value : Nat := 5
  deriving Repr
```
