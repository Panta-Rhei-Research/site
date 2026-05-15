---
{
  "projection_kind": "taulib_declaration",
  "title": "correspondence_functor_not_injective",
  "permalink": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/correspondence-functor-not-injective/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.CorrespondenceMap`.",
  "declaration_id": "TauLib.BookV.Orthodox.CorrespondenceMap::correspondence_functor_not_injective",
  "declaration_slug": "correspondence-functor-not-injective",
  "kind": "theorem",
  "name": "correspondence_functor_not_injective",
  "module_name": "TauLib.BookV.Orthodox.CorrespondenceMap",
  "module_url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/",
  "source_line_start": 243,
  "source_line_end": 244,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L243-L244",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.CorrespondenceMap",
        "url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L243-L244",
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

- Module: [TauLib.BookV.Orthodox.CorrespondenceMap](/corpus/taulib/docs/book-v-orthodox-correspondence-map/)
- Source path: [`TauLib/BookV/Orthodox/CorrespondenceMap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L243-L244)
- Source range: L243-L244
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Phi is NOT injective on objects (chart projection loses information). -/
```

## Source Excerpt

```lean
theorem correspondence_functor_not_injective :
    correspondence_functor.injective = false := rfl
```
