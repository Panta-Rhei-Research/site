---
{
  "projection_kind": "taulib_declaration",
  "title": "RationalityRequirement",
  "permalink": "/verify/taulib/docs/book-v-coda-bridge-to-life/rationality-requirement/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Coda.BridgeToLife`.",
  "declaration_id": "TauLib.BookV.Coda.BridgeToLife::RationalityRequirement",
  "declaration_slug": "rationality-requirement",
  "kind": "structure",
  "name": "RationalityRequirement",
  "module_name": "TauLib.BookV.Coda.BridgeToLife",
  "module_url": "/verify/taulib/docs/book-v-coda-bridge-to-life/",
  "source_line_start": 282,
  "source_line_end": 291,
  "registry_ids": [
    "V.P108"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L282-L291",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Coda.BridgeToLife",
        "url": "/verify/taulib/docs/book-v-coda-bridge-to-life/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L282-L291",
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

- Module: [TauLib.BookV.Coda.BridgeToLife](/verify/taulib/docs/book-v-coda-bridge-to-life/)
- Source path: [`TauLib/BookV/Coda/BridgeToLife.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Coda/BridgeToLife.lean#L282-L291)
- Source range: L282-L291
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.P108] Rationality requirement: a BSD triple (chi_met, chi_rep,
    chi_err) is viable for a self-enriching E2 entity only if all
    three characters factor through a finite quotient.

    This ensures the entity can be described by finite data at each
    stage. An entity that requires infinite precision in its boundary
    characters cannot self-enrich (cannot compute its own evolution). -/
```

## Source Excerpt

```lean
structure RationalityRequirement where
  /-- Number of characters in the BSD triple. -/
  triple_size : Nat
  /-- Always 3. -/
  triple_eq : triple_size = 3
  /-- All must factor through finite quotient. -/
  all_factor_finite : Bool := true
  /-- Required for self-enrichment. -/
  required_for_e2 : Bool := true
  deriving Repr
```
