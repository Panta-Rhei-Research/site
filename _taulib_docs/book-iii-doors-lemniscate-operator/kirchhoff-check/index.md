---
{
  "projection_kind": "taulib_declaration",
  "title": "kirchhoff_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/kirchhoff-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.LemniscateOperator`.",
  "declaration_id": "TauLib.BookIII.Doors.LemniscateOperator::kirchhoff_check",
  "declaration_slug": "kirchhoff-check",
  "kind": "def",
  "name": "kirchhoff_check",
  "module_name": "TauLib.BookIII.Doors.LemniscateOperator",
  "module_url": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/",
  "source_line_start": 47,
  "source_line_end": 58,
  "registry_ids": [
    "III.D28"
  ],
  "related_registry_items": [
    {
      "id": "III.D28",
      "title": "Lemniscate Operator H_L",
      "url": "/registry/object/III.D28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L47-L58",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L47-L58",
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
- Source path: [`TauLib/BookIII/Doors/LemniscateOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L47-L58)
- Source range: L47-L58
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D28` — Lemniscate Operator H_L

## Immediate Comment / Docstring

```lean
/-- [III.D28] Kirchhoff condition: at the crossing point, eigenvalues
    of the full lemniscate operator equal the expected n² values. -/
```

## Source Excerpt

```lean
def kirchhoff_check (bound : TauIdx) : Bool :=
  go 0 (bound + 1)
where
  go (n fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > bound then true
    else
      -- Kirchhoff: eigenvalue gaps follow odd-number pattern
      -- λ(n+1) - λ(n) = 2n + 1 (exercises (n+1)² - n² identity)
      let gap := lemniscate_eigenvalue (n + 1) - lemniscate_eigenvalue n
      gap == 2 * n + 1 && go (n + 1) (fuel - 1)
  termination_by fuel
```
