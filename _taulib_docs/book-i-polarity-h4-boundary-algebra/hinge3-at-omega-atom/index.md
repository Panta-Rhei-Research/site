---
{
  "projection_kind": "taulib_declaration",
  "title": "hinge3_at_omega_atom",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/hinge3-at-omega-atom/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H4BoundaryAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.H4BoundaryAlgebra::hinge3_at_omega_atom",
  "declaration_slug": "hinge3-at-omega-atom",
  "kind": "theorem",
  "name": "hinge3_at_omega_atom",
  "module_name": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/",
  "source_line_start": 314,
  "source_line_end": 319,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L314-L319",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
        "url": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L314-L319",
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

- Module: [TauLib.BookI.Polarity.H4BoundaryAlgebra](/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/)
- Source path: [`TauLib/BookI/Polarity/H4BoundaryAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L314-L319)
- Source range: L314-L319
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem `main-hinge-integration` — Hinge 3 contribution
    in D**.

    Records the H3 master constant ι_τ's defining identity in
    D's algebraic structure: ι_τ · (π_τ + e_τ) ≡ 2_τ at Cauchy
    equivalence.  This is Wave 4's capstone seen as the boundary-
    algebra crossing-mediator identity. -/
```

## Source Excerpt

```lean
theorem hinge3_at_omega_atom :
    Tau.Boundary.TauReal.equiv
      (Tau.Boundary.TauReal.iota_tau.mul
        (Tau.Boundary.TauReal.pi.add Tau.Boundary.TauReal.e))
      Tau.Boundary.TauReal.two :=
  iota_tau_at_boundary
```
