---
{
  "projection_kind": "taulib_declaration",
  "title": "IdentityAsAddressPersistence",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/identity-as-address-persistence/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::IdentityAsAddressPersistence",
  "declaration_slug": "identity-as-address-persistence",
  "kind": "structure",
  "name": "IdentityAsAddressPersistence",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 835,
  "source_line_end": 840,
  "registry_ids": [
    "VII.D34"
  ],
  "related_registry_items": [
    {
      "id": "VII.D34",
      "title": "Identity as Address Persistence",
      "url": "/registry/object/VII.D34/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L835-L840",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L835-L840",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L835-L840)
- Source range: L835-L840
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D34` — Identity as Address Persistence

## Immediate Comment / Docstring

```lean
/-- [VII.D34] Identity as Address Persistence (ch26). Identity of
    an object = persistence of its NF-address through transformations.
    No "bare substrate" needed: identity IS the address trajectory. -/
```

## Source Excerpt

```lean
structure IdentityAsAddressPersistence where
  /-- Identity = NF-address persistence. -/
  address_persistence : Bool := true
  /-- No bare substrate. -/
  no_substrate : Bool := true
  deriving Repr
```
