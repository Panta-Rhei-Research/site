---
{
  "projection_kind": "taulib_declaration",
  "title": "SectorPair.trMinus_add",
  "permalink": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/tr-minus-add/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.SplitComplexCouplingLift`.",
  "declaration_id": "TauLib.BookI.Polarity.SplitComplexCouplingLift::SectorPair.trMinus_add",
  "declaration_slug": "tr-minus-add",
  "kind": "theorem",
  "name": "SectorPair.trMinus_add",
  "module_name": "TauLib.BookI.Polarity.SplitComplexCouplingLift",
  "module_url": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/",
  "source_line_start": 157,
  "source_line_end": 161,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L157-L161",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.SplitComplexCouplingLift",
        "url": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L157-L161",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Polarity.SplitComplexCouplingLift](/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/)
- Source path: [`TauLib/BookI/Polarity/SplitComplexCouplingLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L157-L161)
- Source range: L157-L161
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Tr_- is additive** on SectorPair sums. -/
```

## Source Excerpt

```lean
theorem SectorPair.trMinus_add (a b : SectorPair) :
    SectorPair.trMinus (SectorPair.add a b) =
      SectorPair.trMinus a + SectorPair.trMinus b := by
  unfold SectorPair.trMinus SectorPair.add
  ring
```
