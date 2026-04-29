---
{
  "projection_kind": "taulib_declaration",
  "title": "GapType",
  "permalink": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/gap-type/",
  "summary_short": "`inductive` declaration in `TauLib.BookIII.Bridge.ConjectureGaps`.",
  "declaration_id": "TauLib.BookIII.Bridge.ConjectureGaps::GapType",
  "declaration_slug": "gap-type",
  "kind": "inductive",
  "name": "GapType",
  "module_name": "TauLib.BookIII.Bridge.ConjectureGaps",
  "module_url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/",
  "source_line_start": 85,
  "source_line_end": 89,
  "registry_ids": [
    "III.D112"
  ],
  "related_registry_items": [
    {
      "id": "III.D112",
      "title": "Gap Type",
      "url": "/registry/object/III.D112/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L85-L89",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ConjectureGaps",
        "url": "/verify/taulib/docs/book-iii-bridge-conjecture-gaps/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L85-L89",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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

- Module: [TauLib.BookIII.Bridge.ConjectureGaps](/verify/taulib/docs/book-iii-bridge-conjecture-gaps/)
- Source path: [`TauLib/BookIII/Bridge/ConjectureGaps.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L85-L89)
- Source range: L85-L89
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `III.D112` — Gap Type

## Immediate Comment / Docstring

```lean
/-- [III.D112] The three gap types for additive conjectures. -/
```

## Source Excerpt

```lean
inductive GapType where
  | parity      -- Goldbach: parity barrier blocks sieve lifting
  | density     -- Twin primes: need equidistribution for infinitude
  | structural  -- ABC: primorial tower avoids the hard case
  deriving Repr, DecidableEq, BEq
```
