---
{
  "projection_kind": "taulib_declaration",
  "title": "ParityTransformation",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/parity-transformation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.WeakChirality`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakChirality::ParityTransformation",
  "declaration_slug": "parity-transformation",
  "kind": "structure",
  "name": "ParityTransformation",
  "module_name": "TauLib.BookIV.Electroweak.WeakChirality",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/",
  "source_line_start": 189,
  "source_line_end": 196,
  "registry_ids": [
    "IV.D113"
  ],
  "related_registry_items": [
    {
      "id": "IV.D113",
      "title": "A-Sector Sigma-Admissibility",
      "url": "/registry/object/IV.D113/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L189-L196",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakChirality",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-chirality/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L189-L196",
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

- Module: [TauLib.BookIV.Electroweak.WeakChirality](/verify/taulib/docs/book-iv-electroweak-weak-chirality/)
- Source path: [`TauLib/BookIV/Electroweak/WeakChirality.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakChirality.lean#L189-L196)
- Source range: L189-L196
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D113` — A-Sector Sigma-Admissibility

## Immediate Comment / Docstring

```lean
/-- [IV.D113] Parity transformation P: spatial inversion x to -x.
    In the tau-framework, P is the sigma-involution restricted to spatial
    coordinates (fiber T-squared). It swaps chi_plus and chi_minus on the fiber. -/
```

## Source Excerpt

```lean
structure ParityTransformation where
  /-- Spatial dimension count affected. -/
  spatial_dims : Nat
  spatial_eq : spatial_dims = 3
  /-- Determinant of P: det(P) = (-1)^d = -1 for d = 3. -/
  det_sign : Int
  det_eq : det_sign = -1
  deriving Repr
```
