---
{
  "projection_kind": "taulib_declaration",
  "title": "h6_closure_synthesis",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/h6-closure-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd::h6_closure_synthesis",
  "declaration_slug": "h6-closure-synthesis",
  "kind": "theorem",
  "name": "h6_closure_synthesis",
  "module_name": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/",
  "source_line_start": 339,
  "source_line_end": 362,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L339-L362",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L339-L362",
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
- Source path: [`TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L339-L362)
- Source range: L339-L362
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **H6 PAPER BUNDLE CLOSURE SYNTHESIS — KEYSTONE THEOREM**.

    Wave 30 closes the H6 (holomorphy-first) paper bundle as
    the SIXTH fully formalised paper bundle in TauLib.

    Five-clause synthesis packaging the structural content of
    paper §§4-9:

    1. **§4 Earned Codomain**: D = R'[j]/(j²-1) uniquely forced
       by (CC1)-(CC4) — j² = +1 (Wave 25/28).

    2. **§5 Wave-CR**: hyperbolic wave equation
       e_+ · e_- = 0 vs (1+i)(1-i) ≠ 0 (Wave 27 + Wave 25).

    3. **§6 Diagonal Discipline**: e_+ · e_- = 0 protected by
       DD1-DD4 (Wave 27).

    4. **§7 Earned Categorical Machine**: associativity via
       Wave 26 NF confluence (Wave 29 KEYSTONE).

    5. **§8-9 σ-Idem + HolEnd**: Pre-Yoneda address resolution
       via Wave 26 (this Wave 30).

    All six paper bundles (H1-H6) now structurally formalised
    end-to-end. -/
```

## Source Excerpt

```lean
theorem h6_closure_synthesis (s : SectorPair) (p : Program) :
    -- Clause 1: §4 earned codomain (j² = 1)
    SplitComplex.mul SplitComplex.j_canonical SplitComplex.j_canonical
      = SplitComplex.one ∧
    -- Clause 2: §5+6 protected idempotent orthogonality
    SectorPair.mul e_plus_sector e_minus_sector = ⟨0, 0⟩ ∧
    -- Clause 3: §6 elliptic exclusion (split-complex contrast)
    SplitComplex.mul ⟨1, 1⟩ ⟨1, -1⟩ = SplitComplex.zero ∧
    -- Clause 4: §7 earned associativity (StageFun level)
    (∀ f₁ f₂ f₃ : StageFun,
      StageFun.comp (StageFun.comp f₁ f₂) f₃ =
      StageFun.comp f₁ (StageFun.comp f₂ f₃)) ∧
    -- Clause 5: §8 idempotent-supported decomposition
    s = SectorPair.add ⟨s.b_sector, 0⟩ ⟨0, s.c_sector⟩ ∧
    -- Clause 6: §9 Pre-Yoneda canonical NF address
    (∃ nf : NormalForm, normalize p = nf) :=
  ⟨j_squared_eq_one,
   dd_orthogonal_idempotent_pair_witness,
   split_complex_admits_orthogonal_pair,
   stagefun_comp_assoc,
   idem_supported_holomorphy_witness s,
   pre_yoneda_collapse_witness p⟩

end Tau.Holomorphy
```
