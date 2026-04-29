---
{
  "projection_kind": "taulib_declaration",
  "title": "four_sector_classification_witness",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-circularity-full/four-sector-classification-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7CircularityFull`.",
  "declaration_id": "TauLib.BookI.Topos.H7CircularityFull::four_sector_classification_witness",
  "declaration_slug": "four-sector-classification-witness",
  "kind": "theorem",
  "name": "four_sector_classification_witness",
  "module_name": "TauLib.BookI.Topos.H7CircularityFull",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-circularity-full/",
  "source_line_start": 167,
  "source_line_end": 179,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L167-L179",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L167-L179",
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
- Source path: [`TauLib/BookI/Topos/H7CircularityFull.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L167-L179)
- Source range: L167-L179
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §7 Thm `circularity-classification` — KEYSTONE
    structural witness**.

    Four-sector classification: each Truth4 atom {T, F, B, N} is
    realised as a stabilised value by some canonical
    self-referential template:

    - **T**: Truth-teller from seed T (`truth_teller_stabilises_T`)
    - **F**: Truth-teller from seed F (`truth_teller_stabilises_F`)
    - **B**: Liar from seed F (`liar_stabilises_at_Both`)
    - **N**: Kleene-Rosser from any seed
      (`kleene_rosser_stabilises_at_N`)

    Together these witness the paper's claim that the four-element
    bilattice Truth4 is *exhaustive* for paraconsistent
    fixed-point resolution. -/
```

## Source Excerpt

```lean
theorem four_sector_classification_witness :
    -- T-sector witness
    StabilisedValue truthTellerTemplate T T ∧
    -- F-sector witness
    StabilisedValue truthTellerTemplate F F ∧
    -- B-sector witness (Liar)
    StabilisedValue liarTemplate F B ∧
    -- N-sector witness (Kleene-Rosser)
    StabilisedValue kleeneRosserTemplate F N :=
  ⟨truth_teller_stabilises_T,
   truth_teller_stabilises_F,
   liar_stabilises_at_Both,
   kleene_rosser_stabilises_at_N F⟩
```
