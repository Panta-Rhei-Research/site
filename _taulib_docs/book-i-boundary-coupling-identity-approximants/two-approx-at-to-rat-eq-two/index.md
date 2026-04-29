---
{
  "projection_kind": "taulib_declaration",
  "title": "twoApproxAt_toRat_eq_two",
  "permalink": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/two-approx-at-to-rat-eq-two/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.CouplingIdentityApproximants`.",
  "declaration_id": "TauLib.BookI.Boundary.CouplingIdentityApproximants::twoApproxAt_toRat_eq_two",
  "declaration_slug": "two-approx-at-to-rat-eq-two",
  "kind": "theorem",
  "name": "twoApproxAt_toRat_eq_two",
  "module_name": "TauLib.BookI.Boundary.CouplingIdentityApproximants",
  "module_url": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/",
  "source_line_start": 150,
  "source_line_end": 152,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L150-L152",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.CouplingIdentityApproximants",
        "url": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L150-L152",
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

- Module: [TauLib.BookI.Boundary.CouplingIdentityApproximants](/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/)
- Source path: [`TauLib/BookI/Boundary/CouplingIdentityApproximants.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L150-L152)
- Source range: L150-L152
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §6.1 Equation (6.1-1) / `eq:two-n`**: `Ger2^(n) = 2`
    at every depth `n`.

    The dyadic refinement quotient is always `|B_{n+1}|/|B_n| = 2`
    by the paper's Definition of 2_τ; at the TauReal-level this
    corresponds to `TauReal.two` being the constant Cauchy sequence
    at `2`, whose `.approx n` evaluates to `2` at every `n` (via
    Wave 4's `TauReal.two_approx_toRat`). -/
```

## Source Excerpt

```lean
theorem twoApproxAt_toRat_eq_two (n : Nat) :
    (twoApproxAt n).toRat = 2 :=
  TauReal.two_approx_toRat n
```
