---
{
  "projection_kind": "taulib_declaration",
  "title": "OnticEntropyMonotonicity",
  "permalink": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/ontic-entropy-monotonicity/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.NoShrinkExtended`.",
  "declaration_id": "TauLib.BookV.Cosmology.NoShrinkExtended::OnticEntropyMonotonicity",
  "declaration_slug": "ontic-entropy-monotonicity",
  "kind": "structure",
  "name": "OnticEntropyMonotonicity",
  "module_name": "TauLib.BookV.Cosmology.NoShrinkExtended",
  "module_url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/",
  "source_line_start": 286,
  "source_line_end": 292,
  "registry_ids": [
    "V.T273"
  ],
  "related_registry_items": [
    {
      "id": "V.T273",
      "title": "Ontic Entropy Monotonicity for Mature BH",
      "url": "/registry/object/V.T273/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L286-L292",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.NoShrinkExtended",
        "url": "/verify/taulib/docs/book-v-cosmology-no-shrink-extended/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L286-L292",
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

- Module: [TauLib.BookV.Cosmology.NoShrinkExtended](/verify/taulib/docs/book-v-cosmology-no-shrink-extended/)
- Source path: [`TauLib/BookV/Cosmology/NoShrinkExtended.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/NoShrinkExtended.lean#L286-L292)
- Source range: L286-L292
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.T273` — Ontic Entropy Monotonicity for Mature BH

## Immediate Comment / Docstring

```lean
/-- [V.T273] Ontic entropy monotonicity for mature BH.
    S_vN(ρ_ontic(n+1)) ≤ S_vN(ρ_ontic(n)) for all n ≥ n_mature.
    The ontic state becomes purer, not less ordered.
    Scope: τ-effective. -/
```

## Source Excerpt

```lean
structure OnticEntropyMonotonicity where
  /-- Maturity depth. -/
  maturity_depth : Nat
  /-- Entropy values (in units of k_B, indexed by orbit step beyond maturity). -/
  entropy_at : Nat → Nat
  /-- Monotonically non-increasing. -/
  mono : ∀ n, entropy_at (n + 1) ≤ entropy_at n
```
