---
{
  "projection_kind": "taulib_declaration",
  "title": "d_tau_constant",
  "permalink": "/verify/taulib/docs/book-ii-closure-tau-manifold/d-tau-constant/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.TauManifold`.",
  "declaration_id": "TauLib.BookII.Closure.TauManifold::d_tau_constant",
  "declaration_slug": "d-tau-constant",
  "kind": "theorem",
  "name": "d_tau_constant",
  "module_name": "TauLib.BookII.Closure.TauManifold",
  "module_url": "/verify/taulib/docs/book-ii-closure-tau-manifold/",
  "source_line_start": 306,
  "source_line_end": 308,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L306-L308",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L306-L308",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookII/Closure/TauManifold.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L306-L308)
- Source range: L306-L308
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D64` — Tau-Exterior Derivative

## Immediate Comment / Docstring

```lean
/-- [II.D64] d_tau of a constant 0-form is zero.
    tau_exterior_derivative(const_c, x, k) = c - c = 0. -/
```

## Source Excerpt

```lean
theorem d_tau_constant (c : Int) (x k : TauIdx) :
    tau_exterior_derivative (fun _ _ => c) x k = 0 := by
  simp [tau_exterior_derivative]
```
