---
{
  "projection_kind": "taulib_declaration",
  "title": "CoherenceHessian",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/coherence-hessian/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.TauHiggs2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.TauHiggs2::CoherenceHessian",
  "declaration_slug": "coherence-hessian",
  "kind": "structure",
  "name": "CoherenceHessian",
  "module_name": "TauLib.BookIV.Electroweak.TauHiggs2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-tau-higgs2/",
  "source_line_start": 57,
  "source_line_end": 68,
  "registry_ids": [
    "IV.D140"
  ],
  "related_registry_items": [
    {
      "id": "IV.D140",
      "title": "Vacuum Hessian at Crossing Point",
      "url": "/registry/object/IV.D140/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L57-L68",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L57-L68",
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

- Module: [TauLib.BookIV.Electroweak.TauHiggs2](/verify/taulib/docs/book-iv-electroweak-tau-higgs2/)
- Source path: [`TauLib/BookIV/Electroweak/TauHiggs2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/TauHiggs2.lean#L57-L68)
- Source range: L57-L68
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D140` — Vacuum Hessian at Crossing Point

## Immediate Comment / Docstring

```lean
/-- [IV.D140] The Hessian (second variation matrix) of V_n at the
    physical vacuum. It is a 4×4 real symmetric matrix with:
    - 1 positive eigenvalue (radial = Higgs mass²)
    - 3 zero eigenvalues (angular = Goldstone modes)

    The positive eigenvalue converges as n → ∞ in the tower,
    giving the physical Higgs mass. -/
```

## Source Excerpt

```lean
structure CoherenceHessian where
  /-- Dimension of the Hessian matrix. -/
  dim : Nat := 4
  /-- Number of positive eigenvalues. -/
  positive_eigenvalues : Nat := 1
  /-- Number of zero eigenvalues (Goldstone directions). -/
  zero_eigenvalues : Nat := 3
  /-- Number of negative eigenvalues (stability). -/
  negative_eigenvalues : Nat := 0
  /-- Eigenvalue count check. -/
  eigenvalue_check : positive_eigenvalues + zero_eigenvalues + negative_eigenvalues = dim := by omega
  deriving Repr
```
