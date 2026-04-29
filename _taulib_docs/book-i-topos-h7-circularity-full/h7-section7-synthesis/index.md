---
{
  "projection_kind": "taulib_declaration",
  "title": "h7_section7_synthesis",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-circularity-full/h7-section7-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7CircularityFull`.",
  "declaration_id": "TauLib.BookI.Topos.H7CircularityFull::h7_section7_synthesis",
  "declaration_slug": "h7-section7-synthesis",
  "kind": "theorem",
  "name": "h7_section7_synthesis",
  "module_name": "TauLib.BookI.Topos.H7CircularityFull",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-circularity-full/",
  "source_line_start": 226,
  "source_line_end": 241,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L226-L241",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H7CircularityFull",
        "url": "/verify/taulib/docs/book-i-topos-h7-circularity-full/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L226-L241",
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

- Module: [TauLib.BookI.Topos.H7CircularityFull](/verify/taulib/docs/book-i-topos-h7-circularity-full/)
- Source path: [`TauLib/BookI/Topos/H7CircularityFull.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L226-L241)
- Source range: L226-L241
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 32 H7 §7 synthesis (the KEYSTONE)**.

    Packages the four-sector classification of paper §7's
    `thm:circularity-classification` in five clauses:

    1. **§7 Liar**: paraconsistent contradiction → B
    2. **§7 Truth-teller**: consistent affirmation → T (or F)
    3. **§7 Curry**: paraconsistent equivalent of Liar → B
    4. **§7 Kleene-Rosser**: paraconsistent vacuum → N
    5. **Sub-classifier link**: Truth4 is the subobject
       classifier (Wave 31), so the four-sector classification
       IS the structural content of paraconsistent
       fixed-point resolution. -/
```

## Source Excerpt

```lean
theorem h7_section7_synthesis :
    -- Clause 1: Liar → B
    StabilisedValue liarTemplate F B ∧
    -- Clause 2: Truth-teller → T
    StabilisedValue truthTellerTemplate T T ∧
    -- Clause 3: Curry → B
    StabilisedValue curryTemplate F B ∧
    -- Clause 4: Kleene-Rosser → N
    StabilisedValue kleeneRosserTemplate F N ∧
    -- Clause 5: Truth4 has 4 distinct values (subobject classifier)
    (∀ v : Omega_tau, v = T ∨ v = F ∨ v = B ∨ v = N) :=
  ⟨h7_liar_at_both,
   h7_truth_teller_at_T,
   h7_curry_at_both,
   h7_kleene_rosser_at_N,
   subobject_classifier_witness⟩
```
