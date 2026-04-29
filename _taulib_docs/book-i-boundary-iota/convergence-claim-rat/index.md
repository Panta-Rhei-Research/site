---
{
  "projection_kind": "taulib_declaration",
  "title": "ConvergenceClaimRat",
  "permalink": "/verify/taulib/docs/book-i-boundary-iota/convergence-claim-rat/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Iota`.",
  "declaration_id": "TauLib.BookI.Boundary.Iota::ConvergenceClaimRat",
  "declaration_slug": "convergence-claim-rat",
  "kind": "def",
  "name": "ConvergenceClaimRat",
  "module_name": "TauLib.BookI.Boundary.Iota",
  "module_url": "/verify/taulib/docs/book-i-boundary-iota/",
  "source_line_start": 98,
  "source_line_end": 106,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L98-L106",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L98-L106",
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
- Source path: [`TauLib/BookI/Boundary/Iota.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Iota.lean#L98-L106)
- Source range: L98-L106
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Convergence claim in rational form: for all k (precision level),
    there exists n0 such that for n ≥ n0,
    |count_b(n,N) * denom - numer * count_c(n,N)| < count_c(n,N) * (denom / 10^k).
    This is the pure Nat formulation avoiding Float. -/
```

## Source Excerpt

```lean
def ConvergenceClaimRat (N : TauIdx) (k : Nat) : Prop :=
  ∃ (n0 : Nat), ∀ (n : Nat), n ≥ n0 →
    let (b, c) := bc_ratio_pair n N
    c > 0 ∧
    -- |b * denom - numer * c| < c * (denom / 10^k)
    -- i.e., the ratio b/c is within denom/10^k of numer/denom
    (if b * iota_tau_denom ≥ iota_tau_numer * c
     then b * iota_tau_denom - iota_tau_numer * c < c * (iota_tau_denom / 10 ^ k)
     else iota_tau_numer * c - b * iota_tau_denom < c * (iota_tau_denom / 10 ^ k))
```
