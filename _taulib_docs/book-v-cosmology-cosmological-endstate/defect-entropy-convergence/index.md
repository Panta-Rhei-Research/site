---
{
  "projection_kind": "taulib_declaration",
  "title": "DefectEntropyConvergence",
  "permalink": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/defect-entropy-convergence/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Cosmology.CosmologicalEndstate`.",
  "declaration_id": "TauLib.BookV.Cosmology.CosmologicalEndstate::DefectEntropyConvergence",
  "declaration_slug": "defect-entropy-convergence",
  "kind": "structure",
  "name": "DefectEntropyConvergence",
  "module_name": "TauLib.BookV.Cosmology.CosmologicalEndstate",
  "module_url": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/",
  "source_line_start": 71,
  "source_line_end": 82,
  "registry_ids": [
    "V.P102"
  ],
  "related_registry_items": [
    {
      "id": "V.P102",
      "title": "Defect entropy converges to zero",
      "url": "/registry/object/V.P102/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L71-L82",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.CosmologicalEndstate",
        "url": "/verify/taulib/docs/book-v-cosmology-cosmological-endstate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L71-L82",
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

- Module: [TauLib.BookV.Cosmology.CosmologicalEndstate](/verify/taulib/docs/book-v-cosmology-cosmological-endstate/)
- Source path: [`TauLib/BookV/Cosmology/CosmologicalEndstate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/CosmologicalEndstate.lean#L71-L82)
- Source range: L71-L82
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.P102` — Defect entropy converges to zero

## Immediate Comment / Docstring

```lean
/-- [V.P102] Defect entropy converges as n → ∞:
    lim S_def(n) = S_def^BH ≥ 0.

    The irreducible defect entropy comes from BH excisions.
    Outside excisions, S_def → 0 (vacuum absorbing pattern).

    The defect entropy at each tick is a decreasing sequence
    (modulo BH contributions), bounded below by zero. -/
```

## Source Excerpt

```lean
structure DefectEntropyConvergence where
  /-- Defect entropy at early tick (scaled). -/
  entropy_early : Nat
  /-- Defect entropy at late tick (scaled). -/
  entropy_late : Nat
  /-- Irreducible BH entropy (scaled). -/
  entropy_bh : Nat
  /-- Entropy decreases (modulo BH). -/
  decreasing : entropy_late ≤ entropy_early
  /-- Late entropy is at least BH contribution. -/
  lower_bound : entropy_late ≥ entropy_bh
  deriving Repr
```
