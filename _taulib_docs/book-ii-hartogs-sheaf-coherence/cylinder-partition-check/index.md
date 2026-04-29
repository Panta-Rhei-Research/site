---
{
  "projection_kind": "taulib_declaration",
  "title": "cylinder_partition_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/cylinder-partition-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.SheafCoherence`.",
  "declaration_id": "TauLib.BookII.Hartogs.SheafCoherence::cylinder_partition_check",
  "declaration_slug": "cylinder-partition-check",
  "kind": "def",
  "name": "cylinder_partition_check",
  "module_name": "TauLib.BookII.Hartogs.SheafCoherence",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/",
  "source_line_start": 63,
  "source_line_end": 88,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L63-L88",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.SheafCoherence",
        "url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L63-L88",
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

- Module: [TauLib.BookII.Hartogs.SheafCoherence](/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/)
- Source path: [`TauLib/BookII/Hartogs/SheafCoherence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L63-L88)
- Source range: L63-L88
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Cylinder partition check: at stage k, every x in [0, P_k) belongs
    to exactly one cylinder C_{k,a}. The cylinders partition Z/P_kZ. -/
```

## Source Excerpt

```lean
def cylinder_partition_check (k : TauIdx) : Bool :=
  let pk := primorial k
  if pk == 0 then true
  else go 0 pk k
where
  go (x fuel k : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= primorial k then true
    else
      -- x belongs to exactly one cylinder: C_{k, reduce(x,k)}
      let a := reduce x k
      -- Verify membership
      let mem := presheaf_assign k a x
      -- Verify uniqueness: no other cylinder contains x
      let unique := check_unique x 0 k a (primorial k)
      mem && unique && go (x + 1) (fuel - 1) k
  termination_by fuel
  check_unique (x b k target fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if b >= primorial k then true
    else
      let mem := presheaf_assign k b x
      -- If b != target, then x should NOT be in C_{k,b}
      let ok := b == target || !mem
      ok && check_unique x (b + 1) k target (fuel - 1)
  termination_by fuel
```
