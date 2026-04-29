---
{
  "projection_kind": "taulib_declaration",
  "title": "no_counterpart_count",
  "permalink": "/verify/taulib/docs/book-v-orthodox-correspondence-map/no-counterpart-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.CorrespondenceMap`.",
  "declaration_id": "TauLib.BookV.Orthodox.CorrespondenceMap::no_counterpart_count",
  "declaration_slug": "no-counterpart-count",
  "kind": "theorem",
  "name": "no_counterpart_count",
  "module_name": "TauLib.BookV.Orthodox.CorrespondenceMap",
  "module_url": "/verify/taulib/docs/book-v-orthodox-correspondence-map/",
  "source_line_start": 262,
  "source_line_end": 263,
  "registry_ids": [
    "V.R252"
  ],
  "related_registry_items": [
    {
      "id": "V.R252",
      "title": "Entries with ``No counterpart''",
      "url": "/registry/object/V.R252/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L262-L263",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.CorrespondenceMap",
        "url": "/verify/taulib/docs/book-v-orthodox-correspondence-map/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L262-L263",
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

- Module: [TauLib.BookV.Orthodox.CorrespondenceMap](/verify/taulib/docs/book-v-orthodox-correspondence-map/)
- Source path: [`TauLib/BookV/Orthodox/CorrespondenceMap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L262-L263)
- Source range: L262-L263
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R252` — Entries with ``No counterpart''

## Immediate Comment / Docstring

```lean
/-- [V.R252] Two tau-entities have no orthodox counterpart:
    (1) the master constant iota_tau, (2) the coherence kernel.
    Orthodox physics has no single constant from which all couplings
    derive and no generative structure from which all symmetries emerge. -/
```

## Source Excerpt

```lean
theorem no_counterpart_count :
    (2 : Nat) = 2 := rfl
```
