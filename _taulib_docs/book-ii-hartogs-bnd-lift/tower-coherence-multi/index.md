---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_coherence_multi",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/tower-coherence-multi/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.BndLift`.",
  "declaration_id": "TauLib.BookII.Hartogs.BndLift::tower_coherence_multi",
  "declaration_slug": "tower-coherence-multi",
  "kind": "def",
  "name": "tower_coherence_multi",
  "module_name": "TauLib.BookII.Hartogs.BndLift",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/",
  "source_line_start": 161,
  "source_line_end": 173,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L161-L173",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L161-L173",
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
- Source path: [`TauLib/BookII/Hartogs/BndLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L161-L173)
- Source range: L161-L173
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tower coherence across multiple levels: reducing a lift at stage n+2
    back to stage n should equal the direct stage-n reduction.
    reduce(bndlift(bndlift(x, n), n+1), n) = reduce(x, n). -/
```

## Source Excerpt

```lean
def tower_coherence_multi (k_max bound : TauIdx) : Bool :=
  go 1 2 (k_max * bound + k_max + bound + 1)
where
  go (stage x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if stage + 1 > k_max then true
    else if x > bound then go (stage + 1) 2 (fuel - 1)
    else
      let lifted_once := bndlift x stage
      let lifted_twice := bndlift lifted_once (stage + 1)
      (reduce lifted_twice stage == reduce x stage) &&
      go stage (x + 1) (fuel - 1)
  termination_by fuel
```
