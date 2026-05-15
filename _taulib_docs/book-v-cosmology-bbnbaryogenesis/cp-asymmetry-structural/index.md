---
{
  "projection_kind": "taulib_declaration",
  "title": "cp_asymmetry_structural",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/cp-asymmetry-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNBaryogenesis::cp_asymmetry_structural",
  "declaration_slug": "cp-asymmetry-structural",
  "kind": "theorem",
  "name": "cp_asymmetry_structural",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "source_line_start": 489,
  "source_line_end": 493,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L489-L493",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNBaryogenesis",
        "url": "/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L489-L493",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookV.Cosmology.BBNBaryogenesis](/corpus/taulib/docs/book-v-cosmology-bbnbaryogenesis/)
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L489-L493)
- Source range: L489-L493
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CP asymmetry structural: ε_CP = ι_τ, total = ι_τ¹⁵. -/
```

## Source Excerpt

```lean
theorem cp_asymmetry_structural :
    cp_asymmetry_polarity.cp_scale_is_iota = true ∧
    cp_asymmetry_polarity.total_matches_sai_mod5 = true ∧
    cp_asymmetry_polarity.connects_to_pmns = true :=
  ⟨rfl, rfl, rfl⟩
```
