---
{
  "projection_kind": "taulib_declaration",
  "title": "iota_tau_at_boundary",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/iota-tau-at-boundary/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H4BoundaryAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.H4BoundaryAlgebra::iota_tau_at_boundary",
  "declaration_slug": "iota-tau-at-boundary",
  "kind": "theorem",
  "name": "iota_tau_at_boundary",
  "module_name": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/",
  "source_line_start": 287,
  "source_line_end": 289,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L287-L289",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L287-L289",
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
- Source path: [`TauLib/BookI/Polarity/H4BoundaryAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L287-L289)
- Source range: L287-L289
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The ω-generator role of ι_τ** (paper Theorem `main-iota`):
    `ι_τ` is the unique non-idempotent σ-fixed scalar in D, mediating
    the two polarised lobes (Higgs sector).

    At the TauReal level, ι_τ ≈ 0.341304... is the operational
    crossing mediator from Wave 4.  Its boundary-algebra role is
    captured by the Wave 4 capstone `iota_tau_mul_pi_plus_e_eq_two`,
    which in the boundary-algebra language reads:
    `ι_τ · (π_τ + e_τ) ≡ 2_τ` at the additive trace level. -/
```

## Source Excerpt

```lean
theorem iota_tau_at_boundary :
    TauReal.equiv (TauReal.iota_tau.mul (TauReal.pi.add TauReal.e)) TauReal.two :=
  TauReal.iota_tau_mul_pi_plus_e_eq_two
```
