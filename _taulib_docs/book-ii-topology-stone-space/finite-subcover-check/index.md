---
{
  "projection_kind": "taulib_declaration",
  "title": "finite_subcover_check",
  "permalink": "/corpus/taulib/docs/book-ii-topology-stone-space/finite-subcover-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Topology.StoneSpace`.",
  "declaration_id": "TauLib.BookII.Topology.StoneSpace::finite_subcover_check",
  "declaration_slug": "finite-subcover-check",
  "kind": "def",
  "name": "finite_subcover_check",
  "module_name": "TauLib.BookII.Topology.StoneSpace",
  "module_url": "/corpus/taulib/docs/book-ii-topology-stone-space/",
  "source_line_start": 91,
  "source_line_end": 105,
  "registry_ids": [
    "II.T07"
  ],
  "related_registry_items": [
    {
      "id": "II.T07",
      "title": "Compactness",
      "url": "/registry/object/II.T07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L91-L105",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.StoneSpace",
        "url": "/corpus/taulib/docs/book-ii-topology-stone-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L91-L105",
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

- Module: [TauLib.BookII.Topology.StoneSpace](/corpus/taulib/docs/book-ii-topology-stone-space/)
- Source path: [`TauLib/BookII/Topology/StoneSpace.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/StoneSpace.lean#L91-L105)
- Source range: L91-L105
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `II.T07` — Compactness

## Immediate Comment / Docstring

```lean
/-- [II.T07] Compactness: every cover by cylinders at stage k has
    a finite subcover. For finite ranges, this is automatic since
    ℤ/M_kℤ is finite (|ℤ/M_kℤ| = M_k residue classes).
    Check: the number of stage-k cylinders in [2, bound] is finite. -/
```

## Source Excerpt

```lean
def finite_subcover_check (k bound : TauIdx) : Bool :=
  let mk := primorial k
  if mk == 0 then true
  else
    -- At stage k, there are at most M_k distinct cylinders
    -- Every element belongs to exactly one
    -- Count distinct residue classes in range
    let residues := go 2 (bound + 1) []
    residues.eraseDups.length ≤ mk
where
  go (y fuel : Nat) (acc : List TauIdx) : List TauIdx :=
    if fuel = 0 then acc
    else if y > bound then acc
    else go (y + 1) (fuel - 1) (reduce y k :: acc)
  termination_by fuel
```
