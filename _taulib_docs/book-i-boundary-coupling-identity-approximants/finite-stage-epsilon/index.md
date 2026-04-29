---
{
  "projection_kind": "taulib_declaration",
  "title": "finiteStageEpsilon",
  "permalink": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/finite-stage-epsilon/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.CouplingIdentityApproximants`.",
  "declaration_id": "TauLib.BookI.Boundary.CouplingIdentityApproximants::finiteStageEpsilon",
  "declaration_slug": "finite-stage-epsilon",
  "kind": "def",
  "name": "finiteStageEpsilon",
  "module_name": "TauLib.BookI.Boundary.CouplingIdentityApproximants",
  "module_url": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/",
  "source_line_start": 191,
  "source_line_end": 193,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L191-L193",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L191-L193",
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

- Module: [TauLib.BookI.Boundary.CouplingIdentityApproximants](/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/)
- Source path: [`TauLib/BookI/Boundary/CouplingIdentityApproximants.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L191-L193)
- Source range: L191-L193
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §6.2 finite-stage correction `ε_n`**: the depth-`n`
    deviation between the finite-stage product and the dyadic
    constant.

    Defined explicitly as
    `ε_n := iota^(n) · (π^(n) + e^(n)) − 2`.

    Paper Lemma 6.2 asserts `ε_n = 0` at primorial depths and
    `ε_n → 0` as `n → ∞`.  At the operational Lean level, `ε_n`
    is a computable TauRat that can be `#eval`'d at specific depths. -/
```

## Source Excerpt

```lean
def finiteStageEpsilon (n : Nat) : TauRat :=
  ((iotaApproxAt n).mul ((piApproxAt n).add (eApproxAt n))).sub
    (twoApproxAt n)
```
