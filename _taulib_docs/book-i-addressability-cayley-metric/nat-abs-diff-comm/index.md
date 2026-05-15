---
{
  "projection_kind": "taulib_declaration",
  "title": "natAbsDiff_comm",
  "permalink": "/corpus/taulib/docs/book-i-addressability-cayley-metric/nat-abs-diff-comm/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.CayleyMetric`.",
  "declaration_id": "TauLib.BookI.Addressability.CayleyMetric::natAbsDiff_comm",
  "declaration_slug": "nat-abs-diff-comm",
  "kind": "theorem",
  "name": "natAbsDiff_comm",
  "module_name": "TauLib.BookI.Addressability.CayleyMetric",
  "module_url": "/corpus/taulib/docs/book-i-addressability-cayley-metric/",
  "source_line_start": 61,
  "source_line_end": 62,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/CayleyMetric.lean#L61-L62",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.CayleyMetric",
        "url": "/corpus/taulib/docs/book-i-addressability-cayley-metric/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/CayleyMetric.lean#L61-L62",
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

- Module: [TauLib.BookI.Addressability.CayleyMetric](/corpus/taulib/docs/book-i-addressability-cayley-metric/)
- Source path: [`TauLib/BookI/Addressability/CayleyMetric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/CayleyMetric.lean#L61-L62)
- Source range: L61-L62
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem natAbsDiff_comm (a b : Nat) : natAbsDiff a b = natAbsDiff b a := by
  unfold natAbsDiff; omega
```
