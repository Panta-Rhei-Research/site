---
{
  "projection_kind": "taulib_declaration",
  "title": "h8_girard_linear_embedding_synthesis",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/h8-girard-linear-embedding-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.KernelFoundation.GirardLinearEmbedding`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding::h8_girard_linear_embedding_synthesis",
  "declaration_slug": "h8-girard-linear-embedding-synthesis",
  "kind": "theorem",
  "name": "h8_girard_linear_embedding_synthesis",
  "module_name": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/",
  "source_line_start": 273,
  "source_line_end": 293,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L273-L293",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.GirardLinearEmbedding",
        "url": "/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L273-L293",
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

- Module: [TauLib.BookI.KernelFoundation.GirardLinearEmbedding](/verify/taulib/docs/book-i-kernel-foundation-girard-linear-embedding/)
- Source path: [`TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/GirardLinearEmbedding.lean#L273-L293)
- Source range: L273-L293
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 36 H8 Girard linear-logic embedding synthesis (KEYSTONE)**.

    Packages the four-clause structural significance of paper §3:

    1. **Structural rules**: contraction REFUSED, weakening REFUSED,
       exchange ADMITTED in !-free linear fragment
    2. **Connective tiers**: 4 connectives split into multiplicatives
       (⊗, ⅋) and additives (&, ⊕)
    3. **Cut rule**: signature available as binary operation on sequents
    4. **Diagonal–linear bijection**: K5 ↔ !-free linear logic via
       round-trip witness

    Together they witness paper §3's diagonal–linear correspondence
    at the structural-content level, matching the paper's framing
    scope ("structural isomorphism, not formal isomorphism"). -/
```

## Source Excerpt

```lean
theorem h8_girard_linear_embedding_synthesis :
    -- Clause 1: linear fragment signature (only exchange admitted)
    (allStructuralRules.filter (·.admittedInLinear)).length = 1 ∧
    -- Clause 2: tensor and par are multiplicative
    (Formula.tier (Formula.tensor (.atom 0) (.atom 1)) = some .multiplicative ∧
     Formula.tier (Formula.par (.atom 0) (.atom 1)) = some .multiplicative) ∧
    -- Clause 2 cont: with and plus are additive
    (Formula.tier (Formula.wth (.atom 0) (.atom 1)) = some .additive ∧
     Formula.tier (Formula.plus (.atom 0) (.atom 1)) = some .additive) ∧
    -- Clause 3: cut rule signature available
    (∀ s1 s2 : Sequent, ∀ a : Formula,
       s1.succedent = [a] → s2.antecedent.head? = some a →
       ∃ s : Sequent, cutSequent s1 s2 a = some s) ∧
    -- Clause 4: diagonal–linear bijection (Wave 34 cite)
    ((∀ d : DiagonalAspect, linear_to_diag (diag_to_linear d) = d) ∧
     (∀ l : LinearAspect, diag_to_linear (linear_to_diag l) = l)) :=
  ⟨linear_fragment_signature,
   ⟨tensor_is_multiplicative _ _, par_is_multiplicative _ _⟩,
   ⟨wth_is_additive _ _, plus_is_additive _ _⟩,
   fun s1 s2 a h1 h2 => cut_produces_sequent_when_applicable s1 s2 a h1 h2,
   diagonal_linear_correspondence_witness⟩
```
