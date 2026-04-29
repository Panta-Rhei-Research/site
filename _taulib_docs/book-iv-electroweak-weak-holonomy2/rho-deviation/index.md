---
{
  "projection_kind": "taulib_declaration",
  "title": "rho_deviation",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/rho-deviation/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.WeakHolonomy2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.WeakHolonomy2::rho_deviation",
  "declaration_slug": "rho-deviation",
  "kind": "theorem",
  "name": "rho_deviation",
  "module_name": "TauLib.BookIV.Electroweak.WeakHolonomy2",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/",
  "source_line_start": 179,
  "source_line_end": 182,
  "registry_ids": [
    "IV.P61"
  ],
  "related_registry_items": [
    {
      "id": "IV.P61",
      "title": "Measured Rho",
      "url": "/registry/object/IV.P61/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L179-L182",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.WeakHolonomy2",
        "url": "/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L179-L182",
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

- Module: [TauLib.BookIV.Electroweak.WeakHolonomy2](/verify/taulib/docs/book-iv-electroweak-weak-holonomy2/)
- Source path: [`TauLib/BookIV/Electroweak/WeakHolonomy2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/WeakHolonomy2.lean#L179-L182)
- Source range: L179-L182
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P61` — Measured Rho

## Immediate Comment / Docstring

```lean
/-- [IV.P61] Deviations of rho from 1 measure radiative corrections
    (loop effects). In the tau-framework, these correspond to
    higher-order boundary-character contributions. -/
```

## Source Excerpt

```lean
theorem rho_deviation :
    rho_exp.numer > rho_exp.denom ∧
    rho_exp.numer - rho_exp.denom < 100 := by
  simp [rho_exp]
```
