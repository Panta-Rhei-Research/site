---
{
  "projection_kind": "taulib_declaration",
  "title": "WaddingtonLandscape",
  "permalink": "/verify/taulib/docs/book-vi-source-epigenetics/waddington-landscape/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Source.Epigenetics`.",
  "declaration_id": "TauLib.BookVI.Source.Epigenetics::WaddingtonLandscape",
  "declaration_slug": "waddington-landscape",
  "kind": "structure",
  "name": "WaddingtonLandscape",
  "module_name": "TauLib.BookVI.Source.Epigenetics",
  "module_url": "/verify/taulib/docs/book-vi-source-epigenetics/",
  "source_line_start": 193,
  "source_line_end": 202,
  "registry_ids": [
    "VI.D83"
  ],
  "related_registry_items": [
    {
      "id": "VI.D83",
      "title": "Waddington Landscape",
      "url": "/registry/object/VI.D83/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L193-L202",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Source.Epigenetics",
        "url": "/verify/taulib/docs/book-vi-source-epigenetics/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L193-L202",
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

- Module: [TauLib.BookVI.Source.Epigenetics](/verify/taulib/docs/book-vi-source-epigenetics/)
- Source path: [`TauLib/BookVI/Source/Epigenetics.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Source/Epigenetics.lean#L193-L202)
- Source range: L193-L202
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D83` — Waddington Landscape

## Immediate Comment / Docstring

```lean
/-- [VI.D83] Waddington Landscape.
    The refinement tower (VI.P18) indexed by epigenetic state (VI.D79),
    with the defect-functional Δ: State → ℝ≥0 providing the landscape surface.
    Valleys = local minima of Δ (stable cell types).
    Ridges = saddle points (barriers between fates).
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure WaddingtonLandscape where
  /-- Number of potency levels (depth of tower). -/
  potency_levels : Nat := 5
  /-- Active gene count descends along tower. -/
  descending_active_genes : Bool := true
  /-- Surface given by defect functional Δ. -/
  defect_functional_surface : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau-effective"
  deriving Repr
```
