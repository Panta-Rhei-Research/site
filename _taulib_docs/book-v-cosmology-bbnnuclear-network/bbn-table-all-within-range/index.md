---
{
  "projection_kind": "taulib_declaration",
  "title": "bbn_table_all_within_range",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbn-table-all-within-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::bbn_table_all_within_range",
  "declaration_slug": "bbn-table-all-within-range",
  "kind": "theorem",
  "name": "bbn_table_all_within_range",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 428,
  "source_line_end": 434,
  "registry_ids": [
    "V.P169"
  ],
  "related_registry_items": [
    {
      "id": "V.P169",
      "title": "BBN Table Consistency",
      "url": "/registry/object/V.P169/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L428-L434",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
        "url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L428-L434",
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

- Module: [TauLib.BookV.Cosmology.BBNNuclearNetwork](/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/)
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L428-L434)
- Source range: L428-L434
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P169` — BBN Table Consistency

## Immediate Comment / Docstring

```lean
/-- [V.P169] All four predictions within observational range. -/
```

## Source Excerpt

```lean
theorem bbn_table_all_within_range :
    complete_bbn_table.yp_ok = true ∧
    complete_bbn_table.dh_ok = true ∧
    complete_bbn_table.he3_ok = true ∧
    complete_bbn_table.li7_ok = true ∧
    complete_bbn_table.n_free_params = 0 :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩
```
