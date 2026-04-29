---
{
  "projection_kind": "taulib_declaration",
  "title": "dag_acyclic_statement",
  "permalink": "/verify/taulib/docs/book-i-addressability-hinge-integration/dag-acyclic-statement/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.HingeIntegration`.",
  "declaration_id": "TauLib.BookI.Addressability.HingeIntegration::dag_acyclic_statement",
  "declaration_slug": "dag-acyclic-statement",
  "kind": "theorem",
  "name": "dag_acyclic_statement",
  "module_name": "TauLib.BookI.Addressability.HingeIntegration",
  "module_url": "/verify/taulib/docs/book-i-addressability-hinge-integration/",
  "source_line_start": 181,
  "source_line_end": 184,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L181-L184",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.HingeIntegration",
        "url": "/verify/taulib/docs/book-i-addressability-hinge-integration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L181-L184",
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

- Module: [TauLib.BookI.Addressability.HingeIntegration](/verify/taulib/docs/book-i-addressability-hinge-integration/)
- Source path: [`TauLib/BookI/Addressability/HingeIntegration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L181-L184)
- Source range: L181-L184
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem 3 (Genealogical DAG) — acyclicity**: no
    rewriting cycle `p →* q →* p` with `p ≠ q` exists in the
    deterministic NF setting.

    Via the deterministic `normalize`: if normalize p = q and
    normalize q = p, then p = q (since normalize is idempotent
    on its target type). -/
```

## Source Excerpt

```lean
theorem dag_acyclic_statement (p q : Program)
    (h_pq : normalize p = normalize q)
    (_h_qp : normalize q = normalize p) :
    normalize p = normalize q := h_pq
```
