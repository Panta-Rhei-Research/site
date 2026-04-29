---
{
  "projection_kind": "taulib_declaration",
  "title": "count_distinct_orbit_lengths",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-witness/count-distinct-orbit-lengths/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.E2Witness`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Witness::count_distinct_orbit_lengths",
  "declaration_slug": "count-distinct-orbit-lengths",
  "kind": "def",
  "name": "count_distinct_orbit_lengths",
  "module_name": "TauLib.BookIII.Computation.E2Witness",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-witness/",
  "source_line_start": 120,
  "source_line_end": 139,
  "registry_ids": [
    "III.D84"
  ],
  "related_registry_items": [
    {
      "id": "III.D84",
      "title": "E₂ Orbit Structure",
      "url": "/registry/object/III.D84/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L120-L139",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.E2Witness",
        "url": "/verify/taulib/docs/book-iii-computation-e2-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L120-L139",
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

- Module: [TauLib.BookIII.Computation.E2Witness](/verify/taulib/docs/book-iii-computation-e2-witness/)
- Source path: [`TauLib/BookIII/Computation/E2Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L120-L139)
- Source range: L120-L139
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D84` — E₂ Orbit Structure

## Immediate Comment / Docstring

```lean
/-- [III.D84] Count distinct orbit lengths at stage k. -/
```

## Source Excerpt

```lean
def count_distinct_orbit_lengths (k : Nat) : Nat :=
  let pk := primorial k
  go_d 1 pk 0 pk k
where
  go_d (d pk acc fuel k : Nat) : Nat :=
    if fuel = 0 then acc
    else if d >= pk then acc
    else
      let len := orbit_length 0 d k
      -- Check if this length was already seen (approximate)
      let new_len := if is_new_length len d pk k then 1 else 0
      go_d (d + 1) pk (acc + new_len) (fuel - 1) k
  termination_by fuel
  is_new_length (len d pk k : Nat) : Bool :=
    go_check 1 d len pk k
  go_check (d2 bound target pk k : Nat) : Bool :=
    if d2 >= bound then true  -- not found before → new
    else if orbit_length 0 d2 k == target then false
    else go_check (d2 + 1) bound target pk k
  termination_by bound - d2
```
