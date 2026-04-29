---
{
  "projection_kind": "taulib_declaration",
  "title": "comp_bisquare_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-comp-bi-square/comp-bisquare-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.CompBiSquare`.",
  "declaration_id": "TauLib.BookIII.Computation.CompBiSquare::comp_bisquare_check",
  "declaration_slug": "comp-bisquare-check",
  "kind": "def",
  "name": "comp_bisquare_check",
  "module_name": "TauLib.BookIII.Computation.CompBiSquare",
  "module_url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/",
  "source_line_start": 113,
  "source_line_end": 117,
  "registry_ids": [
    "III.D56"
  ],
  "related_registry_items": [
    {
      "id": "III.D56",
      "title": "Computational Bi-Square",
      "url": "/registry/object/III.D56/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L113-L117",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.CompBiSquare",
        "url": "/verify/taulib/docs/book-iii-computation-comp-bi-square/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L113-L117",
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

- Module: [TauLib.BookIII.Computation.CompBiSquare](/verify/taulib/docs/book-iii-computation-comp-bi-square/)
- Source path: [`TauLib/BookIII/Computation/CompBiSquare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/CompBiSquare.lean#L113-L117)
- Source range: L113-L117
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D56` — Computational Bi-Square

## Immediate Comment / Docstring

```lean
/-- [III.D56] Computational bi-square check: left face = TTM tower coherence,
    right face = witness spectral naturality, paste = product-meet collapse. -/
```

## Source Excerpt

```lean
def comp_bisquare_check (bound db : TauIdx) : Bool :=
  let left := ttm_tower_coherence_go 0 1 bound db ((bound + 1) * (db + 1))
  let right := witness_spectral_go 0 1 bound db ((bound + 1) * (db + 1))
  let paste := product_meet_collapse_check bound db
  left && right && paste
```
