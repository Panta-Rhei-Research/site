---
{
  "projection_kind": "taulib_declaration",
  "title": "nf_convergence",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/nf-convergence/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.NonlinearEinstein`.",
  "declaration_id": "TauLib.BookV.GravityField.NonlinearEinstein::nf_convergence",
  "declaration_slug": "nf-convergence",
  "kind": "theorem",
  "name": "nf_convergence",
  "module_name": "TauLib.BookV.GravityField.NonlinearEinstein",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/",
  "source_line_start": 358,
  "source_line_end": 361,
  "registry_ids": [
    "V.P15"
  ],
  "related_registry_items": [
    {
      "id": "V.P15",
      "title": "Convergence in all regimes",
      "url": "/registry/object/V.P15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L358-L361",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.NonlinearEinstein",
        "url": "/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L358-L361",
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

- Module: [TauLib.BookV.GravityField.NonlinearEinstein](/verify/taulib/docs/book-v-gravity-field-nonlinear-einstein/)
- Source path: [`TauLib/BookV/GravityField/NonlinearEinstein.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/NonlinearEinstein.lean#L358-L361)
- Source range: L358-L361
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P15` — Convergence in all regimes

## Immediate Comment / Docstring

```lean
/-- [V.P15] NF iteration convergence: each truncation-coherent step
    decreases the cocycle defect (cross-multiplied form).

    defect_after / denom_after ≤ defect_before / denom_before
    ⟺ defect_after · denom_before ≤ defect_before · denom_after -/
```

## Source Excerpt

```lean
theorem nf_convergence (s : TruncationCoherentStep) :
    s.defect_after.defect_numer * s.defect_before.defect_denom ≤
    s.defect_before.defect_numer * s.defect_after.defect_denom :=
  s.defect_decrease
```
