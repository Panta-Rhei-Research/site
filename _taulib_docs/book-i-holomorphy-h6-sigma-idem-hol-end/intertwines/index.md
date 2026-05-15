---
{
  "projection_kind": "taulib_declaration",
  "title": "Intertwines",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/intertwines/",
  "summary_short": "`def` declaration in `TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd::Intertwines",
  "declaration_slug": "intertwines",
  "kind": "def",
  "name": "Intertwines",
  "module_name": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/",
  "source_line_start": 216,
  "source_line_end": 217,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L216-L217",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd",
        "url": "/corpus/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L216-L217",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd](/corpus/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/)
- Source path: [`TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L216-L217)
- Source range: L216-L217
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §9 Definition `holend` — intertwining morphism**.

    A morphism `φ : (X, f) → (Y, g)` is a StageFun φ satisfying
    the intertwining condition `g ∘ φ = φ ∘ f`.

    At TauLib level: an intertwining φ is a StageFun for which
    the equation `StageFun.comp g φ = StageFun.comp φ f` holds
    in the earned category. -/
```

## Source Excerpt

```lean
def Intertwines (f g phi : StageFun) : Prop :=
  StageFun.comp g phi = StageFun.comp phi f
```
