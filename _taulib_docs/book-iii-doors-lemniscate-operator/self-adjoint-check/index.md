---
{
  "projection_kind": "taulib_declaration",
  "title": "self_adjoint_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/self-adjoint-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.LemniscateOperator`.",
  "declaration_id": "TauLib.BookIII.Doors.LemniscateOperator::self_adjoint_check",
  "declaration_slug": "self-adjoint-check",
  "kind": "def",
  "name": "self_adjoint_check",
  "module_name": "TauLib.BookIII.Doors.LemniscateOperator",
  "module_url": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/",
  "source_line_start": 83,
  "source_line_end": 95,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L83-L95",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L83-L95",
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
- Source path: [`TauLib/BookIII/Doors/LemniscateOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L83-L95)
- Source range: L83-L95
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T17` — Self-Adjointness of H_L

## Immediate Comment / Docstring

```lean
/-- [III.T17] Self-adjointness check: eigenvalues are real and strictly
    ordered. In the finite τ-model, all eigenvalues are natural numbers. -/
```

## Source Excerpt

```lean
def self_adjoint_check (bound : TauIdx) : Bool :=
  go 0 (bound + 1)
where
  go (n fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > bound then true
    else
      -- Strict ordering: λ_{n+1} > λ_n for n > 0
      let ordered := if n > 0 then
        lemniscate_eigenvalue (n + 1) > lemniscate_eigenvalue n
      else true
      ordered && go (n + 1) (fuel - 1)
  termination_by fuel
```
