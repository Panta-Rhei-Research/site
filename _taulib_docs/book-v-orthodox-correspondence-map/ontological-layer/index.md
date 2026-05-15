---
{
  "projection_kind": "taulib_declaration",
  "title": "OntologicalLayer",
  "permalink": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/ontological-layer/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Orthodox.CorrespondenceMap`.",
  "declaration_id": "TauLib.BookV.Orthodox.CorrespondenceMap::OntologicalLayer",
  "declaration_slug": "ontological-layer",
  "kind": "inductive",
  "name": "OntologicalLayer",
  "module_name": "TauLib.BookV.Orthodox.CorrespondenceMap",
  "module_url": "/corpus/taulib/docs/book-v-orthodox-correspondence-map/",
  "source_line_start": 139,
  "source_line_end": 144,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L139-L144",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L139-L144",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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
- Source path: [`TauLib/BookV/Orthodox/CorrespondenceMap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L139-L144)
- Source range: L139-L144
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Layer classification in the tau-framework. -/
```

## Source Excerpt

```lean
inductive OntologicalLayer where
  /-- Ontic: H_partial[omega], E₀→E₁, observer-independent. -/
  | Ontic
  /-- Readout: orthodox VM, chart projection, observer-dependent. -/
  | Readout
  deriving Repr, DecidableEq, BEq
```
