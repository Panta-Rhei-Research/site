---
{
  "projection_kind": "taulib_declaration",
  "title": "ConvergenceClaimFloat",
  "permalink": "/verify/taulib/docs/book-i-boundary-iota/convergence-claim-float/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Iota`.",
  "declaration_id": "TauLib.BookI.Boundary.Iota::ConvergenceClaimFloat",
  "declaration_slug": "convergence-claim-float",
  "kind": "def",
  "name": "ConvergenceClaimFloat",
  "module_name": "TauLib.BookI.Boundary.Iota",
  "module_url": "/verify/taulib/docs/book-i-boundary-iota/",
  "source_line_start": 89,
  "source_line_end": 92,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L89-L92",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Iota",
        "url": "/verify/taulib/docs/book-i-boundary-iota/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L89-L92",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookI.Boundary.Iota](/verify/taulib/docs/book-i-boundary-iota/)
- Source path: [`TauLib/BookI/Boundary/Iota.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L89-L92)
- Source range: L89-L92
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The convergence claim: for all epsilon > 0, there exists N₀ such that
    for all n ≥ N₀, |bc_ratio(n, N) - iota_tau| < epsilon.
    This is an axiom stub — the proof requires analytic number theory
    (effective prime number theorem + polarity equidistribution)
    which is beyond the current mechanization scope. -/
```

## Source Excerpt

```lean
def ConvergenceClaimFloat (N : TauIdx) : Prop :=
  ∀ (eps : Float), eps > 0.0 →
    ∃ (n0 : Nat), ∀ (n : Nat), n ≥ n0 →
      Float.abs (bc_ratio_float n N - iota_tau_float) < eps
```
