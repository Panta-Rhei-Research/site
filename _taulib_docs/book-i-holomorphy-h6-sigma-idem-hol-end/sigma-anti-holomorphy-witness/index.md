---
{
  "projection_kind": "taulib_declaration",
  "title": "sigma_anti_holomorphy_witness",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/sigma-anti-holomorphy-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd::sigma_anti_holomorphy_witness",
  "declaration_slug": "sigma-anti-holomorphy-witness",
  "kind": "theorem",
  "name": "sigma_anti_holomorphy_witness",
  "module_name": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/",
  "source_line_start": 135,
  "source_line_end": 140,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L135-L140",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L135-L140",
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
- Source path: [`TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L135-L140)
- Source range: L135-L140
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §8 Theorem `sigma-anti-holomorphy` — structural
    witness**.

    The σ-conjugate transformer `\bar f = σ_Y ∘ f ∘ σ_X` is
    constructed by two applications of earned composition
    (Wave 29's `earned_associativity_witness` shows this
    composition is well-defined and associative).

    Structurally: σ_X, σ_Y are both StageFuns, so the composite
    σ_Y ∘ (f ∘ σ_X) = σ_Y ∘ f ∘ σ_X is admissible whenever each
    component is, by the earned categorical machine. -/
```

## Source Excerpt

```lean
theorem sigma_anti_holomorphy_witness
    (sigma_X sigma_Y f : StageFun) :
    -- The σ-conjugate is built via earned composition
    sigma_conjugate_transformer sigma_X sigma_Y f =
      StageFun.comp sigma_Y (StageFun.comp f sigma_X) :=
  rfl
```
