---
{
  "projection_kind": "taulib_declaration",
  "title": "mod_mul_eq",
  "permalink": "/verify/taulib/docs/book-i-polarity-mod-arith/mod-mul-eq/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.ModArith`.",
  "declaration_id": "TauLib.BookI.Polarity.ModArith::mod_mul_eq",
  "declaration_slug": "mod-mul-eq",
  "kind": "theorem",
  "name": "mod_mul_eq",
  "module_name": "TauLib.BookI.Polarity.ModArith",
  "module_url": "/verify/taulib/docs/book-i-polarity-mod-arith/",
  "source_line_start": 83,
  "source_line_end": 84,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L83-L84",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L83-L84",
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

- Module: [TauLib.BookI.Polarity.ModArith](/verify/taulib/docs/book-i-polarity-mod-arith/)
- Source path: [`TauLib/BookI/Polarity/ModArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ModArith.lean#L83-L84)
- Source range: L83-L84
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Modular multiplication: (a * b) % m = ((a % m) * (b % m)) % m. -/
```

## Source Excerpt

```lean
theorem mod_mul_eq (a b m : Nat) : (a * b) % m = ((a % m) * (b % m)) % m :=
  Nat.mul_mod a b m
```
