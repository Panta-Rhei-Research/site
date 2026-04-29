---
{
  "projection_kind": "taulib_declaration",
  "title": "self_model_idempotent_3",
  "permalink": "/verify/taulib/docs/book-iii-mirror-e3-witness/self-model-idempotent-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Mirror.E3Witness`.",
  "declaration_id": "TauLib.BookIII.Mirror.E3Witness::self_model_idempotent_3",
  "declaration_slug": "self-model-idempotent-3",
  "kind": "theorem",
  "name": "self_model_idempotent_3",
  "module_name": "TauLib.BookIII.Mirror.E3Witness",
  "module_url": "/verify/taulib/docs/book-iii-mirror-e3-witness/",
  "source_line_start": 254,
  "source_line_end": 255,
  "registry_ids": [
    "III.P35"
  ],
  "related_registry_items": [
    {
      "id": "III.P35",
      "title": "Saturation Semantics",
      "url": "/registry/object/III.P35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L254-L255",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.E3Witness",
        "url": "/verify/taulib/docs/book-iii-mirror-e3-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L254-L255",
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

- Module: [TauLib.BookIII.Mirror.E3Witness](/verify/taulib/docs/book-iii-mirror-e3-witness/)
- Source path: [`TauLib/BookIII/Mirror/E3Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L254-L255)
- Source range: L254-L255
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P35` — Saturation Semantics

## Immediate Comment / Docstring

```lean
/-- [III.P35] Self-model idempotent at stages 1-3. -/
```

## Source Excerpt

```lean
theorem self_model_idempotent_3 :
    self_model_idempotent_check 3 = true := by native_decide
```
