---
{
  "projection_kind": "taulib_declaration",
  "title": "orbit_length",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-witness/orbit-length/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.E2Witness`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Witness::orbit_length",
  "declaration_slug": "orbit-length",
  "kind": "def",
  "name": "orbit_length",
  "module_name": "TauLib.BookIII.Computation.E2Witness",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-witness/",
  "source_line_start": 95,
  "source_line_end": 105,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L95-L105",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L95-L105",
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
- Source path: [`TauLib/BookIII/Computation/E2Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L95-L105)
- Source range: L95-L105
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D84` — E₂ Orbit Structure

## Immediate Comment / Docstring

```lean
/-- [III.D84] Orbit of code c under decoder d at stage k:
    length of the cycle c → (c+d) → (c+2d) → ... → c. -/
```

## Source Excerpt

```lean
def orbit_length (c d k : Nat) : Nat :=
  let pk := primorial k
  if pk == 0 || d % pk == 0 then 1
  else
    go ((c + d) % pk) c pk 1 pk
where
  go (pos start pk steps fuel : Nat) : Nat :=
    if fuel = 0 then steps
    else if pos == start then steps
    else go ((pos + d) % pk) start pk (steps + 1) (fuel - 1)
  termination_by fuel
```
