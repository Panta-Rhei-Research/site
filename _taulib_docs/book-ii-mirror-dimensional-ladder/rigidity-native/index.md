---
{
  "projection_kind": "taulib_declaration",
  "title": "rigidity_native",
  "permalink": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/rigidity-native/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::rigidity_native",
  "declaration_slug": "rigidity-native",
  "kind": "theorem",
  "name": "rigidity_native",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 492,
  "source_line_end": 497,
  "registry_ids": [
    "II.D76"
  ],
  "related_registry_items": [
    {
      "id": "II.D76",
      "title": "Dimensional Rigidity",
      "url": "/registry/object/II.D76/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L492-L497",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.DimensionalLadder",
        "url": "/verify/taulib/docs/book-ii-mirror-dimensional-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L492-L497",
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

- Module: [TauLib.BookII.Mirror.DimensionalLadder](/verify/taulib/docs/book-ii-mirror-dimensional-ladder/)
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L492-L497)
- Source range: L492-L497
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D76` — Dimensional Rigidity

## Immediate Comment / Docstring

```lean
-- [II.D76] Rigidity values
```

## Source Excerpt

```lean
theorem rigidity_native :
    tau_rigidity.fibration_index = 3 ∧
    tau_rigidity.refinement_dim = 4 ∧
    tau_rigidity.base_factors = 1 ∧
    tau_rigidity.fiber_factors = 2 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> native_decide
```
