---
{
  "projection_kind": "taulib_declaration",
  "title": "probe_tower_15_4",
  "permalink": "/corpus/taulib/docs/book-ii-regularity-pre-yoneda/probe-tower-15-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.PreYoneda`.",
  "declaration_id": "TauLib.BookII.Regularity.PreYoneda::probe_tower_15_4",
  "declaration_slug": "probe-tower-15-4",
  "kind": "theorem",
  "name": "probe_tower_15_4",
  "module_name": "TauLib.BookII.Regularity.PreYoneda",
  "module_url": "/corpus/taulib/docs/book-ii-regularity-pre-yoneda/",
  "source_line_start": 340,
  "source_line_end": 341,
  "registry_ids": [
    "II.R12"
  ],
  "related_registry_items": [
    {
      "id": "II.R12",
      "title": "Probe Naturality Equals Holomorphy",
      "url": "/registry/object/II.R12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L340-L341",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PreYoneda",
        "url": "/corpus/taulib/docs/book-ii-regularity-pre-yoneda/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L340-L341",
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

- Module: [TauLib.BookII.Regularity.PreYoneda](/corpus/taulib/docs/book-ii-regularity-pre-yoneda/)
- Source path: [`TauLib/BookII/Regularity/PreYoneda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L340-L341)
- Source range: L340-L341
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.R12` — Probe Naturality Equals Holomorphy

## Immediate Comment / Docstring

```lean
-- Probe implies tower coherence [II.R12]
```

## Source Excerpt

```lean
theorem probe_tower_15_4 :
    probe_implies_tower_check 15 4 = true := by native_decide
```
