---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L308",
  "permalink": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/eval-l308/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Orthodox.EmergentGeometry`.",
  "declaration_id": "TauLib.BookV.Orthodox.EmergentGeometry::#eval:308",
  "declaration_slug": "eval-l308",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Orthodox.EmergentGeometry",
  "module_url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/",
  "source_line_start": 308,
  "source_line_end": 308,
  "registry_ids": [
    "V.R269",
    "V.R270",
    "V.R271",
    "V.R272",
    "V.R273"
  ],
  "related_registry_items": [
    {
      "id": "V.R269",
      "title": "Spacetime in tau",
      "url": "/registry/object/V.R269/"
    },
    {
      "id": "V.R270",
      "title": "Gravity is already quantum",
      "url": "/registry/object/V.R270/"
    },
    {
      "id": "V.R271",
      "title": "The metric is a derived quantity",
      "url": "/registry/object/V.R271/"
    },
    {
      "id": "V.R272",
      "title": "Dualities as structural echoes",
      "url": "/registry/object/V.R272/"
    },
    {
      "id": "V.R273",
      "title": "Occam and dimensions",
      "url": "/registry/object/V.R273/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L308-L308",
  "formal_status": "computed",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L308-L308",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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
- Source path: [`TauLib/BookV/Orthodox/EmergentGeometry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L308-L308)
- Source range: L308-L308
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R269` — Spacetime in tau
- `V.R270` — Gravity is already quantum
- `V.R271` — The metric is a derived quantity
- `V.R272` — Dualities as structural echoes
- `V.R273` — Occam and dimensions

## Immediate Comment / Docstring

```lean
-- [V.R269] Spacetime in tau: not a manifold (M, g) but a readout
-- of the boundary holonomy algebra. The manifold emerges from the
-- chart projection, like a coastline emerges from a satellite photo.

-- [V.R270] Gravity is already quantum: H_partial[omega] is a
-- non-commutative profinite algebra. There is no classical-to-quantum
-- transition for gravity; the classical limit IS the readout.

-- [V.R271] The metric is a derived quantity: g_mu_nu = pr_chart(h)
-- where h is the holonomy connection on H_partial[omega].

-- [V.R272] Dualities as structural echoes: S-duality, T-duality,
-- mirror symmetry are echoes of the lobe-swap involution on L.

-- [V.R273] Occam and dimensions: tau needs 3 geometric dimensions
-- (the fibered product tau^3 = tau^1 x_f T^2). String theory needs
-- 10 or 11. The extra dimensions in string theory are artifacts of
-- choosing the wrong starting point.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval gr_chart_shadow.preserves_eom        -- true
```
