---
{
  "projection_kind": "taulib_declaration",
  "title": "splitting_count_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/splitting-count-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.BndLift`.",
  "declaration_id": "TauLib.BookII.Hartogs.BndLift::splitting_count_check",
  "declaration_slug": "splitting-count-check",
  "kind": "def",
  "name": "splitting_count_check",
  "module_name": "TauLib.BookII.Hartogs.BndLift",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/",
  "source_line_start": 333,
  "source_line_end": 352,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L333-L352",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L333-L352",
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
- Source path: [`TauLib/BookII/Hartogs/BndLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L333-L352)
- Source range: L333-L352
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Each residue class at stage n splits into exactly p_{n+1}
    residue classes at stage n+1.
    Evidence: for a fixed r < P_n, count elements in [0, P_{n+1})
    with reduce(x, n) = r. Should equal p_{n+1}. -/
```

## Source Excerpt

```lean
def splitting_count_check (stage : TauIdx) : Bool :=
  let pn := primorial stage
  let pn1 := primorial (stage + 1)
  if pn <= 1 || pn1 <= 1 then true
  else go_r 0 (pn + 1)
where
  go_r (r fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if r >= primorial stage then true
    else
      -- Count x in [0, P_{n+1}) with reduce(x, stage) = r
      let count := count_x 0 (primorial (stage + 1)) 0 r
      (count == nth_prime (stage + 1)) &&
      go_r (r + 1) (fuel - 1)
  termination_by fuel
  count_x (x fuel acc r : Nat) : Nat :=
    if fuel = 0 then acc
    else if x >= primorial (stage + 1) then acc
    else count_x (x + 1) (fuel - 1) (acc + if reduce x stage == r then 1 else 0) r
  termination_by fuel
```
