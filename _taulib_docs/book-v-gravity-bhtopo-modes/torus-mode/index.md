---
{
  "projection_kind": "taulib_declaration",
  "title": "TorusMode",
  "permalink": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/torus-mode/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::TorusMode",
  "declaration_slug": "torus-mode",
  "kind": "structure",
  "name": "TorusMode",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 57,
  "source_line_end": 62,
  "registry_ids": [
    "V.D234"
  ],
  "related_registry_items": [
    {
      "id": "V.D234",
      "title": "T² QNM Mode Structure",
      "url": "/registry/object/V.D234/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L57-L62",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/verify/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L57-L62",
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/verify/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L57-L62)
- Source range: L57-L62
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D234` — T² QNM Mode Structure

## Immediate Comment / Docstring

```lean
/-- A torus quasi-normal mode labeled by integer winding numbers (n, m)
    for the outer and inner S¹ cycles respectively. [V.D234]

    Laplacian eigenvalue (in units 1/R²): λ_{n,m} = n² + m²·ι_τ⁻²
    QNM frequency: f_{n,m} ∝ √λ_{n,m} -/
```

## Source Excerpt

```lean
structure TorusMode where
  /-- Outer S¹ winding number (outer horizon cycle). -/
  n : Int
  /-- Inner S¹ winding number (inner horizon cycle, r = R·ι_τ). -/
  m : Int
  deriving Repr
```
