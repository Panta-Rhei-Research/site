---
{
  "projection_kind": "taulib_declaration",
  "title": "k5_diagonal_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/k5-diagonal-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.LemniscateOperator`.",
  "declaration_id": "TauLib.BookIII.Doors.LemniscateOperator::k5_diagonal_check",
  "declaration_slug": "k5-diagonal-check",
  "kind": "def",
  "name": "k5_diagonal_check",
  "module_name": "TauLib.BookIII.Doors.LemniscateOperator",
  "module_url": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/",
  "source_line_start": 100,
  "source_line_end": 113,
  "registry_ids": [
    "III.T17"
  ],
  "related_registry_items": [
    {
      "id": "III.T17",
      "title": "Self-Adjointness of H_L",
      "url": "/registry/object/III.T17/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L100-L113",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.LemniscateOperator",
        "url": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L100-L113",
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

- Module: [TauLib.BookIII.Doors.LemniscateOperator](/verify/taulib/docs/book-iii-doors-lemniscate-operator/)
- Source path: [`TauLib/BookIII/Doors/LemniscateOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L100-L113)
- Source range: L100-L113
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T17` — Self-Adjointness of H_L

## Immediate Comment / Docstring

```lean
/-- [III.T17] K5 diagonal discipline: the off-diagonal coupling at the
    crossing point vanishes. B-lobe and C-lobe eigenvalues are independent
    (no imaginary mixing terms). -/
```

## Source Excerpt

```lean
def k5_diagonal_check (bound : TauIdx) : Bool :=
  go 1 (bound + 1)
where
  go (n fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > bound then true
    else
      -- Diagonal: eigenvalue n for B-lobe = eigenvalue n for C-lobe
      let b_lambda := lemniscate_eigenvalue n
      let c_lambda := lemniscate_eigenvalue n
      -- No off-diagonal coupling: the difference is zero
      let no_mixing := b_lambda == c_lambda
      no_mixing && go (n + 1) (fuel - 1)
  termination_by fuel
```
