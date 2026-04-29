---
{
  "projection_kind": "taulib_declaration",
  "title": "DeuteriumBottleneck",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/deuterium-bottleneck/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::DeuteriumBottleneck",
  "declaration_slug": "deuterium-bottleneck",
  "kind": "structure",
  "name": "DeuteriumBottleneck",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 90,
  "source_line_end": 95,
  "registry_ids": [
    "V.D301"
  ],
  "related_registry_items": [
    {
      "id": "V.D301",
      "title": "Deuterium Bottleneck Temperature",
      "url": "/registry/object/V.D301/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L90-L95",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L90-L95",
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
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L90-L95)
- Source range: L90-L95
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D301` — Deuterium Bottleneck Temperature

## Immediate Comment / Docstring

```lean
/-- [V.D301] Deuterium bottleneck temperature T_D ≈ 0.07 MeV.
    Below this temperature, deuterium survives photo-dissociation
    and the nuclear chain proceeds. -/
```

## Source Excerpt

```lean
structure DeuteriumBottleneck where
  /-- Bottleneck temperature in units of 0.01 MeV. -/
  temp_001MeV : Nat := 7
  /-- Bottleneck lies within the nucleosynthetic window. -/
  within_nuc_window : Bool := true
  deriving Repr
```
