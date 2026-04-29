---
{
  "projection_kind": "taulib_declaration",
  "title": "h6_section8_9_synthesis",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/h6-section8-9-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd::h6_section8_9_synthesis",
  "declaration_slug": "h6-section8-9-synthesis",
  "kind": "theorem",
  "name": "h6_section8_9_synthesis",
  "module_name": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/",
  "source_line_start": 292,
  "source_line_end": 308,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L292-L308",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L292-L308",
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
- Source path: [`TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L292-L308)
- Source range: L292-L308
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 30 H6 §§8+9 synthesis (closes H6 §§8-9 content)**.

    Packages the four-clause structural significance of paper
    §§8-9:

    1. **σ-conjugate exists**: `\bar f = σ_Y ∘ f ∘ σ_X` is a
       well-defined StageFun via earned composition.

    2. **Idempotent decomposition**: every SectorPair admits the
       canonical e_+/e_- decomposition with orthogonality.

    3. **HolEnd_τ identity**: identity intertwines any
       endomorphism trivially via earned unit law.

    4. **Pre-Yoneda concrete-representability**: every Program
       has a canonical NF address via Wave 26 H7. -/
```

## Source Excerpt

```lean
theorem h6_section8_9_synthesis (sigma_X sigma_Y f : StageFun)
    (s : SectorPair) (n k : TauIdx) (p : Program) :
    -- Clause 1: σ-conjugate well-defined
    sigma_conjugate_transformer sigma_X sigma_Y f =
      StageFun.comp sigma_Y (StageFun.comp f sigma_X) ∧
    -- Clause 2: idempotent decomposition + orthogonality
    (s = SectorPair.add ⟨s.b_sector, 0⟩ ⟨0, s.c_sector⟩ ∧
     SectorPair.mul ⟨s.b_sector, 0⟩ ⟨0, s.c_sector⟩ = ⟨0, 0⟩) ∧
    -- Clause 3: HolEnd_τ identity intertwines
    (StageFun.comp f id_stage).b_fun n k = f.b_fun (reduce n k) k ∧
    -- Clause 4: Pre-Yoneda canonical NF address (Wave 26 cite)
    (∃ nf : NormalForm, normalize p = nf) :=
  ⟨sigma_anti_holomorphy_witness sigma_X sigma_Y f,
   ⟨idem_supported_holomorphy_witness s,
    idem_orthogonality_for_decomposition s⟩,
   holend_identity_intertwines f n k,
   pre_yoneda_collapse_witness p⟩
```
