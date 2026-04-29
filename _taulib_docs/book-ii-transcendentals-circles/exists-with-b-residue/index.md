---
{
  "projection_kind": "taulib_declaration",
  "title": "exists_with_b_residue",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-circles/exists-with-b-residue/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.Circles`.",
  "declaration_id": "TauLib.BookII.Transcendentals.Circles::exists_with_b_residue",
  "declaration_slug": "exists-with-b-residue",
  "kind": "def",
  "name": "exists_with_b_residue",
  "module_name": "TauLib.BookII.Transcendentals.Circles",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-circles/",
  "source_line_start": 51,
  "source_line_end": 59,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L51-L59",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L51-L59",
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
- Source path: [`TauLib/BookII/Transcendentals/Circles.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L51-L59)
- Source range: L51-L59
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Check whether a given residue r appears as a B-residue mod p_k
    in some tau-admissible point in [2, bound]. -/
```

## Source Excerpt

```lean
def exists_with_b_residue (r k bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then false
    else if x > bound then false
    else if solenoidal_b_orbit x k == r then true
    else go (x + 1) (fuel - 1)
  termination_by fuel
```
