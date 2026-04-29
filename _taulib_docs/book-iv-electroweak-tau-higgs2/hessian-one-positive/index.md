---
{
  "projection_kind": "taulib_declaration",
  "title": "hessian_one_positive",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/hessian-one-positive/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::hessian_one_positive",
  "declaration_slug": "hessian-one-positive",
  "kind": "theorem",
  "name": "hessian_one_positive",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 229,
  "source_line_end": 233,
  "registry_ids": [
    "IV.P74"
  ],
  "related_registry_items": [
    {
      "id": "IV.P74",
      "title": "Finite-Stage Hessian Properties",
      "url": "/registry/object/IV.P74/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L229-L233",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.TauHiggs2",
        "url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L229-L233",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L229-L233)
- Source range: L229-L233
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P74` — Finite-Stage Hessian Properties

## Immediate Comment / Docstring

```lean
/-- [IV.P74] The Hessian has exactly one positive eigenvalue.
    This structural fact means there is exactly ONE physical scalar
    surviving after Goldstone absorption. -/
```

## Source Excerpt

```lean
theorem hessian_one_positive :
    coherence_hessian.positive_eigenvalues = 1 ∧
    coherence_hessian.zero_eigenvalues = 3 ∧
    coherence_hessian.negative_eigenvalues = 0 := by
  exact ⟨rfl, rfl, rfl⟩
```
