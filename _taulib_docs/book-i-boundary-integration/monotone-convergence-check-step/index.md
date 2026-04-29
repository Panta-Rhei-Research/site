---
{
  "projection_kind": "taulib_declaration",
  "title": "monotone_convergence_check_step",
  "permalink": "/verify/taulib/docs/book-i-boundary-integration/monotone-convergence-check-step/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Integration`.",
  "declaration_id": "TauLib.BookI.Boundary.Integration::monotone_convergence_check_step",
  "declaration_slug": "monotone-convergence-check-step",
  "kind": "def",
  "name": "monotone_convergence_check_step",
  "module_name": "TauLib.BookI.Boundary.Integration",
  "module_url": "/verify/taulib/docs/book-i-boundary-integration/",
  "source_line_start": 85,
  "source_line_end": 91,
  "registry_ids": [
    "I.P45"
  ],
  "related_registry_items": [
    {
      "id": "I.P45",
      "title": "Monotone Convergence",
      "url": "/registry/object/I.P45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L85-L91",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Integration",
        "url": "/verify/taulib/docs/book-i-boundary-integration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L85-L91",
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

- Module: [TauLib.BookI.Boundary.Integration](/verify/taulib/docs/book-i-boundary-integration/)
- Source path: [`TauLib/BookI/Boundary/Integration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Integration.lean#L85-L91)
- Source range: L85-L91
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.P45` — Monotone Convergence

## Immediate Comment / Docstring

```lean
/-- [I.P45] Check that integrals increase from stage k to stage k+1
    for a given function family. -/
```

## Source Excerpt

```lean
def monotone_convergence_check_step (f : Nat → Nat → Int)
    (k : Nat) : Bool :=
  let ik := tau_integral (f k) k
  let ik1 := tau_integral (f (k + 1)) (k + 1)
  -- Compare ik.num / ik.den ≤ ik1.num / ik1.den
  -- i.e., ik.num * ik1.den ≤ ik1.num * ik.den
  ik.numerator * ik1.denominator ≤ ik1.numerator * ik.denominator
```
