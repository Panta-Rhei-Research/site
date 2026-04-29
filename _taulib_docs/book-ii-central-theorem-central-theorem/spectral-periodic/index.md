---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_periodic",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/spectral-periodic/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::spectral_periodic",
  "declaration_slug": "spectral-periodic",
  "kind": "theorem",
  "name": "spectral_periodic",
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 407,
  "source_line_end": 409,
  "registry_ids": [
    "II.D60"
  ],
  "related_registry_items": [
    {
      "id": "II.D60",
      "title": "Spectral Algebra",
      "url": "/registry/object/II.D60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L407-L409",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.CentralTheorem",
        "url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L407-L409",
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

- Module: [TauLib.BookII.CentralTheorem.CentralTheorem](/verify/taulib/docs/book-ii-central-theorem-central-theorem/)
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L407-L409)
- Source range: L407-L409
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D60` — Spectral Algebra

## Immediate Comment / Docstring

```lean
/-- [II.D60] Spectral algebra periodicity: evaluation is periodic in x
    with period P_k. This follows from reduce(x + P_k, k) = reduce(x, k). -/
```

## Source Excerpt

```lean
theorem spectral_periodic (sa : SpectralAlgebraElement) (x k : TauIdx) :
    sa.eval (x + primorial k) k = sa.eval x k := by
  simp [SpectralAlgebraElement.eval, reduce, Nat.add_mod_right]
```
