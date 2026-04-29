---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_character_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/boundary-character-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.MutualDetermination`.",
  "declaration_id": "TauLib.BookII.Hartogs.MutualDetermination::boundary_character_check",
  "declaration_slug": "boundary-character-check",
  "kind": "def",
  "name": "boundary_character_check",
  "module_name": "TauLib.BookII.Hartogs.MutualDetermination",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/",
  "source_line_start": 158,
  "source_line_end": 174,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L158-L174",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.MutualDetermination",
        "url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L158-L174",
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

- Module: [TauLib.BookII.Hartogs.MutualDetermination](/verify/taulib/docs/book-ii-hartogs-mutual-determination/)
- Source path: [`TauLib/BookII/Hartogs/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L158-L174)
- Source range: L158-L174
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.L04, clause C] Boundary character determined by B/C data:
    the B and C components of from_tau_idx encode the bipolar character
    assignment. The character is determined by the idempotent decomposition:
    e_plus projects onto the B-sector, e_minus onto the C-sector.

    We verify: the sector pair (B, C) is consistent with the idempotent
    decomposition — applying e_plus projects to (B, 0) and e_minus to (0, C),
    and their sum recovers (B, C). -/
```

## Source Excerpt

```lean
def boundary_character_check (bound _db : TauIdx) : Bool :=
  go 2 ((bound + 1))
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let p := from_tau_idx x
      let sp : SectorPair := ⟨(p.b : Int), (p.c : Int)⟩
      -- e_plus projects onto B-sector
      let proj_b := SectorPair.mul e_plus_sector sp
      -- e_minus projects onto C-sector
      let proj_c := SectorPair.mul e_minus_sector sp
      -- Their sum recovers the full sector pair
      let ok := SectorPair.add proj_b proj_c == sp
      ok && go (x + 1) (fuel - 1)
  termination_by fuel
```
