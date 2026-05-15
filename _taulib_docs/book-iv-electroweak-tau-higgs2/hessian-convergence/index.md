---
{
  "projection_kind": "taulib_declaration",
  "title": "HessianConvergence",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/hessian-convergence/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::HessianConvergence",
  "declaration_slug": "hessian-convergence",
  "kind": "structure",
  "name": "HessianConvergence",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 178,
  "source_line_end": 185,
  "registry_ids": [
    "IV.L07"
  ],
  "related_registry_items": [
    {
      "id": "IV.L07",
      "title": "Discrete Hessian Spectrum",
      "url": "/registry/object/IV.L07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L178-L185",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L178-L185",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/corpus/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L178-L185)
- Source range: L178-L185
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `IV.L07` — Discrete Hessian Spectrum

## Immediate Comment / Docstring

```lean
/-- [IV.L07] The positive eigenvalue of the Hessian converges as the
    tower level n → ∞. The limit is the physical Higgs mass squared.

    At each finite level n, the eigenvalue is a rational function of ι_τ.
    The convergence is exponentially fast in n, so level-1 already
    gives a good approximation. -/
```

## Source Excerpt

```lean
structure HessianConvergence where
  /-- Convergence is exponentially fast. -/
  exponential_rate : Bool := true
  /-- Level 1 already approximates well. -/
  level1_good : Bool := true
  /-- Limit exists. -/
  limit_exists : Bool := true
  deriving Repr
```
