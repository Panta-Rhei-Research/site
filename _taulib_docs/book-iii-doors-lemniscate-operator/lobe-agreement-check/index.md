---
{
  "projection_kind": "taulib_declaration",
  "title": "lobe_agreement_check",
  "permalink": "/corpus/taulib/docs/book-iii-doors-lemniscate-operator/lobe-agreement-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.LemniscateOperator`.",
  "declaration_id": "TauLib.BookIII.Doors.LemniscateOperator::lobe_agreement_check",
  "declaration_slug": "lobe-agreement-check",
  "kind": "def",
  "name": "lobe_agreement_check",
  "module_name": "TauLib.BookIII.Doors.LemniscateOperator",
  "module_url": "/corpus/taulib/docs/book-iii-doors-lemniscate-operator/",
  "source_line_start": 62,
  "source_line_end": 75,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L62-L75",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.LemniscateOperator",
        "url": "/corpus/taulib/docs/book-iii-doors-lemniscate-operator/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L62-L75",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIII.Doors.LemniscateOperator](/corpus/taulib/docs/book-iii-doors-lemniscate-operator/)
- Source path: [`TauLib/BookIII/Doors/LemniscateOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L62-L75)
- Source range: L62-L75
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.D28` — Lemniscate Operator H_L

## Immediate Comment / Docstring

```lean
/-- [III.D28] B-lobe and C-lobe eigenvalue agreement: the two lobes
    of L produce the same eigenvalue spectrum (K5 diagonal discipline). -/
```

## Source Excerpt

```lean
def lobe_agreement_check (bound : TauIdx) : Bool :=
  go 0 (bound + 1)
where
  go (n fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > bound then true
    else
      -- B-lobe: eigenvalue at mode n (direct formula n²)
      let b_lambda := lemniscate_eigenvalue n
      -- C-lobe: eigenvalue via independent path: n(n+1) - n = n²
      -- (exercises Nat.mul and Nat.sub — distinct computation from n*n)
      let c_lambda := n * (n + 1) - n
      b_lambda == c_lambda && go (n + 1) (fuel - 1)
  termination_by fuel
```
