---
{
  "projection_kind": "taulib_declaration",
  "title": "characteristics_iff_hyperbolic",
  "permalink": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/characteristics-iff-hyperbolic/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.WaveHolomorphy`.",
  "declaration_id": "TauLib.BookII.Mirror.WaveHolomorphy::characteristics_iff_hyperbolic",
  "declaration_slug": "characteristics-iff-hyperbolic",
  "kind": "theorem",
  "name": "characteristics_iff_hyperbolic",
  "module_name": "TauLib.BookII.Mirror.WaveHolomorphy",
  "module_url": "/verify/taulib/docs/book-ii-mirror-wave-holomorphy/",
  "source_line_start": 124,
  "source_line_end": 127,
  "registry_ids": [
    "II.T44"
  ],
  "related_registry_items": [
    {
      "id": "II.T44",
      "title": "Asymmetric Determination",
      "url": "/registry/object/II.T44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L124-L127",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L124-L127",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookII/Mirror/WaveHolomorphy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/WaveHolomorphy.lean#L124-L127)
- Source range: L124-L127
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T44` — Asymmetric Determination

## Immediate Comment / Docstring

```lean
/-- [II.T44] PDE type determines characteristics existence. -/
```

## Source Excerpt

```lean
theorem characteristics_iff_hyperbolic :
    hyperbolic_classification.has_characteristics = true ∧
    elliptic_classification.has_characteristics = false := by
  exact ⟨rfl, rfl⟩
```
