---
{
  "projection_kind": "taulib_declaration",
  "title": "WitnessAddress",
  "permalink": "/verify/taulib/docs/book-iii-computation-witness-search/witness-address/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Computation.WitnessSearch`.",
  "declaration_id": "TauLib.BookIII.Computation.WitnessSearch::WitnessAddress",
  "declaration_slug": "witness-address",
  "kind": "structure",
  "name": "WitnessAddress",
  "module_name": "TauLib.BookIII.Computation.WitnessSearch",
  "module_url": "/verify/taulib/docs/book-iii-computation-witness-search/",
  "source_line_start": 42,
  "source_line_end": 48,
  "registry_ids": [
    "III.D55"
  ],
  "related_registry_items": [
    {
      "id": "III.D55",
      "title": "NP Witness as Canonical Address",
      "url": "/registry/object/III.D55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L42-L48",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.WitnessSearch",
        "url": "/verify/taulib/docs/book-iii-computation-witness-search/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L42-L48",
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

- Module: [TauLib.BookIII.Computation.WitnessSearch](/verify/taulib/docs/book-iii-computation-witness-search/)
- Source path: [`TauLib/BookIII/Computation/WitnessSearch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L42-L48)
- Source range: L42-L48
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `III.D55` — NP Witness as Canonical Address

## Immediate Comment / Docstring

```lean
/-- [III.D55] Witness address: a τ-address with its BNF decomposition.
    The witness is self-verifying: BNF components encode the proof. -/
```

## Source Excerpt

```lean
structure WitnessAddress where
  value : TauIdx        -- the witness value
  depth : TauIdx        -- primorial depth
  b_part : TauIdx       -- B-component (multiplicative proof)
  c_part : TauIdx       -- C-component (additive proof)
  x_part : TauIdx       -- X-component (balanced proof)
  deriving Repr, DecidableEq, BEq
```
