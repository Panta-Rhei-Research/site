---
{
  "projection_kind": "taulib_declaration",
  "title": "CompleteBBNTable",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/complete-bbntable/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::CompleteBBNTable",
  "declaration_slug": "complete-bbntable",
  "kind": "structure",
  "name": "CompleteBBNTable",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 408,
  "source_line_end": 421,
  "registry_ids": [
    "V.D307"
  ],
  "related_registry_items": [
    {
      "id": "V.D307",
      "title": "Complete BBN Abundance Table",
      "url": "/registry/object/V.D307/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L408-L421",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L408-L421",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L408-L421)
- Source range: L408-L421
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D307` — Complete BBN Abundance Table

## Immediate Comment / Docstring

```lean
/-- [V.D307] Complete BBN abundance table.
    All four species from single η_B with zero free parameters. -/
```

## Source Excerpt

```lean
structure CompleteBBNTable where
  /-- Number of species predicted. -/
  n_species : Nat := 4
  /-- Number of free parameters. -/
  n_free_params : Nat := 0
  /-- Y_p within range. -/
  yp_ok : Bool := true
  /-- D/H within range. -/
  dh_ok : Bool := true
  /-- ³He/H within range. -/
  he3_ok : Bool := true
  /-- ⁷Li/H within range. -/
  li7_ok : Bool := true
  deriving Repr
```
