---
{
  "projection_kind": "taulib_declaration",
  "title": "WOmega.trPlus",
  "permalink": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/tr-plus-l184/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.SplitComplexCouplingLift`.",
  "declaration_id": "TauLib.BookI.Polarity.SplitComplexCouplingLift::WOmega.trPlus",
  "declaration_slug": "tr-plus-l184",
  "kind": "def",
  "name": "WOmega.trPlus",
  "module_name": "TauLib.BookI.Polarity.SplitComplexCouplingLift",
  "module_url": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/",
  "source_line_start": 184,
  "source_line_end": 185,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L184-L185",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L184-L185",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookI.Polarity.SplitComplexCouplingLift](/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/)
- Source path: [`TauLib/BookI/Polarity/SplitComplexCouplingLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L184-L185)
- Source range: L184-L185
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Additive trace on WOmega**: lifts `SectorPair.trPlus` to
    TauReal-valued entries.

      `Tr_+(a · e_+ + b · e_-) := a + b`. -/
```

## Source Excerpt

```lean
def WOmega.trPlus (w : WOmega) : TauReal :=
  w.ePlus.add w.eMinus
```
