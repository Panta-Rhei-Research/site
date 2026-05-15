---
{
  "projection_kind": "taulib_declaration",
  "title": "gauge_3_count",
  "permalink": "/corpus/taulib/docs/book-iii-physics-strong-sector/gauge-3-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.StrongSector`.",
  "declaration_id": "TauLib.BookIII.Physics.StrongSector::gauge_3_count",
  "declaration_slug": "gauge-3-count",
  "kind": "theorem",
  "name": "gauge_3_count",
  "module_name": "TauLib.BookIII.Physics.StrongSector",
  "module_url": "/corpus/taulib/docs/book-iii-physics-strong-sector/",
  "source_line_start": 223,
  "source_line_end": 225,
  "registry_ids": [
    "III.D44"
  ],
  "related_registry_items": [
    {
      "id": "III.D44",
      "title": "τ-Admissible Gauge Data",
      "url": "/registry/object/III.D44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L223-L225",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.StrongSector",
        "url": "/corpus/taulib/docs/book-iii-physics-strong-sector/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L223-L225",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIII.Physics.StrongSector](/corpus/taulib/docs/book-iii-physics-strong-sector/)
- Source path: [`TauLib/BookIII/Physics/StrongSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L223-L225)
- Source range: L223-L225
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D44` — τ-Admissible Gauge Data

## Immediate Comment / Docstring

```lean
/-- [III.D44] Structural: gauge data at depth 3 has correct counts. -/
```

## Source Excerpt

```lean
theorem gauge_3_count :
    (gauge_data_at 3).b_count + (gauge_data_at 3).c_count +
    (gauge_data_at 3).x_count = 3 := by native_decide
```
