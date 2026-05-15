---
{
  "projection_kind": "taulib_declaration",
  "title": "abcd_zero_3",
  "permalink": "/corpus/taulib/docs/book-iii-physics-fluid-data/abcd-zero-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.FluidData`.",
  "declaration_id": "TauLib.BookIII.Physics.FluidData::abcd_zero_3",
  "declaration_slug": "abcd-zero-3",
  "kind": "theorem",
  "name": "abcd_zero_3",
  "module_name": "TauLib.BookIII.Physics.FluidData",
  "module_url": "/corpus/taulib/docs/book-iii-physics-fluid-data/",
  "source_line_start": 236,
  "source_line_end": 237,
  "registry_ids": [
    "III.D38"
  ],
  "related_registry_items": [
    {
      "id": "III.D38",
      "title": "Fluid Sector Decomposition",
      "url": "/registry/object/III.D38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L236-L237",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.FluidData",
        "url": "/corpus/taulib/docs/book-iii-physics-fluid-data/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L236-L237",
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

- Module: [TauLib.BookIII.Physics.FluidData](/corpus/taulib/docs/book-iii-physics-fluid-data/)
- Source path: [`TauLib/BookIII/Physics/FluidData.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/FluidData.lean#L236-L237)
- Source range: L236-L237
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D38` — Fluid Sector Decomposition

## Immediate Comment / Docstring

```lean
/-- [III.D38] Structural: ABCD of 0 is always zero. -/
```

## Source Excerpt

```lean
theorem abcd_zero_3 :
    abcd_extract 0 3 = ⟨3, 0, 0, 0⟩ := by native_decide
```
