---
{
  "projection_kind": "taulib_declaration",
  "title": "has_split_cr_form",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-dholomorphic/has-split-cr-form/",
  "summary_short": "`def` declaration in `TauLib.BookI.Holomorphy.DHolomorphic`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DHolomorphic::has_split_cr_form",
  "declaration_slug": "has-split-cr-form",
  "kind": "def",
  "name": "has_split_cr_form",
  "module_name": "TauLib.BookI.Holomorphy.DHolomorphic",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-dholomorphic/",
  "source_line_start": 87,
  "source_line_end": 88,
  "registry_ids": [
    "I.D43"
  ],
  "related_registry_items": [
    {
      "id": "I.D43",
      "title": "Split-CR Equations",
      "url": "/registry/object/I.D43/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L87-L88",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.DHolomorphic",
        "url": "/verify/taulib/docs/book-i-holomorphy-dholomorphic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L87-L88",
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

- Module: [TauLib.BookI.Holomorphy.DHolomorphic](/verify/taulib/docs/book-i-holomorphy-dholomorphic/)
- Source path: [`TauLib/BookI/Holomorphy/DHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L87-L88)
- Source range: L87-L88
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D43` — Split-CR Equations

## Immediate Comment / Docstring

```lean
/-- [I.D43] A function f: SplitComplex → SplitComplex satisfies the split-CR
    form if it factors through sector coordinates as a SectorFun.
    That is, there exist g, h such that f = from_sectors ∘ (g, h) ∘ to_sectors. -/
```

## Source Excerpt

```lean
def has_split_cr_form (f : SplitComplex → SplitComplex) : Prop :=
  ∃ sf : SectorFun, ∀ z : SplitComplex, f z = sf.apply_sc z
```
