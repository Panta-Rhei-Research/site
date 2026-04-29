---
{
  "projection_kind": "taulib_declaration",
  "title": "holend_composition_intertwines",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/holend-composition-intertwines/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd::holend_composition_intertwines",
  "declaration_slug": "holend-composition-intertwines",
  "kind": "theorem",
  "name": "holend_composition_intertwines",
  "module_name": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/",
  "source_line_start": 233,
  "source_line_end": 240,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L233-L240",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd",
        "url": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L233-L240",
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

- Module: [TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd](/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/)
- Source path: [`TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L233-L240)
- Source range: L233-L240
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §9 Prop `holend-is-cat` — composition closure**.

    The composition of two intertwiners is an intertwiner.
    Direct from earned associativity (Wave 29). -/
```

## Source Excerpt

```lean
theorem holend_composition_intertwines
    (f g h phi psi : StageFun)
    (_h_phi : Intertwines f g phi)
    (h_psi : Intertwines g h psi) :
    -- Goal: h ∘ (ψ ∘ φ) = ψ ∘ (g ∘ φ) via earned associativity
    StageFun.comp h (StageFun.comp psi phi) =
    StageFun.comp psi (StageFun.comp g phi) := by
  rw [← stagefun_comp_assoc, h_psi, stagefun_comp_assoc]
```
