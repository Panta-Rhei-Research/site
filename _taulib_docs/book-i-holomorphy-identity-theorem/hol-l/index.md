---
{
  "projection_kind": "taulib_declaration",
  "title": "HolL",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/hol-l/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Holomorphy.IdentityTheorem`.",
  "declaration_id": "TauLib.BookI.Holomorphy.IdentityTheorem::HolL",
  "declaration_slug": "hol-l",
  "kind": "structure",
  "name": "HolL",
  "module_name": "TauLib.BookI.Holomorphy.IdentityTheorem",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/",
  "source_line_start": 192,
  "source_line_end": 194,
  "registry_ids": [
    "I.D49"
  ],
  "related_registry_items": [
    {
      "id": "I.D49",
      "title": "Hol(L)",
      "url": "/registry/object/I.D49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L192-L194",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.IdentityTheorem",
        "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L192-L194",
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

- Module: [TauLib.BookI.Holomorphy.IdentityTheorem](/verify/taulib/docs/book-i-holomorphy-identity-theorem/)
- Source path: [`TauLib/BookI/Holomorphy/IdentityTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L192-L194)
- Source range: L192-L194
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D49` — Hol(L)

## Immediate Comment / Docstring

```lean
/-- [I.D49] Hol(L): the type of τ-holomorphic functions on the algebraic lemniscate.
    By the Identity Theorem, elements of Hol(L) are uniquely determined by
    their values at any single primorial depth. -/
```

## Source Excerpt

```lean
structure HolL where
  /-- The underlying HolFun. -/
  fun_ : HolFun
```
