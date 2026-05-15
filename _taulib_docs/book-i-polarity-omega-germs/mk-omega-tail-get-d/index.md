---
{
  "projection_kind": "taulib_declaration",
  "title": "mk_omega_tail_getD",
  "permalink": "/corpus/taulib/docs/book-i-polarity-omega-germs/mk-omega-tail-get-d/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.OmegaGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaGerms::mk_omega_tail_getD",
  "declaration_slug": "mk-omega-tail-get-d",
  "kind": "theorem",
  "name": "mk_omega_tail_getD",
  "module_name": "TauLib.BookI.Polarity.OmegaGerms",
  "module_url": "/corpus/taulib/docs/book-i-polarity-omega-germs/",
  "source_line_start": 161,
  "source_line_end": 163,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L161-L163",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.OmegaGerms",
        "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L161-L163",
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

- Module: [TauLib.BookI.Polarity.OmegaGerms](/corpus/taulib/docs/book-i-polarity-omega-germs/)
- Source path: [`TauLib/BookI/Polarity/OmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L161-L163)
- Source range: L161-L163
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Component accessor for mk_omega_tail: the i-th component is reduce n (i+1). -/
```

## Source Excerpt

```lean
theorem mk_omega_tail_getD (n d i : Nat) (hi : i < d) :
    (mk_omega_tail n d).components.getD i 0 = reduce n (i + 1) :=
  tail_list_getD n d i hi
```
