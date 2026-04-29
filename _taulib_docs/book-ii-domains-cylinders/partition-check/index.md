---
{
  "projection_kind": "taulib_declaration",
  "title": "partition_check",
  "permalink": "/verify/taulib/docs/book-ii-domains-cylinders/partition-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Domains.Cylinders`.",
  "declaration_id": "TauLib.BookII.Domains.Cylinders::partition_check",
  "declaration_slug": "partition-check",
  "kind": "def",
  "name": "partition_check",
  "module_name": "TauLib.BookII.Domains.Cylinders",
  "module_url": "/verify/taulib/docs/book-ii-domains-cylinders/",
  "source_line_start": 111,
  "source_line_end": 126,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L111-L126",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Domains.Cylinders",
        "url": "/verify/taulib/docs/book-ii-domains-cylinders/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L111-L126",
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

- Module: [TauLib.BookII.Domains.Cylinders](/verify/taulib/docs/book-ii-domains-cylinders/)
- Source path: [`TauLib/BookII/Domains/Cylinders.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L111-L126)
- Source range: L111-L126
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T04, clause 3] Partition: residue classes at stage k partition.
    Every y ∈ [0, M_k) satisfies y ∈ C_k(y). -/
```

## Source Excerpt

```lean
def partition_check (k : TauIdx) : Bool :=
  let mk := primorial k
  if mk ≤ 1 then true
  else go 0 mk
where
  go (y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if y ≥ primorial k then true
    else
      let pk := primorial k
      -- Periodicity: y + P_k is in the same cylinder as y
      let period_ok := cylinder_mem k y (y + pk)
      -- Separation: y and (y+1) % pk are in different cylinders
      let sep_ok := !cylinder_mem k (y + 1) y || (y + 1 == pk && y == 0)
      period_ok && sep_ok && go (y + 1) (fuel - 1)
  termination_by fuel
```
