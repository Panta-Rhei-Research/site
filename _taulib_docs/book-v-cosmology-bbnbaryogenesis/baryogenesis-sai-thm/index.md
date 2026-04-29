---
{
  "projection_kind": "taulib_declaration",
  "title": "baryogenesis_sai_thm",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/baryogenesis-sai-thm/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BBNBaryogenesis`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNBaryogenesis::baryogenesis_sai_thm",
  "declaration_slug": "baryogenesis-sai-thm",
  "kind": "theorem",
  "name": "baryogenesis_sai_thm",
  "module_name": "TauLib.BookV.Cosmology.BBNBaryogenesis",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/",
  "source_line_start": 283,
  "source_line_end": 288,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L283-L288",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNBaryogenesis",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L283-L288",
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

- Module: [TauLib.BookV.Cosmology.BBNBaryogenesis](/verify/taulib/docs/book-v-cosmology-bbnbaryogenesis/)
- Source path: [`TauLib/BookV/Cosmology/BBNBaryogenesis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNBaryogenesis.lean#L283-L288)
- Source range: L283-L288
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- SA-i mechanism: modulus 5, exponent 15, coefficient 5/6. -/
```

## Source Excerpt

```lean
theorem baryogenesis_sai_thm :
    baryogenesis_sai_mechanism.sai_modulus = 5 ∧
    baryogenesis_sai_mechanism.exponent = 15 ∧
    baryogenesis_sai_mechanism.coeff_num = 5 ∧
    baryogenesis_sai_mechanism.coeff_den = 6 :=
  ⟨rfl, rfl, rfl, rfl⟩
```
