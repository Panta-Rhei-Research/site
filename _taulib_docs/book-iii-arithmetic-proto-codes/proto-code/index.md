---
{
  "projection_kind": "taulib_declaration",
  "title": "ProtoCode",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/proto-code/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Arithmetic.ProtoCodes`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ProtoCodes::ProtoCode",
  "declaration_slug": "proto-code",
  "kind": "structure",
  "name": "ProtoCode",
  "module_name": "TauLib.BookIII.Arithmetic.ProtoCodes",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/",
  "source_line_start": 42,
  "source_line_end": 47,
  "registry_ids": [
    "III.D61"
  ],
  "related_registry_items": [
    {
      "id": "III.D61",
      "title": "Proto-Code",
      "url": "/registry/object/III.D61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L42-L47",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ProtoCodes",
        "url": "/verify/taulib/docs/book-iii-arithmetic-proto-codes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L42-L47",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIII.Arithmetic.ProtoCodes](/verify/taulib/docs/book-iii-arithmetic-proto-codes/)
- Source path: [`TauLib/BookIII/Arithmetic/ProtoCodes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ProtoCodes.lean#L42-L47)
- Source range: L42-L47
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `III.D61` — Proto-Code

## Immediate Comment / Docstring

```lean
/-- [III.D61] Proto-code: E₁ object with discrete carrier and self-verification
    but no decoder. Has BNF + gauge data but cannot self-modify. -/
```

## Source Excerpt

```lean
structure ProtoCode where
  address : TauIdx        -- the code's τ-address
  depth : TauIdx          -- primorial depth
  rank : TauIdx           -- tower depth at which it stabilizes
  verified : Bool         -- self-verification status
  deriving Repr, DecidableEq, BEq
```
