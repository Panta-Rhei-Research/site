---
{
  "projection_kind": "taulib_declaration",
  "title": "BBNNucleus",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbnnucleus/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::BBNNucleus",
  "declaration_slug": "bbnnucleus",
  "kind": "inductive",
  "name": "BBNNucleus",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 105,
  "source_line_end": 114,
  "registry_ids": [
    "V.D302"
  ],
  "related_registry_items": [
    {
      "id": "V.D302",
      "title": "BBN Network Light Elements",
      "url": "/registry/object/V.D302/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L105-L114",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L105-L114",
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
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L105-L114)
- Source range: L105-L114
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D302` — BBN Network Light Elements

## Immediate Comment / Docstring

```lean
/-- [V.D302] The 8 light nuclei in the BBN network. -/
```

## Source Excerpt

```lean
inductive BBNNucleus where
  | neutron    -- n (A=1)
  | proton     -- p (A=1)
  | deuterium  -- D (A=2)
  | helium3    -- ³He (A=3)
  | tritium    -- T (A=3)
  | helium4    -- ⁴He (A=4)
  | lithium7   -- ⁷Li (A=7)
  | beryllium7 -- ⁷Be (A=7)
  deriving Repr, DecidableEq, BEq
```
