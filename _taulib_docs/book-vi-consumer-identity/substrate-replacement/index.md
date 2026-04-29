---
{
  "projection_kind": "taulib_declaration",
  "title": "SubstrateReplacement",
  "permalink": "/verify/taulib/docs/book-vi-consumer-identity/substrate-replacement/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Consumer.Identity`.",
  "declaration_id": "TauLib.BookVI.Consumer.Identity::SubstrateReplacement",
  "declaration_slug": "substrate-replacement",
  "kind": "structure",
  "name": "SubstrateReplacement",
  "module_name": "TauLib.BookVI.Consumer.Identity",
  "module_url": "/verify/taulib/docs/book-vi-consumer-identity/",
  "source_line_start": 52,
  "source_line_end": 61,
  "registry_ids": [
    "VI.L08"
  ],
  "related_registry_items": [
    {
      "id": "VI.L08",
      "title": "Substrate Replacement Preserves Life-Equivalence",
      "url": "/registry/object/VI.L08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L52-L61",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L52-L61",
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
- Source path: [`TauLib/BookVI/Consumer/Identity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L52-L61)
- Source range: L52-L61
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.L08` — Substrate Replacement Preserves Life-Equivalence

## Immediate Comment / Docstring

```lean
/-- [VI.L08] Substrate Replacement Preserves Life-Equivalence.
    Complete material turnover (every atom replaced) does not
    alter life status, because SelfDesc evaluates code continuity,
    not material identity. Passes the metamorphosis test:
    caterpillar → chrysalis → butterfly preserves identity. -/
```

## Source Excerpt

```lean
structure SubstrateReplacement where
  /-- Material turnover occurs. -/
  material_turnover : Bool := true
  /-- ω-germ code is preserved. -/
  code_preserved : Bool := true
  /-- SelfDesc evaluation is continuous through turnover. -/
  selfdesc_continuous : Bool := true
  /-- Passes metamorphosis test (caterpillar → butterfly). -/
  metamorphosis_test : Bool := true
  deriving Repr
```
