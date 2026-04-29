---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_convergence",
  "permalink": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/primorial-convergence/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.CosmicLife.CrossLimit`.",
  "declaration_id": "TauLib.BookVI.CosmicLife.CrossLimit::primorial_convergence",
  "declaration_slug": "primorial-convergence",
  "kind": "theorem",
  "name": "primorial_convergence",
  "module_name": "TauLib.BookVI.CosmicLife.CrossLimit",
  "module_url": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/",
  "source_line_start": 102,
  "source_line_end": 106,
  "registry_ids": [
    "VI.L11"
  ],
  "related_registry_items": [
    {
      "id": "VI.L11",
      "title": "Primorial Ladder Convergence",
      "url": "/registry/object/VI.L11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L102-L106",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.CosmicLife.CrossLimit",
        "url": "/verify/taulib/docs/book-vi-cosmic-life-cross-limit/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L102-L106",
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

- Module: [TauLib.BookVI.CosmicLife.CrossLimit](/verify/taulib/docs/book-vi-cosmic-life-cross-limit/)
- Source path: [`TauLib/BookVI/CosmicLife/CrossLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/CosmicLife/CrossLimit.lean#L102-L106)
- Source range: L102-L106
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VI.L11` — Primorial Ladder Convergence

## Immediate Comment / Docstring

```lean
/-- [VI.L11] Primorial ladder converges superexponentially to ι_τ.
    Error bound: |c_k/P_k - ι_τ| ≤ 1/(2·p_{k+1}).
    Coherence: c_{k+1} ≡ c_k (mod P_k) for all k. -/
```

## Source Excerpt

```lean
theorem primorial_convergence :
    lift_omega.superexponential = true ∧
    lift_omega.converges_to_iota = true ∧
    lift_omega.iota_irrational = true :=
  ⟨rfl, rfl, rfl⟩
```
