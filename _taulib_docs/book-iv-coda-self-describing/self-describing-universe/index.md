---
{
  "projection_kind": "taulib_declaration",
  "title": "SelfDescribingUniverse",
  "permalink": "/verify/taulib/docs/book-iv-coda-self-describing/self-describing-universe/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.SelfDescribing`.",
  "declaration_id": "TauLib.BookIV.Coda.SelfDescribing::SelfDescribingUniverse",
  "declaration_slug": "self-describing-universe",
  "kind": "structure",
  "name": "SelfDescribingUniverse",
  "module_name": "TauLib.BookIV.Coda.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-iv-coda-self-describing/",
  "source_line_start": 225,
  "source_line_end": 238,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L225-L238",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Coda.SelfDescribing",
        "url": "/verify/taulib/docs/book-iv-coda-self-describing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L225-L238",
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

- Module: [TauLib.BookIV.Coda.SelfDescribing](/verify/taulib/docs/book-iv-coda-self-describing/)
- Source path: [`TauLib/BookIV/Coda/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L225-L238)
- Source range: L225-L238
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The title-theorem of Book IV: the universe described by tau^3 is
    self-describing.

    Self-description means:
    1. The laws governing tau^3 are objects of tau^3 (self-enrichment)
    2. The constants of nature are readouts of structural invariants
    3. The framework determines itself (no external input besides m_n)
    4. The fiber T^2 contains complete spatial physics
    5. The base tau^1 contains complete temporal physics

    Together: tau^3 = tau^1 x_f T^2 describes a complete, self-contained
    physical universe with zero free parameters. -/
```

## Source Excerpt

```lean
structure SelfDescribingUniverse where
  /-- Laws are internal objects. -/
  laws_internal : Bool := true
  /-- Constants are structural readouts. -/
  constants_readouts : Bool := true
  /-- Self-determined (modulo m_n). -/
  self_determined : Bool := true
  /-- Fiber: complete spatial physics. -/
  fiber_complete : Bool := true
  /-- Base: complete temporal physics. -/
  base_complete : Bool := true
  /-- Zero free parameters. -/
  zero_params : Nat := 0
  deriving Repr
```
