---
{
  "projection_kind": "taulib_declaration",
  "title": "SelfDescOverCode",
  "permalink": "/verify/taulib/docs/book-vi-consumer-identity/self-desc-over-code/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Identity`.",
  "declaration_id": "TauLib.BookVI.Consumer.Identity::SelfDescOverCode",
  "declaration_slug": "self-desc-over-code",
  "kind": "structure",
  "name": "SelfDescOverCode",
  "module_name": "TauLib.BookVI.Consumer.Identity",
  "module_url": "/verify/taulib/docs/book-vi-consumer-identity/",
  "source_line_start": 32,
  "source_line_end": 39,
  "registry_ids": [
    "VI.D53"
  ],
  "related_registry_items": [
    {
      "id": "VI.D53",
      "title": "SelfDesc over Code, Not Carrier",
      "url": "/registry/object/VI.D53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L32-L39",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Identity",
        "url": "/verify/taulib/docs/book-vi-consumer-identity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L32-L39",
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

- Module: [TauLib.BookVI.Consumer.Identity](/verify/taulib/docs/book-vi-consumer-identity/)
- Source path: [`TauLib/BookVI/Consumer/Identity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L32-L39)
- Source range: L32-L39
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.D53` — SelfDesc over Code, Not Carrier

## Immediate Comment / Docstring

```lean
/-- [VI.D53] SelfDesc over Code, Not Carrier.
    Biological identity resides in the ω-germ code (Book II, Part X),
    not in the material carrier. The profinite invariant is preserved
    under complete material turnover. -/
```

## Source Excerpt

```lean
structure SelfDescOverCode where
  /-- Identity locus is the ω-germ code. -/
  identity_locus : String := "omega_germ_code"
  /-- Identity is NOT in the carrier. -/
  not_carrier : Bool := true
  /-- The ω-germ code is a profinite invariant (Book II, Part X). -/
  profinite_invariant : Bool := true
  deriving Repr
```
