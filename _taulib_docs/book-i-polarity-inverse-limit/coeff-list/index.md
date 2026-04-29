---
{
  "projection_kind": "taulib_declaration",
  "title": "coeff_list",
  "permalink": "/verify/taulib/docs/book-i-polarity-inverse-limit/coeff-list/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.InverseLimit`.",
  "declaration_id": "TauLib.BookI.Polarity.InverseLimit::coeff_list",
  "declaration_slug": "coeff-list",
  "kind": "def",
  "name": "coeff_list",
  "module_name": "TauLib.BookI.Polarity.InverseLimit",
  "module_url": "/verify/taulib/docs/book-i-polarity-inverse-limit/",
  "source_line_start": 118,
  "source_line_end": 120,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L118-L120",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.InverseLimit",
        "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L118-L120",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookI.Polarity.InverseLimit](/verify/taulib/docs/book-i-polarity-inverse-limit/)
- Source path: [`TauLib/BookI/Polarity/InverseLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L118-L120)
- Source range: L118-L120
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Build a list of coefficients `[f 1, f 2, …, f d]` by recursion on
    `d`.  Structurally parallel to the `tail_list` helper in
    `OmegaGerms.lean` but parameterised by an arbitrary coefficient
    function. -/
```

## Source Excerpt

```lean
private def coeff_list (f : TauIdx → TauIdx) : TauIdx → List TauIdx
  | 0 => []
  | d + 1 => coeff_list f d ++ [f (d + 1)]
```
