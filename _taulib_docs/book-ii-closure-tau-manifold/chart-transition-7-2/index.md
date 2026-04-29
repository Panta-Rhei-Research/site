---
{
  "projection_kind": "taulib_declaration",
  "title": "chart_transition_7_2",
  "permalink": "/verify/taulib/docs/book-ii-closure-tau-manifold/chart-transition-7-2/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Closure.TauManifold`.",
  "declaration_id": "TauLib.BookII.Closure.TauManifold::chart_transition_7_2",
  "declaration_slug": "chart-transition-7-2",
  "kind": "theorem",
  "name": "chart_transition_7_2",
  "module_name": "TauLib.BookII.Closure.TauManifold",
  "module_url": "/verify/taulib/docs/book-ii-closure-tau-manifold/",
  "source_line_start": 298,
  "source_line_end": 299,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L298-L299",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L298-L299",
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
- Source path: [`TauLib/BookII/Closure/TauManifold.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L298-L299)
- Source range: L298-L299
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D63` — Tau-Analytic Atlas

## Immediate Comment / Docstring

```lean
/-- [II.D63] Chart transitions are reduce-compatible:
    reduce(to_tau_idx(from_tau_idx(x)), k) = reduce(x, k).
    Verified for specific instances. -/
```

## Source Excerpt

```lean
theorem chart_transition_7_2 :
    reduce (to_tau_idx (from_tau_idx 7)) 2 = reduce 7 2 := by native_decide
```
