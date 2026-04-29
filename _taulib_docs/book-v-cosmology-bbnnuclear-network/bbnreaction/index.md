---
{
  "projection_kind": "taulib_declaration",
  "title": "BBNReaction",
  "permalink": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/bbnreaction/",
  "summary_short": "`inductive` declaration in `TauLib.BookV.Cosmology.BBNNuclearNetwork`.",
  "declaration_id": "TauLib.BookV.Cosmology.BBNNuclearNetwork::BBNReaction",
  "declaration_slug": "bbnreaction",
  "kind": "inductive",
  "name": "BBNReaction",
  "module_name": "TauLib.BookV.Cosmology.BBNNuclearNetwork",
  "module_url": "/verify/taulib/docs/book-v-cosmology-bbnnuclear-network/",
  "source_line_start": 137,
  "source_line_end": 150,
  "registry_ids": [
    "V.D303"
  ],
  "related_registry_items": [
    {
      "id": "V.D303",
      "title": "BBN Reaction Chain",
      "url": "/registry/object/V.D303/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L137-L150",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L137-L150",
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
- Source path: [`TauLib/BookV/Cosmology/BBNNuclearNetwork.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/BBNNuclearNetwork.lean#L137-L150)
- Source range: L137-L150
- Kind: `inductive`
- Formal status hint: `defined`

## Registry Links

- `V.D303` — BBN Reaction Chain

## Immediate Comment / Docstring

```lean
/-- [V.D303] The 12 dominant BBN reactions, indexed 1–12. -/
```

## Source Excerpt

```lean
inductive BBNReaction where
  | R1   -- n → p + e⁻ + ν̄_e (weak decay)
  | R2   -- p + n → D + γ (EM capture)
  | R3   -- D + p → ³He + γ (EM capture)
  | R4   -- D + D → ³He + n (strong)
  | R5   -- D + D → T + p (strong)
  | R6   -- T + D → ⁴He + n (strong)
  | R7   -- ³He + n → T + p (strong)
  | R8   -- ³He + D → ⁴He + p (strong)
  | R9   -- ³He + ⁴He → ⁷Be + γ (EM capture) — CRITICAL
  | R10  -- T + ⁴He → ⁷Li + γ (EM capture)
  | R11  -- ⁷Be + n → ⁷Li + p (strong)
  | R12  -- ⁷Li + p → 2 ⁴He (strong)
  deriving Repr, DecidableEq, BEq
```
