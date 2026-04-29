---
{
  "projection_kind": "taulib_declaration",
  "title": "atlas_transition_check",
  "permalink": "/verify/taulib/docs/book-ii-closure-tau-manifold/atlas-transition-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.TauManifold`.",
  "declaration_id": "TauLib.BookII.Closure.TauManifold::atlas_transition_check",
  "declaration_slug": "atlas-transition-check",
  "kind": "def",
  "name": "atlas_transition_check",
  "module_name": "TauLib.BookII.Closure.TauManifold",
  "module_url": "/verify/taulib/docs/book-ii-closure-tau-manifold/",
  "source_line_start": 88,
  "source_line_end": 102,
  "registry_ids": [
    "II.D63"
  ],
  "related_registry_items": [
    {
      "id": "II.D63",
      "title": "Tau-Analytic Atlas",
      "url": "/registry/object/II.D63/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L88-L102",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Closure.TauManifold",
        "url": "/verify/taulib/docs/book-ii-closure-tau-manifold/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L88-L102",
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

- Module: [TauLib.BookII.Closure.TauManifold](/verify/taulib/docs/book-ii-closure-tau-manifold/)
- Source path: [`TauLib/BookII/Closure/TauManifold.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L88-L102)
- Source range: L88-L102
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D63` — Tau-Analytic Atlas

## Immediate Comment / Docstring

```lean
/-- [II.D63] Atlas transition check: chart transitions from stage k+1
    to stage k are reduce-compatible. For any x at stage k+1, reducing
    to stage k and then applying from_tau_idx at stage k must agree with
    directly reducing the ABCD-reconstructed value.

    Concretely: reduce(to_tau_idx(from_tau_idx(x)), k) = reduce(x, k).
    Since to_tau_idx(from_tau_idx(x)) = x (round-trip), this reduces to
    reduce(x, k) = reduce(x, k), which is trivial.

    The nontrivial check: the ABCD coordinates at stage k+1 project
    consistently to stage k. -/
```

## Source Excerpt

```lean
def atlas_transition_check (db bound : TauIdx) : Bool :=
  go 1 2 ((db + 1) * (bound + 1))
where
  go (k x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else if x > bound then go (k + 1) 2 (fuel - 1)
    else
      let p_k1 := from_tau_idx x
      let reconstructed := to_tau_idx p_k1
      let reduced_direct := reduce x k
      let reduced_via_chart := reduce reconstructed k
      let ok := reduced_direct == reduced_via_chart
      ok && go k (x + 1) (fuel - 1)
  termination_by fuel
```
