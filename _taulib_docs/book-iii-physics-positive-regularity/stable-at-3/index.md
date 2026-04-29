---
{
  "projection_kind": "taulib_declaration",
  "title": "stable_at_3",
  "permalink": "/verify/taulib/docs/book-iii-physics-positive-regularity/stable-at-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.PositiveRegularity`.",
  "declaration_id": "TauLib.BookIII.Physics.PositiveRegularity::stable_at_3",
  "declaration_slug": "stable-at-3",
  "kind": "theorem",
  "name": "stable_at_3",
  "module_name": "TauLib.BookIII.Physics.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-iii-physics-positive-regularity/",
  "source_line_start": 231,
  "source_line_end": 234,
  "registry_ids": [
    "III.P15"
  ],
  "related_registry_items": [
    {
      "id": "III.P15",
      "title": "3-Condition Sufficiency",
      "url": "/registry/object/III.P15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L231-L234",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L231-L234",
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
- Source path: [`TauLib/BookIII/Physics/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L231-L234)
- Source range: L231-L234
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P15` — 3-Condition Sufficiency

## Immediate Comment / Docstring

```lean
/-- [III.P15] Structural: is_stable at every tested level. -/
```

## Source Excerpt

```lean
theorem stable_at_3 :
    is_stable 3 = true := by native_decide

end Tau.BookIII.Physics
```
