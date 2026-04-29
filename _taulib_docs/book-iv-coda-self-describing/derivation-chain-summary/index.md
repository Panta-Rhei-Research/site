---
{
  "projection_kind": "taulib_declaration",
  "title": "DerivationChainSummary",
  "permalink": "/verify/taulib/docs/book-iv-coda-self-describing/derivation-chain-summary/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Coda.SelfDescribing`.",
  "declaration_id": "TauLib.BookIV.Coda.SelfDescribing::DerivationChainSummary",
  "declaration_slug": "derivation-chain-summary",
  "kind": "structure",
  "name": "DerivationChainSummary",
  "module_name": "TauLib.BookIV.Coda.SelfDescribing",
  "module_url": "/verify/taulib/docs/book-iv-coda-self-describing/",
  "source_line_start": 183,
  "source_line_end": 199,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L183-L199",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L183-L199",
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
- Source path: [`TauLib/BookIV/Coda/SelfDescribing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Coda/SelfDescribing.lean#L183-L199)
- Source range: L183-L199
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The complete derivation chain from axioms to predictions.
    Each link is either established (E), tau-effective (T), or conjectural (C). -/
```

## Source Excerpt

```lean
structure DerivationChainSummary where
  /-- Total links. -/
  total_links : Nat := 10
  /-- Description. -/
  chain : List String := [
    "K0-K6 axioms (E)",
    "5 generators (E)",
    "tau^3 fibered product (E)",
    "iota_tau = 2/(pi+e) (E)",
    "5 sector couplings (E)",
    "Boundary characters (T)",
    "Spectral decomposition (T)",
    "Mass ratio R (T)",
    "SI calibration via m_n (T)",
    "m_e = 0.510999 MeV (C)"
  ]
  deriving Repr
```
