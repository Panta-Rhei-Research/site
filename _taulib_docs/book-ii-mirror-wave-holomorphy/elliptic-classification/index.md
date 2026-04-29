---
{
  "projection_kind": "taulib_declaration",
  "title": "elliptic_classification",
  "permalink": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/elliptic-classification/",
  "summary_short": "`def` declaration in `TauLib.BookII.Mirror.WaveHolomorphy`.",
  "declaration_id": "TauLib.BookII.Mirror.WaveHolomorphy::elliptic_classification",
  "declaration_slug": "elliptic-classification",
  "kind": "def",
  "name": "elliptic_classification",
  "module_name": "TauLib.BookII.Mirror.WaveHolomorphy",
  "module_url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/",
  "source_line_start": 74,
  "source_line_end": 79,
  "registry_ids": [
    "II.D70"
  ],
  "related_registry_items": [
    {
      "id": "II.D70",
      "title": "PDE Type Classification",
      "url": "/registry/object/II.D70/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L74-L79",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.WaveHolomorphy",
        "url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L74-L79",
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

- Module: [TauLib.BookII.Mirror.WaveHolomorphy](/verify/taulib/docs/book-ii-mirror-wave-holomorphy/)
- Source path: [`TauLib/BookII/Mirror/WaveHolomorphy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L74-L79)
- Source range: L74-L79
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D70` — PDE Type Classification

## Immediate Comment / Docstring

```lean
/-- [II.D70] The elliptic classification (orthodox Cauchy-Riemann). -/
```

## Source Excerpt

```lean
def elliptic_classification : PDEClassification :=
  { pde_type := .Elliptic
  , has_characteristics := false  -- no real characteristics for elliptic PDE
  , has_max_principle := true     -- maximum principle holds for harmonic functions
  , propagation_isotropic := true -- Laplacian is isotropic
  , hartogs_natural := false }    -- Hartogs is a deep theorem, not natural
```
