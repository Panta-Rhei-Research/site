---
{
  "projection_kind": "taulib_declaration",
  "title": "circle_profinite_b_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-circles/circle-profinite-b-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.Circles`.",
  "declaration_id": "TauLib.BookII.Transcendentals.Circles::circle_profinite_b_check",
  "declaration_slug": "circle-profinite-b-check",
  "kind": "def",
  "name": "circle_profinite_b_check",
  "module_name": "TauLib.BookII.Transcendentals.Circles",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-circles/",
  "source_line_start": 75,
  "source_line_end": 83,
  "registry_ids": [
    "II.T21"
  ],
  "related_registry_items": [
    {
      "id": "II.T21",
      "title": "S^1 as Profinite Limit",
      "url": "/registry/object/II.T21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L75-L83",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.Circles",
        "url": "/verify/taulib/docs/book-ii-transcendentals-circles/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L75-L83",
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

- Module: [TauLib.BookII.Transcendentals.Circles](/verify/taulib/docs/book-ii-transcendentals-circles/)
- Source path: [`TauLib/BookII/Transcendentals/Circles.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L75-L83)
- Source range: L75-L83
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T21` — S^1 as Profinite Limit

## Immediate Comment / Docstring

```lean
/-- [II.T21] S^1 as profinite limit: all residues 0..p_k-1 appear
    in the B-coordinate of some tau-admissible point in [2, bound].
    This witnesses the surjectivity of the B-projection onto Z/p_k Z. -/
```

## Source Excerpt

```lean
def circle_profinite_b_check (k bound : TauIdx) : Bool :=
  let pk := nth_prime k
  go 0 (pk + 1)
where
  go (r fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if r >= nth_prime k then true
    else exists_with_b_residue r k bound && go (r + 1) (fuel - 1)
  termination_by fuel
```
