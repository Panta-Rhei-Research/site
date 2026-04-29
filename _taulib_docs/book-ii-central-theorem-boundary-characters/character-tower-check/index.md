---
{
  "projection_kind": "taulib_declaration",
  "title": "character_tower_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/character-tower-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.BoundaryCharacters::character_tower_check",
  "declaration_slug": "character-tower-check",
  "kind": "def",
  "name": "character_tower_check",
  "module_name": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/",
  "source_line_start": 129,
  "source_line_end": 146,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L129-L146",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
        "url": "/verify/taulib/docs/book-ii-central-theorem-boundary-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L129-L146",
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

- Module: [TauLib.BookII.CentralTheorem.BoundaryCharacters](/verify/taulib/docs/book-ii-central-theorem-boundary-characters/)
- Source path: [`TauLib/BookII/CentralTheorem/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L129-L146)
- Source range: L129-L146
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Character tower coherence: reduce(chi(x, k+1), k) = chi(x, k).
    For the canonical character, this means:
    - B: the B-coordinate of from_tau_idx(reduce(reduce(x, k+1), k))
      equals the B-coordinate of from_tau_idx(reduce(x, k))
    - C: similarly for the C-coordinate

    Since reduce(reduce(x, k+1), k) = reduce(x, k) by reduction_compat,
    the same input to from_tau_idx yields the same ABCD chart. -/
```

## Source Excerpt

```lean
def character_tower_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      -- The tower coherence means: the character at the reduced stage
      -- is determined by the reduction. Concretely, verify that the
      -- stage-k character equals the character computed from the
      -- stage-(k+1) reduction projected down.
      let reduced_x := reduce (reduce x (k + 1)) k
      let direct_x := reduce x k
      let tower_ok := reduced_x == direct_x
      -- If the inputs to from_tau_idx are equal, outputs are equal
      tower_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
