---
{
  "projection_kind": "taulib_declaration",
  "title": "normal_hierarchy_spacings_positive",
  "permalink": "/verify/taulib/docs/book-v-cosmology-neutrino-background/normal-hierarchy-spacings-positive/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.NeutrinoBackground`.",
  "declaration_id": "TauLib.BookV.Cosmology.NeutrinoBackground::normal_hierarchy_spacings_positive",
  "declaration_slug": "normal-hierarchy-spacings-positive",
  "kind": "theorem",
  "name": "normal_hierarchy_spacings_positive",
  "module_name": "TauLib.BookV.Cosmology.NeutrinoBackground",
  "module_url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/",
  "source_line_start": 177,
  "source_line_end": 183,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L177-L183",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NeutrinoBackground",
        "url": "/verify/taulib/docs/book-v-cosmology-neutrino-background/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L177-L183",
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

- Module: [TauLib.BookV.Cosmology.NeutrinoBackground](/verify/taulib/docs/book-v-cosmology-neutrino-background/)
- Source path: [`TauLib/BookV/Cosmology/NeutrinoBackground.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NeutrinoBackground.lean#L177-L183)
- Source range: L177-L183
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All spacings have positive numerators → exponents satisfy q > p > r → m₁ < m₂ < m₃. -/
```

## Source Excerpt

```lean
theorem normal_hierarchy_spacings_positive :
    normal_hierarchy_proof.delta_pq_num > 0 ∧
    normal_hierarchy_proof.delta_pr_num > 0 ∧
    normal_hierarchy_proof.delta_qr_num > 0 :=
  ⟨Nat.zero_lt_of_lt (by omega : 0 < 203),
   Nat.zero_lt_of_lt (by omega : 0 < 609),
   Nat.zero_lt_of_lt (by omega : 0 < 1421)⟩
```
