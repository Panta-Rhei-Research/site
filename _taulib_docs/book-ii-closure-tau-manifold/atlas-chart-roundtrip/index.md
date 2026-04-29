---
{
  "projection_kind": "taulib_declaration",
  "title": "atlas_chart_roundtrip",
  "permalink": "/verify/taulib/docs/book-ii-closure-tau-manifold/atlas-chart-roundtrip/",
  "summary_short": "`def` declaration in `TauLib.BookII.Closure.TauManifold`.",
  "declaration_id": "TauLib.BookII.Closure.TauManifold::atlas_chart_roundtrip",
  "declaration_slug": "atlas-chart-roundtrip",
  "kind": "def",
  "name": "atlas_chart_roundtrip",
  "module_name": "TauLib.BookII.Closure.TauManifold",
  "module_url": "/verify/taulib/docs/book-ii-closure-tau-manifold/",
  "source_line_start": 53,
  "source_line_end": 61,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L53-L61",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L53-L61",
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
- Source path: [`TauLib/BookII/Closure/TauManifold.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Closure/TauManifold.lean#L53-L61)
- Source range: L53-L61
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D63` — Tau-Analytic Atlas

## Immediate Comment / Docstring

```lean
/-- [II.D63] Atlas chart check at stage k: verify that the ABCD chart
    (from_tau_idx/to_tau_idx) round-trips for all x in [2, P_k).
    Each chart maps a tau-index to its ABCD quadruple and back. -/
```

## Source Excerpt

```lean
def atlas_chart_roundtrip (k x fuel : Nat) : Bool :=
  if fuel = 0 then true
  else if x >= primorial k then true
  else if x < 2 then atlas_chart_roundtrip k (x + 1) (fuel - 1)
  else
    let p := from_tau_idx x
    let rt := to_tau_idx p
    (rt == x) && atlas_chart_roundtrip k (x + 1) (fuel - 1)
termination_by fuel
```
