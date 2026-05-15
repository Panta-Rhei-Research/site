---
{
  "projection_kind": "taulib_declaration",
  "title": "defect_1_is_zero",
  "permalink": "/corpus/taulib/docs/book-iii-physics-positive-regularity/defect-1-is-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.PositiveRegularity`.",
  "declaration_id": "TauLib.BookIII.Physics.PositiveRegularity::defect_1_is_zero",
  "declaration_slug": "defect-1-is-zero",
  "kind": "theorem",
  "name": "defect_1_is_zero",
  "module_name": "TauLib.BookIII.Physics.PositiveRegularity",
  "module_url": "/corpus/taulib/docs/book-iii-physics-positive-regularity/",
  "source_line_start": 227,
  "source_line_end": 228,
  "registry_ids": [
    "III.P14"
  ],
  "related_registry_items": [
    {
      "id": "III.P14",
      "title": "Defect Contractivity",
      "url": "/registry/object/III.P14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L227-L228",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.PositiveRegularity",
        "url": "/corpus/taulib/docs/book-iii-physics-positive-regularity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L227-L228",
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

- Module: [TauLib.BookIII.Physics.PositiveRegularity](/corpus/taulib/docs/book-iii-physics-positive-regularity/)
- Source path: [`TauLib/BookIII/Physics/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L227-L228)
- Source range: L227-L228
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.P14` — Defect Contractivity

## Immediate Comment / Docstring

```lean
/-- [III.P14] Structural: defect at depth 1 is zero. -/
```

## Source Excerpt

```lean
theorem defect_1_is_zero :
    defect_functional 1 = 0 := by native_decide
```
