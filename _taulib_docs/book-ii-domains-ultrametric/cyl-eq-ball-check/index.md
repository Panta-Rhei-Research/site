---
{
  "projection_kind": "taulib_declaration",
  "title": "cyl_eq_ball_check",
  "permalink": "/verify/taulib/docs/book-ii-domains-ultrametric/cyl-eq-ball-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Domains.Ultrametric`.",
  "declaration_id": "TauLib.BookII.Domains.Ultrametric::cyl_eq_ball_check",
  "declaration_slug": "cyl-eq-ball-check",
  "kind": "def",
  "name": "cyl_eq_ball_check",
  "module_name": "TauLib.BookII.Domains.Ultrametric",
  "module_url": "/verify/taulib/docs/book-ii-domains-ultrametric/",
  "source_line_start": 113,
  "source_line_end": 123,
  "registry_ids": [
    "II.P04"
  ],
  "related_registry_items": [
    {
      "id": "II.P04",
      "title": "Cylinders Are Balls",
      "url": "/registry/object/II.P04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L113-L123",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Domains.Ultrametric",
        "url": "/verify/taulib/docs/book-ii-domains-ultrametric/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L113-L123",
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

- Module: [TauLib.BookII.Domains.Ultrametric](/verify/taulib/docs/book-ii-domains-ultrametric/)
- Source path: [`TauLib/BookII/Domains/Ultrametric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L113-L123)
- Source range: L113-L123
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P04` — Cylinders Are Balls

## Immediate Comment / Docstring

```lean
/-- [II.P04] C_k(x) = B(x, 2^{-k}) = { y : δ(x,y) ≥ k }.
    Cylinder membership and ultrametric ball membership coincide. -/
```

## Source Excerpt

```lean
def cyl_eq_ball_check (k center bound db : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if y > bound then true
    else
      let in_cyl := cylinder_mem k center y
      let in_ball := disagree_depth center y db ≥ k
      (in_cyl == in_ball) && go (y + 1) (fuel - 1)
  termination_by fuel
```
