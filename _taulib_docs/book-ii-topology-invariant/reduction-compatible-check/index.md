---
{
  "projection_kind": "taulib_declaration",
  "title": "reduction_compatible_check",
  "permalink": "/verify/taulib/docs/book-ii-topology-invariant/reduction-compatible-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.Invariant`.",
  "declaration_id": "TauLib.BookII.Topology.Invariant::reduction_compatible_check",
  "declaration_slug": "reduction-compatible-check",
  "kind": "def",
  "name": "reduction_compatible_check",
  "module_name": "TauLib.BookII.Topology.Invariant",
  "module_url": "/verify/taulib/docs/book-ii-topology-invariant/",
  "source_line_start": 81,
  "source_line_end": 92,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/Invariant.lean#L81-L92",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/Invariant.lean#L81-L92",
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
- Source path: [`TauLib/BookII/Topology/Invariant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/Invariant.lean#L81-L92)
- Source range: L81-L92
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The reduction maps form a compatible family:
    reduce(reduce(x, l), k) = reduce(x, k) for k ≤ l.
    This is the defining property of an inverse system. -/
```

## Source Excerpt

```lean
def reduction_compatible_check (bound : TauIdx) : Bool :=
  go 1 1 2 ((bound + 1) * 5 * 5)
where
  go (k l x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > 4 then true
    else if l > 4 then go (k + 1) (k + 2) 2 (fuel - 1)
    else if x > bound then go k (l + 1) 2 (fuel - 1)
    else
      let ok := k > l || reduce (reduce x l) k == reduce x k
      ok && go k l (x + 1) (fuel - 1)
  termination_by fuel
```
