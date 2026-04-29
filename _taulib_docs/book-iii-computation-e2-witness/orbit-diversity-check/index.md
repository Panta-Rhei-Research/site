---
{
  "projection_kind": "taulib_declaration",
  "title": "orbit_diversity_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-e2-witness/orbit-diversity-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.E2Witness`.",
  "declaration_id": "TauLib.BookIII.Computation.E2Witness::orbit_diversity_check",
  "declaration_slug": "orbit-diversity-check",
  "kind": "def",
  "name": "orbit_diversity_check",
  "module_name": "TauLib.BookIII.Computation.E2Witness",
  "module_url": "/verify/taulib/docs/book-iii-computation-e2-witness/",
  "source_line_start": 108,
  "source_line_end": 117,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L108-L117",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L108-L117",
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
- Source path: [`TauLib/BookIII/Computation/E2Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/E2Witness.lean#L108-L117)
- Source range: L108-L117
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D84` — E₂ Orbit Structure

## Immediate Comment / Docstring

```lean
/-- [III.D84] Collect distinct orbit lengths at stage k for all (c, d). -/
```

## Source Excerpt

```lean
def orbit_diversity_check (k : Nat) : Bool :=
  let pk := primorial k
  if pk <= 2 then true  -- trivially diverse at small stages
  else
    -- Check that not all orbits have the same length
    let len_0_1 := orbit_length 0 1 k
    let len_1_1 := orbit_length 1 1 k
    let len_0_2 := orbit_length 0 2 k
    -- Diversity: at least two distinct orbit lengths exist
    len_0_1 != len_0_2 || len_0_1 != len_1_1 || pk <= 2
```
