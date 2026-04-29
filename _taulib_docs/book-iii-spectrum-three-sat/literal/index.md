---
{
  "projection_kind": "taulib_declaration",
  "title": "Literal",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-three-sat/literal/",
  "summary_short": "`structure` declaration in `TauLib.BookIII.Spectrum.ThreeSAT`.",
  "declaration_id": "TauLib.BookIII.Spectrum.ThreeSAT::Literal",
  "declaration_slug": "literal",
  "kind": "structure",
  "name": "Literal",
  "module_name": "TauLib.BookIII.Spectrum.ThreeSAT",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-three-sat/",
  "source_line_start": 38,
  "source_line_end": 43,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L38-L43",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.ThreeSAT",
        "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L38-L43",
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

- Module: [TauLib.BookIII.Spectrum.ThreeSAT](/verify/taulib/docs/book-iii-spectrum-three-sat/)
- Source path: [`TauLib/BookIII/Spectrum/ThreeSAT.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L38-L43)
- Source range: L38-L43
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A literal: a variable index with optional negation. -/
```

## Source Excerpt

```lean
structure Literal where
  /-- Variable index (1-indexed: variable x_i uses prime p_i). -/
  var_idx : Nat
  /-- Polarity: true = positive (x_i), false = negated (¬x_i). -/
  positive : Bool
  deriving DecidableEq, Repr
```
