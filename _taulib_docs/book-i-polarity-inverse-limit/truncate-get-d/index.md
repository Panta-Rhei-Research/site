---
{
  "projection_kind": "taulib_declaration",
  "title": "OmegaInverseLimit.truncate_getD",
  "permalink": "/corpus/taulib/docs/book-i-polarity-inverse-limit/truncate-get-d/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.InverseLimit`.",
  "declaration_id": "TauLib.BookI.Polarity.InverseLimit::OmegaInverseLimit.truncate_getD",
  "declaration_slug": "truncate-get-d",
  "kind": "theorem",
  "name": "OmegaInverseLimit.truncate_getD",
  "module_name": "TauLib.BookI.Polarity.InverseLimit",
  "module_url": "/corpus/taulib/docs/book-i-polarity-inverse-limit/",
  "source_line_start": 159,
  "source_line_end": 162,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L159-L162",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.InverseLimit",
        "url": "/corpus/taulib/docs/book-i-polarity-inverse-limit/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L159-L162",
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

- Module: [TauLib.BookI.Polarity.InverseLimit](/corpus/taulib/docs/book-i-polarity-inverse-limit/)
- Source path: [`TauLib/BookI/Polarity/InverseLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L159-L162)
- Source range: L159-L162
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The truncation's i-th component is `t.coeff (i + 1)`. -/
```

## Source Excerpt

```lean
theorem OmegaInverseLimit.truncate_getD
    (t : OmegaInverseLimit) (d i : TauIdx) (hi : i < d) :
    (t.truncate d).components.getD i 0 = t.coeff (i + 1) :=
  coeff_list_getD t.coeff d i hi
```
