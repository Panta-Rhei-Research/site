---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_idempotent_check",
  "permalink": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-idempotent-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.ChineseRemainder`.",
  "declaration_id": "TauLib.BookI.Polarity.ChineseRemainder::crt_idempotent_check",
  "declaration_slug": "crt-idempotent-check",
  "kind": "def",
  "name": "crt_idempotent_check",
  "module_name": "TauLib.BookI.Polarity.ChineseRemainder",
  "module_url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/",
  "source_line_start": 160,
  "source_line_end": 163,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ChineseRemainder.lean#L160-L163",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.ChineseRemainder",
        "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ChineseRemainder.lean#L160-L163",
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

- Module: [TauLib.BookI.Polarity.ChineseRemainder](/verify/taulib/docs/book-i-polarity-chinese-remainder/)
- Source path: [`TauLib/BookI/Polarity/ChineseRemainder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ChineseRemainder.lean#L160-L163)
- Source range: L160-L163
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- eᵢ · eᵢ ≡ eᵢ (mod M_k): each basis element is idempotent. -/
```

## Source Excerpt

```lean
def crt_idempotent_check (k i : TauIdx) : Bool :=
  let mk := primorial k
  let ei := crt_basis k i
  (ei * ei) % mk == ei
```
