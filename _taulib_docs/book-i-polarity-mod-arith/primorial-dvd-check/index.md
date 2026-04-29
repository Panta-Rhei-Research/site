---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_dvd_check",
  "permalink": "/verify/taulib/docs/book-i-polarity-mod-arith/primorial-dvd-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.ModArith`.",
  "declaration_id": "TauLib.BookI.Polarity.ModArith::primorial_dvd_check",
  "declaration_slug": "primorial-dvd-check",
  "kind": "def",
  "name": "primorial_dvd_check",
  "module_name": "TauLib.BookI.Polarity.ModArith",
  "module_url": "/verify/taulib/docs/book-i-polarity-mod-arith/",
  "source_line_start": 66,
  "source_line_end": 67,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L66-L67",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.ModArith",
        "url": "/verify/taulib/docs/book-i-polarity-mod-arith/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L66-L67",
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

- Module: [TauLib.BookI.Polarity.ModArith](/verify/taulib/docs/book-i-polarity-mod-arith/)
- Source path: [`TauLib/BookI/Polarity/ModArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L66-L67)
- Source range: L66-L67
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Primorial divisibility: M_k divides M_ℓ when k ≤ ℓ.
    Computable check. -/
```

## Source Excerpt

```lean
def primorial_dvd_check (k l : TauIdx) : Bool :=
  k ≤ l && primorial l % primorial k == 0
```
