---
{
  "projection_kind": "taulib_declaration",
  "title": "selectivity_threshold",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/selectivity-threshold/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::selectivity_threshold",
  "declaration_slug": "selectivity-threshold",
  "kind": "theorem",
  "name": "selectivity_threshold",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 388,
  "source_line_end": 400,
  "registry_ids": [
    "V.P168"
  ],
  "related_registry_items": [
    {
      "id": "V.P168",
      "title": "Selectivity: Only A ≥ 7 Suppressed",
      "url": "/registry/object/V.P168/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L388-L400",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L388-L400",
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
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L388-L400)
- Source range: L388-L400
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P168` — Selectivity: Only A ≥ 7 Suppressed

## Immediate Comment / Docstring

```lean
/-- [V.P168] Only A ≥ 7 nuclei are suppressed.
    A ≤ 4 fit the macrocell; A = 5,6 don't appear in BBN. -/
```

## Source Excerpt

```lean
theorem selectivity_threshold :
    -- All A ≤ 4 BBN nuclei have mass ≤ macrocell stride + 1
    BBNNucleus.massNumber .neutron ≤ 4 ∧
    BBNNucleus.massNumber .proton ≤ 4 ∧
    BBNNucleus.massNumber .deuterium ≤ 4 ∧
    BBNNucleus.massNumber .helium3 ≤ 4 ∧
    BBNNucleus.massNumber .tritium ≤ 4 ∧
    BBNNucleus.massNumber .helium4 ≤ 4 ∧
    -- A = 7 nuclei exceed macrocell
    BBNNucleus.massNumber .lithium7 > 4 ∧
    BBNNucleus.massNumber .beryllium7 > 4 :=
  ⟨by native_decide, by native_decide, by native_decide, by native_decide,
   by native_decide, by native_decide, by native_decide, by native_decide⟩
```
