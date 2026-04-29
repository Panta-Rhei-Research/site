---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_exterior_derivative",
  "permalink": "/verify/taulib/docs/book-ii-closure-tau-manifold/tau-exterior-derivative/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.TauManifold`.",
  "declaration_id": "TauLib.BookII.Closure.TauManifold::tau_exterior_derivative",
  "declaration_slug": "tau-exterior-derivative",
  "kind": "def",
  "name": "tau_exterior_derivative",
  "module_name": "TauLib.BookII.Closure.TauManifold",
  "module_url": "/verify/taulib/docs/book-ii-closure-tau-manifold/",
  "source_line_start": 111,
  "source_line_end": 112,
  "registry_ids": [
    "II.D64"
  ],
  "related_registry_items": [
    {
      "id": "II.D64",
      "title": "Tau-Exterior Derivative",
      "url": "/registry/object/II.D64/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L111-L112",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L111-L112",
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
- Source path: [`TauLib/BookII/Closure/TauManifold.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L111-L112)
- Source range: L111-L112
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D64` — Tau-Exterior Derivative

## Immediate Comment / Docstring

```lean
/-- [II.D64] tau-Exterior derivative acting on a 0-form f at point (x, k).
    d_tau f(x, k) = f(reduce(x+1, k)) - f(reduce(x, k)).
    This is the finite-difference operator on the cyclic group Z/P_kZ. -/
```

## Source Excerpt

```lean
def tau_exterior_derivative (f : TauIdx -> TauIdx -> Int) (x k : TauIdx) : Int :=
  f (reduce (x + 1) k) k - f (reduce x k) k
```
