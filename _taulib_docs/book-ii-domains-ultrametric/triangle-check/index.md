---
{
  "projection_kind": "taulib_declaration",
  "title": "triangle_check",
  "permalink": "/verify/taulib/docs/book-ii-domains-ultrametric/triangle-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Domains.Ultrametric`.",
  "declaration_id": "TauLib.BookII.Domains.Ultrametric::triangle_check",
  "declaration_slug": "triangle-check",
  "kind": "def",
  "name": "triangle_check",
  "module_name": "TauLib.BookII.Domains.Ultrametric",
  "module_url": "/verify/taulib/docs/book-ii-domains-ultrametric/",
  "source_line_start": 92,
  "source_line_end": 105,
  "registry_ids": [
    "II.T05"
  ],
  "related_registry_items": [
    {
      "id": "II.T05",
      "title": "Ultrametric Triangle Inequality",
      "url": "/registry/object/II.T05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L92-L105",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L92-L105",
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
- Source path: [`TauLib/BookII/Domains/Ultrametric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L92-L105)
- Source range: L92-L105
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T05` — Ultrametric Triangle Inequality

## Immediate Comment / Docstring

```lean
/-- [II.T05] Ultrametric triangle inequality:
    δ(x,z) ≥ min(δ(x,y), δ(y,z)) for all x, y, z ∈ [2, bound].
    Equivalent to d(x,z) ≤ max(d(x,y), d(y,z)).
    Uses a flat triple loop with single fuel counter. -/
```

## Source Excerpt

```lean
def triangle_check (bound db : TauIdx) : Bool :=
  go 2 2 2 ((bound + 1) * (bound + 1) * (bound + 1))
where
  go (x y z fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 2 2 (fuel - 1)
    else if z > bound then go x (y + 1) 2 (fuel - 1)
    else
      let dxz := disagree_depth x z db
      let dxy := disagree_depth x y db
      let dyz := disagree_depth y z db
      (dxz ≥ min dxy dyz) && go x y (z + 1) (fuel - 1)
  termination_by fuel
```
