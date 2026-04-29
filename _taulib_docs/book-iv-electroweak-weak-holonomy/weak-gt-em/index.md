---
{
  "projection_kind": "taulib_declaration",
  "title": "weak_gt_em",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/weak-gt-em/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy::weak_gt_em",
  "declaration_slug": "weak-gt-em",
  "kind": "theorem",
  "name": "weak_gt_em",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/",
  "source_line_start": 288,
  "source_line_end": 291,
  "registry_ids": [
    "IV.P58"
  ],
  "related_registry_items": [
    {
      "id": "IV.P58",
      "title": "EM-Weak Coupling Hierarchy",
      "url": "/registry/object/IV.P58/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L288-L291",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L288-L291",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy](/verify/taulib/docs/book-iv-electroweak-weak-holonomy/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy.lean#L288-L291)
- Source range: L288-L291
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P58` — EM-Weak Coupling Hierarchy

## Immediate Comment / Docstring

```lean
/-- [IV.P58] The weak self-coupling exceeds the EM self-coupling:
    kappa(A;1) = iota_tau > iota_tau^2 = kappa(B;2).
    Since 0 < iota_tau < 1, iota > iota^2.
    Proven via the coupling formula definitions. -/
```

## Source Excerpt

```lean
theorem weak_gt_em :
    kappa_AA.numer * kappa_BB.denom > kappa_BB.numer * kappa_AA.denom := by
  simp [kappa_AA, kappa_BB, iota_sq_numer, iota_sq_denom,
        iota, iotaD, iota_tau_numer, iota_tau_denom]
```
