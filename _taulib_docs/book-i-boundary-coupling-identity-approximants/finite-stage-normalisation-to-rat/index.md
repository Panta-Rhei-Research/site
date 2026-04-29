---
{
  "projection_kind": "taulib_declaration",
  "title": "finiteStageNormalisation_toRat",
  "permalink": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/finite-stage-normalisation-to-rat/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.CouplingIdentityApproximants`.",
  "declaration_id": "TauLib.BookI.Boundary.CouplingIdentityApproximants::finiteStageNormalisation_toRat",
  "declaration_slug": "finite-stage-normalisation-to-rat",
  "kind": "theorem",
  "name": "finiteStageNormalisation_toRat",
  "module_name": "TauLib.BookI.Boundary.CouplingIdentityApproximants",
  "module_url": "/verify/taulib/docs/book-i-boundary-coupling-identity-approximants/",
  "source_line_start": 205,
  "source_line_end": 210,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L205-L210",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L205-L210",
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
- Source path: [`TauLib/BookI/Boundary/CouplingIdentityApproximants.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/CouplingIdentityApproximants.lean#L205-L210)
- Source range: L205-L210
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The finite-stage normalisation identity at toRat level**
    (paper Lemma 6.2 Equation (6.2-1), structural form).

    At every depth `n`:
      `iota^(n) · (pi^(n) + e^(n)) .toRat = 2 + ε_n.toRat`

    Expressed at toRat level for clean Rat-arithmetic handling
    (TauRat struct-level equality would require full ring-axiom
    framework; the toRat projection is sufficient for the
    normalisation-identity content). -/
```

## Source Excerpt

```lean
theorem finiteStageNormalisation_toRat (n : Nat) :
    ((iotaApproxAt n).mul ((piApproxAt n).add (eApproxAt n))).toRat
      = 2 + (finiteStageEpsilon n).toRat := by
  unfold finiteStageEpsilon
  rw [toRat_sub, twoApproxAt_toRat_eq_two]
  ring
```
