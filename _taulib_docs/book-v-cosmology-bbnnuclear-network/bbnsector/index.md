---
{
  "projection_kind": "taulib_declaration",
  "title": "BBNSector",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbnsector/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::BBNSector",
  "declaration_slug": "bbnsector",
  "kind": "inductive",
  "name": "BBNSector",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 165,
  "source_line_end": 169,
  "registry_ids": [
    "V.D304"
  ],
  "related_registry_items": [
    {
      "id": "V.D304",
      "title": "Sector Assignment",
      "url": "/registry/object/V.D304/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L165-L169",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L165-L169",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
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
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L165-L169)
- Source range: L165-L169
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D304` — Sector Assignment

## Immediate Comment / Docstring

```lean
/-- [V.D304] τ-sector assignment for BBN reactions. -/
```

## Source Excerpt

```lean
inductive BBNSector where
  | A  -- Weak sector (κ(A;1) = ι_τ)
  | B  -- EM sector (κ(B;2) = ι_τ²)
  | C  -- Strong sector (κ(C;3) = ι_τ³/(1−ι_τ))
  deriving Repr, DecidableEq, BEq
```
