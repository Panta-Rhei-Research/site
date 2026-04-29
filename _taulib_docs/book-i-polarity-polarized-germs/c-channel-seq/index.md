---
{
  "projection_kind": "taulib_declaration",
  "title": "c_channel_seq",
  "permalink": "/verify/taulib/docs/book-i-polarity-polarized-germs/c-channel-seq/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.PolarizedGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.PolarizedGerms::c_channel_seq",
  "declaration_slug": "c-channel-seq",
  "kind": "def",
  "name": "c_channel_seq",
  "module_name": "TauLib.BookI.Polarity.PolarizedGerms",
  "module_url": "/verify/taulib/docs/book-i-polarity-polarized-germs/",
  "source_line_start": 43,
  "source_line_end": 43,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L43-L43",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PolarizedGerms",
        "url": "/verify/taulib/docs/book-i-polarity-polarized-germs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L43-L43",
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

- Module: [TauLib.BookI.Polarity.PolarizedGerms](/verify/taulib/docs/book-i-polarity-polarized-germs/)
- Source path: [`TauLib/BookI/Polarity/PolarizedGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L43-L43)
- Source range: L43-L43
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- C-channel sequence at primorial stages: C_max for prime p at bound M_k. -/
```

## Source Excerpt

```lean
def c_channel_seq (p k : TauIdx) : TauIdx := c_max p (primorial k)
```
