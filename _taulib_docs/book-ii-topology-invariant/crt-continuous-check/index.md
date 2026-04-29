---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_continuous_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-invariant/crt-continuous-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.Invariant`.",
  "declaration_id": "TauLib.BookII.Topology.Invariant::crt_continuous_check",
  "declaration_slug": "crt-continuous-check",
  "kind": "def",
  "name": "crt_continuous_check",
  "module_name": "TauLib.BookII.Topology.Invariant",
  "module_url": "/verify/taulib/docs/book-ii-topology-invariant/",
  "source_line_start": 40,
  "source_line_end": 58,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/Invariant.lean#L40-L58",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.Invariant",
        "url": "/verify/taulib/docs/book-ii-topology-invariant/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/Invariant.lean#L40-L58",
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

- Module: [TauLib.BookII.Topology.Invariant](/verify/taulib/docs/book-ii-topology-invariant/)
- Source path: [`TauLib/BookII/Topology/Invariant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/Invariant.lean#L40-L58)
- Source range: L40-L58
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CRT reduction maps preserve cylinder structure:
    if y ∈ C_k(x), then π_l(y) ∈ C_l(π_l(x)) for all l ≤ k.
    This is the cylinder-theoretic definition of continuity. -/
```

## Source Excerpt

```lean
def crt_continuous_check (k bound : TauIdx) : Bool :=
  go 2 2 ((bound + 1) * (bound + 1))
where
  /-- Check all lower stages preserve agreement. -/
  check_lower (x y k l fuel_l : Nat) : Bool :=
    if fuel_l = 0 then true
    else if l > k then true
    else cylinder_mem l x y && check_lower x y k (l + 1) (fuel_l - 1)
  termination_by fuel_l
  go (x y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 2 (fuel - 1)
    else
      -- If y ∈ C_k(x), then reduce(y, l) ∈ C_l(reduce(x, l)) for l ≤ k
      let ok := !cylinder_mem k x y ||
        check_lower x y k 1 (k + 1)
      ok && go x (y + 1) (fuel - 1)
  termination_by fuel
```
