---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_independence_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/crt-independence-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.BndLift`.",
  "declaration_id": "TauLib.BookII.Hartogs.BndLift::crt_independence_check",
  "declaration_slug": "crt-independence-check",
  "kind": "def",
  "name": "crt_independence_check",
  "module_name": "TauLib.BookII.Hartogs.BndLift",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/",
  "source_line_start": 198,
  "source_line_end": 215,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L198-L215",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.BndLift",
        "url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L198-L215",
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

- Module: [TauLib.BookII.Hartogs.BndLift](/verify/taulib/docs/book-ii-hartogs-bnd-lift/)
- Source path: [`TauLib/BookII/Hartogs/BndLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L198-L215)
- Source range: L198-L215
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The new prime at stage n+1 provides an independent coordinate.
    For x, y with same stage-n projection but different stage-(n+1) projections,
    they must differ in the new prime factor.
    Evidence: find pairs (x, y) with reduce(x,n) = reduce(y,n) but
    reduce(x,n+1) ≠ reduce(y,n+1), and check their p_{n+1}-residues differ. -/
```

## Source Excerpt

```lean
def crt_independence_check (stage bound : TauIdx) : Bool :=
  go 2 3 ((bound + 1) * (bound + 1))
where
  go (x y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) (x + 2) (fuel - 1)
    else
      -- If same stage-n but different stage-(n+1) projections
      let same_n := reduce x stage == reduce y stage
      let diff_n1 := reduce x (stage + 1) != reduce y (stage + 1)
      let ok :=
        if same_n && diff_n1 then
          -- They must differ in the new prime residue
          x % nth_prime (stage + 1) != y % nth_prime (stage + 1)
        else true
      ok && go x (y + 1) (fuel - 1)
  termination_by fuel
```
