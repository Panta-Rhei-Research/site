---
{
  "projection_kind": "taulib_declaration",
  "title": "stab_germ_0_3",
  "permalink": "/verify/taulib/docs/book-iii-physics-positive-regularity/stab-germ-0-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.PositiveRegularity`.",
  "declaration_id": "TauLib.BookIII.Physics.PositiveRegularity::stab_germ_0_3",
  "declaration_slug": "stab-germ-0-3",
  "kind": "theorem",
  "name": "stab_germ_0_3",
  "module_name": "TauLib.BookIII.Physics.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-iii-physics-positive-regularity/",
  "source_line_start": 223,
  "source_line_end": 224,
  "registry_ids": [
    "III.D42"
  ],
  "related_registry_items": [
    {
      "id": "III.D42",
      "title": "Stabilized ω-Germ",
      "url": "/registry/object/III.D42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L223-L224",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.PositiveRegularity",
        "url": "/verify/taulib/docs/book-iii-physics-positive-regularity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L223-L224",
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

- Module: [TauLib.BookIII.Physics.PositiveRegularity](/verify/taulib/docs/book-iii-physics-positive-regularity/)
- Source path: [`TauLib/BookIII/Physics/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L223-L224)
- Source range: L223-L224
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D42` — Stabilized ω-Germ

## Immediate Comment / Docstring

```lean
/-- [III.D42] Structural: stabilized germ of 0 is zero BNF. -/
```

## Source Excerpt

```lean
theorem stab_germ_0_3 :
    stabilized_germ 0 3 = ⟨0, 0, 0, 3⟩ := by native_decide
```
