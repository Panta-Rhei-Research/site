---
{
  "projection_kind": "taulib_declaration",
  "title": "arith_preserves_ops_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-arith/arith-preserves-ops-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationArith`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationArith::arith_preserves_ops_check",
  "declaration_slug": "arith-preserves-ops-check",
  "kind": "def",
  "name": "arith_preserves_ops_check",
  "module_name": "TauLib.BookIII.Bridge.TranslationArith",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-arith/",
  "source_line_start": 213,
  "source_line_end": 214,
  "registry_ids": [
    "III.P36"
  ],
  "related_registry_items": [
    {
      "id": "III.P36",
      "title": "Arithmetic Preserves Operations",
      "url": "/registry/object/III.P36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L213-L214",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationArith",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-arith/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L213-L214",
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

- Module: [TauLib.BookIII.Bridge.TranslationArith](/verify/taulib/docs/book-iii-bridge-translation-arith/)
- Source path: [`TauLib/BookIII/Bridge/TranslationArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L213-L214)
- Source range: L213-L214
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P36` — Arithmetic Preserves Operations

## Immediate Comment / Docstring

```lean
/-- [III.P36] Full operation preservation check. -/
```

## Source Excerpt

```lean
def arith_preserves_ops_check (bound db : Nat) : Bool :=
  arith_faithful_check bound db && arith_gcd_check bound db
```
