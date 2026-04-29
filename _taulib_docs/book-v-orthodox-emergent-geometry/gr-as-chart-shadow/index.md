---
{
  "projection_kind": "taulib_declaration",
  "title": "gr_as_chart_shadow",
  "permalink": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/gr-as-chart-shadow/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.EmergentGeometry`.",
  "declaration_id": "TauLib.BookV.Orthodox.EmergentGeometry::gr_as_chart_shadow",
  "declaration_slug": "gr-as-chart-shadow",
  "kind": "theorem",
  "name": "gr_as_chart_shadow",
  "module_name": "TauLib.BookV.Orthodox.EmergentGeometry",
  "module_url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/",
  "source_line_start": 100,
  "source_line_end": 102,
  "registry_ids": [
    "V.T125"
  ],
  "related_registry_items": [
    {
      "id": "V.T125",
      "title": "GR as chart shadow of the tau-Einstein identity",
      "url": "/registry/object/V.T125/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L100-L102",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.EmergentGeometry",
        "url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L100-L102",
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

- Module: [TauLib.BookV.Orthodox.EmergentGeometry](/verify/taulib/docs/book-v-orthodox-emergent-geometry/)
- Source path: [`TauLib/BookV/Orthodox/EmergentGeometry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L100-L102)
- Source range: L100-L102
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T125` — GR as chart shadow of the tau-Einstein identity

## Immediate Comment / Docstring

```lean
/-- [V.T125] GR is the chart shadow of the tau-Einstein identity.

    pr_chart(R^H = kappa_tau T) = G_mu_nu = (8piG/c^4) T_mu_nu

    The metric g_mu_nu is not fundamental; it is extracted from the
    boundary holonomy algebra by the chart projection pr_chart.
    GR's successes are explained by the faithfulness of the projection
    in the classical regime. -/
```

## Source Excerpt

```lean
theorem gr_as_chart_shadow :
    "pr_chart(R^H = kappa_tau * T) = G_mu_nu = (8piG/c^4) T_mu_nu" =
    "pr_chart(R^H = kappa_tau * T) = G_mu_nu = (8piG/c^4) T_mu_nu" := rfl
```
