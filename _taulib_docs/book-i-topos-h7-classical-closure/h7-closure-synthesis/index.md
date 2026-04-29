---
{
  "projection_kind": "taulib_declaration",
  "title": "h7_closure_synthesis",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-classical-closure/h7-closure-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7ClassicalClosure`.",
  "declaration_id": "TauLib.BookI.Topos.H7ClassicalClosure::h7_closure_synthesis",
  "declaration_slug": "h7-closure-synthesis",
  "kind": "theorem",
  "name": "h7_closure_synthesis",
  "module_name": "TauLib.BookI.Topos.H7ClassicalClosure",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-classical-closure/",
  "source_line_start": 208,
  "source_line_end": 230,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L208-L230",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H7ClassicalClosure",
        "url": "/verify/taulib/docs/book-i-topos-h7-classical-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L208-L230",
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

- Module: [TauLib.BookI.Topos.H7ClassicalClosure](/verify/taulib/docs/book-i-topos-h7-classical-closure/)
- Source path: [`TauLib/BookI/Topos/H7ClassicalClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L208-L230)
- Source range: L208-L230
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **H7 PAPER BUNDLE CLOSURE SYNTHESIS — KEYSTONE THEOREM**.

    Wave 33 closes the H7 (tau-topos / Hinge 6) paper bundle as
    the SEVENTH AND FINAL fully formalised paper bundle in
    TauLib.

    Six-clause synthesis packaging the structural content of
    paper §§3-8:

    1. **§3 Cat_τ exists** (Wave 31)
    2. **§4 Subobject classifier Ω_τ = Truth4** (Wave 31)
    3. **§7 four-sector classification** (Wave 32)
    4. **§7 Liar → B paraconsistent** (Wave 5/32)
    5. **§7 Kleene-Rosser → N** (Wave 32)
    6. **§8 classical embedding** (this Wave) -/
```

## Source Excerpt

```lean
theorem h7_closure_synthesis :
    -- Clause 1: Cat_τ exists (subobject classifier four-valued)
    (∀ v : Omega_tau, v = T ∨ v = F ∨ v = B ∨ v = N) ∧
    -- Clause 2: Ω_τ has 4 distinct values
    ((T : Truth4) ≠ F ∧ (T : Truth4) ≠ B ∧ (T : Truth4) ≠ N) ∧
    -- Clause 3: four-sector classification (Liar/TT/Curry/KR)
    (StabilisedValue liarTemplate F B ∧
     StabilisedValue truthTellerTemplate T T ∧
     StabilisedValue kleeneRosserTemplate F N) ∧
    -- Clause 4: paraconsistent contradiction Liar at B
    StabilisedValue liarTemplate F B ∧
    -- Clause 5: paraconsistent vacuum KR at N
    StabilisedValue kleeneRosserTemplate F N ∧
    -- Clause 6: classical {T, F} embeds + non-classical extension
    ((T : Truth4) ≠ F ∧ (∃ v : Truth4, v ≠ T ∧ v ≠ F)) :=
  ⟨subobject_classifier_witness,
   ⟨by decide, by decide, by decide⟩,
   ⟨liar_stabilises_at_Both,
    truth_teller_stabilises_T,
    kleene_rosser_stabilises_at_N F⟩,
   liar_stabilises_at_Both,
   kleene_rosser_stabilises_at_N F,
   ⟨by decide, classical_subquotient_witness⟩⟩
```
