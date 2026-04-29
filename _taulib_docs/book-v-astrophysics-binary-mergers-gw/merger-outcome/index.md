---
{
  "projection_kind": "taulib_declaration",
  "title": "MergerOutcome",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/merger-outcome/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Astrophysics.BinaryMergersGW`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BinaryMergersGW::MergerOutcome",
  "declaration_slug": "merger-outcome",
  "kind": "inductive",
  "name": "MergerOutcome",
  "module_name": "TauLib.BookV.Astrophysics.BinaryMergersGW",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/",
  "source_line_start": 158,
  "source_line_end": 165,
  "registry_ids": [
    "V.D135"
  ],
  "related_registry_items": [
    {
      "id": "V.D135",
      "title": "Ringdown Readout",
      "url": "/registry/object/V.D135/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L158-L165",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.BinaryMergersGW",
        "url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L158-L165",
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

- Module: [TauLib.BookV.Astrophysics.BinaryMergersGW](/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/)
- Source path: [`TauLib/BookV/Astrophysics/BinaryMergersGW.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L158-L165)
- Source range: L158-L165
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D135` — Ringdown Readout

## Immediate Comment / Docstring

```lean
/-- [V.D135] Merger outcome: what remains after a compact binary merger. -/
```

## Source Excerpt

```lean
inductive MergerOutcome where
  /-- BH remnant (from BH-BH or massive NS-NS). -/
  | BlackHole
  /-- Massive NS remnant (from light NS-NS). -/
  | MassiveNS
  /-- Hypermassive NS (temporary, collapses to BH). -/
  | HypermassiveNS
  deriving Repr, DecidableEq, BEq
```
