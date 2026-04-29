---
{
  "projection_kind": "taulib_declaration",
  "title": "is_sector_independent",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-dholomorphic/is-sector-independent/",
  "summary_short": "`def` declaration in `TauLib.BookI.Holomorphy.DHolomorphic`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DHolomorphic::is_sector_independent",
  "declaration_slug": "is-sector-independent",
  "kind": "def",
  "name": "is_sector_independent",
  "module_name": "TauLib.BookI.Holomorphy.DHolomorphic",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-dholomorphic/",
  "source_line_start": 66,
  "source_line_end": 69,
  "registry_ids": [
    "I.P22"
  ],
  "related_registry_items": [
    {
      "id": "I.P22",
      "title": "Sector Independence",
      "url": "/registry/object/I.P22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L66-L69",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L66-L69",
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
- Source path: [`TauLib/BookI/Holomorphy/DHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L66-L69)
- Source range: L66-L69
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.P22` — Sector Independence

## Immediate Comment / Docstring

```lean
/-- [I.P22] A function f: SectorPair → SectorPair is sector-independent if
    its B-output depends only on the B-input and its C-output depends only
    on the C-input. This is the content of the split-CR equations. -/
```

## Source Excerpt

```lean
def is_sector_independent (f : SectorPair → SectorPair) : Prop :=
  ∀ s₁ s₂ : SectorPair,
    (s₁.b_sector = s₂.b_sector → (f s₁).b_sector = (f s₂).b_sector) ∧
    (s₁.c_sector = s₂.c_sector → (f s₁).c_sector = (f s₂).c_sector)
```
