---
{
  "projection_kind": "taulib_declaration",
  "title": "disagree_depth",
  "permalink": "/verify/taulib/docs/book-ii-domains-ultrametric/disagree-depth/",
  "summary_short": "`def` declaration in `TauLib.BookII.Domains.Ultrametric`.",
  "declaration_id": "TauLib.BookII.Domains.Ultrametric::disagree_depth",
  "declaration_slug": "disagree-depth",
  "kind": "def",
  "name": "disagree_depth",
  "module_name": "TauLib.BookII.Domains.Ultrametric",
  "module_url": "/verify/taulib/docs/book-ii-domains-ultrametric/",
  "source_line_start": 38,
  "source_line_end": 46,
  "registry_ids": [
    "II.D12"
  ],
  "related_registry_items": [
    {
      "id": "II.D12",
      "title": "First Disagreement Depth",
      "url": "/registry/object/II.D12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L38-L46",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L38-L46",
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
- Source path: [`TauLib/BookII/Domains/Ultrametric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Ultrametric.lean#L38-L46)
- Source range: L38-L46
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D12` — First Disagreement Depth

## Immediate Comment / Docstring

```lean
/-- [II.D12] First disagreement depth δ(x, y).
    Returns max { k : π_k(x) = π_k(y) } for k ≤ bound.
    If they agree for all k ≤ bound, returns bound + 1 (∞ proxy).
    Stage 0 always agrees (primorial 0 = 1), so δ ≥ 0. -/
```

## Source Excerpt

```lean
def disagree_depth (x y bound : TauIdx) : TauIdx :=
  go 0 (bound + 2)
where
  go (k fuel : Nat) : TauIdx :=
    if fuel = 0 then k
    else if k > bound then bound + 1
    else if reduce x (k + 1) ≠ reduce y (k + 1) then k
    else go (k + 1) (fuel - 1)
  termination_by fuel
```
