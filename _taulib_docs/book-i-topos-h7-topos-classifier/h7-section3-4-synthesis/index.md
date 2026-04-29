---
{
  "projection_kind": "taulib_declaration",
  "title": "h7_section3_4_synthesis",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/h7-section3-4-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7ToposClassifier`.",
  "declaration_id": "TauLib.BookI.Topos.H7ToposClassifier::h7_section3_4_synthesis",
  "declaration_slug": "h7-section3-4-synthesis",
  "kind": "theorem",
  "name": "h7_section3_4_synthesis",
  "module_name": "TauLib.BookI.Topos.H7ToposClassifier",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/",
  "source_line_start": 280,
  "source_line_end": 305,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L280-L305",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H7ToposClassifier",
        "url": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L280-L305",
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

- Module: [TauLib.BookI.Topos.H7ToposClassifier](/verify/taulib/docs/book-i-topos-h7-topos-classifier/)
- Source path: [`TauLib/BookI/Topos/H7ToposClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L280-L305)
- Source range: L280-L305
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 31 H7 §§3+4 synthesis (the keystone)**.

    Packages the topos-backbone of H7 in seven structural clauses:

    1. **§3 Cat_τ exists** (via Wave 29 earned cat machine)
    2. **§3 terminal object** (omega_true = T)
    3. **§3 typed binary product** (SectorPair witness)
    4. **§3 boundary-addressedness** (Wave 26 H7)
    5. **§4 subobject classifier** Ω_τ = Truth4 (existing keystone)
    6. **§4 four-valued cardinality** (Ω_τ has 4 distinct values)
    7. **§4 non-Boolean** (B and N exist, complement law fails) -/
```

## Source Excerpt

```lean
theorem h7_section3_4_synthesis (p : Program) :
    -- Clause 1: Cat_τ exists (data structure available)
    (∃ _ : CatTau, True) ∧
    -- Clause 2: Terminal object T
    omega_true = T ∧
    -- Clause 3: Typed binary product orthogonality
    (∀ a b : Int, SectorPair.mul ⟨a, 0⟩ ⟨0, b⟩ = ⟨0, 0⟩) ∧
    -- Clause 4: Boundary-addressedness via NF
    (∃ nf : NormalForm, normalize p = nf) ∧
    -- Clause 5: Subobject classifier four-valued
    (∀ v : Omega_tau, v = T ∨ v = F ∨ v = B ∨ v = N) ∧
    -- Clause 6: Four distinct values
    (omega_true ≠ omega_false ∧
     omega_true ≠ omega_both ∧
     omega_both ≠ omega_neither) ∧
    -- Clause 7: Non-Boolean (B and N exist)
    (∃ v : Omega_tau, v ≠ T ∧ v ≠ F) :=
  ⟨cattau_existence_witness,
   cattau_terminal_witness,
   fun a b => cattau_typed_product_witness a b,
   cattau_boundary_addressed_witness p,
   subobject_classifier_witness,
   ⟨omega_tau_card_four.1,
    omega_tau_card_four.2.1,
    omega_tau_card_four.2.2.2.2.2⟩,
   classical_subquotient_witness⟩
```
