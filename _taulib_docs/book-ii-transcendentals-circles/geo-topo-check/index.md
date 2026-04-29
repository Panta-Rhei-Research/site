---
{
  "projection_kind": "taulib_declaration",
  "title": "geo_topo_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-circles/geo-topo-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.Circles`.",
  "declaration_id": "TauLib.BookII.Transcendentals.Circles::geo_topo_check",
  "declaration_slug": "geo-topo-check",
  "kind": "def",
  "name": "geo_topo_check",
  "module_name": "TauLib.BookII.Transcendentals.Circles",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-circles/",
  "source_line_start": 105,
  "source_line_end": 110,
  "registry_ids": [
    "II.D27"
  ],
  "related_registry_items": [
    {
      "id": "II.D27",
      "title": "Geometric-Topological Unification",
      "url": "/registry/object/II.D27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L105-L110",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L105-L110",
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
- Source path: [`TauLib/BookII/Transcendentals/Circles.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Circles.lean#L105-L110)
- Source range: L105-L110
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D27` — Geometric-Topological Unification

## Immediate Comment / Docstring

```lean
/-- [II.D27] Geometric-topological unification: B and C orbits are
    independently cyclic at each stage. T^2 = S^1_B x S^1_C.

    Evidence: both B and C projections are surjective onto Z/p_k Z
    for the first few primes. -/
```

## Source Excerpt

```lean
def geo_topo_check (bound : TauIdx) : Bool :=
  -- Check for k=1 (p=2) and k=2 (p=3)
  circle_profinite_b_check 1 bound &&
  circle_profinite_c_check 1 bound &&
  circle_profinite_b_check 2 bound &&
  circle_profinite_c_check 2 bound
```
