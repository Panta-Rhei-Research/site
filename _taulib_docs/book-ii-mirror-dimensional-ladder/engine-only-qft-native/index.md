---
{
  "projection_kind": "taulib_declaration",
  "title": "engine_only_qft_native",
  "permalink": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/engine-only-qft-native/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Mirror.DimensionalLadder`.",
  "declaration_id": "TauLib.BookII.Mirror.DimensionalLadder::engine_only_qft_native",
  "declaration_slug": "engine-only-qft-native",
  "kind": "theorem",
  "name": "engine_only_qft_native",
  "module_name": "TauLib.BookII.Mirror.DimensionalLadder",
  "module_url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/",
  "source_line_start": 484,
  "source_line_end": 489,
  "registry_ids": [
    "II.D75"
  ],
  "related_registry_items": [
    {
      "id": "II.D75",
      "title": "Archimedean-Elliptic Engine",
      "url": "/registry/object/II.D75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L484-L489",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Mirror.DimensionalLadder",
        "url": "/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L484-L489",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookII.Mirror.DimensionalLadder](/corpus/taulib/docs/book-ii-mirror-dimensional-ladder/)
- Source path: [`TauLib/BookII/Mirror/DimensionalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Mirror/DimensionalLadder.lean#L484-L489)
- Source range: L484-L489
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.D75` — Archimedean-Elliptic Engine

## Immediate Comment / Docstring

```lean
-- ============================================================
-- FORMAL VERIFICATION (native_decide)
-- ============================================================

-- [II.D75] Engine active only in QFT quadrant
```

## Source Excerpt

```lean
theorem engine_only_qft_native :
    engine_active qft_quadrant = true ∧
    engine_active gr_local_quadrant = false ∧
    engine_active padic_quadrant = false ∧
    engine_active tau_quadrant = false := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> native_decide
```
