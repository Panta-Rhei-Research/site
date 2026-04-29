---
{
  "projection_kind": "taulib_declaration",
  "title": "rar_from_single_coupling",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/rar-from-single-coupling/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::rar_from_single_coupling",
  "declaration_slug": "rar-from-single-coupling",
  "kind": "theorem",
  "name": "rar_from_single_coupling",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 160,
  "source_line_end": 162,
  "registry_ids": [
    "V.P68"
  ],
  "related_registry_items": [
    {
      "id": "V.P68",
      "title": "MOND as Capacity Proxy --- V.P32",
      "url": "/registry/object/V.P68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L160-L162",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.RotationCurves",
        "url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L160-L162",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L160-L162)
- Source range: L160-L162
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P68` — MOND as Capacity Proxy --- V.P32

## Immediate Comment / Docstring

```lean
/-- [V.P68] Radial Acceleration Relation from single coupling: the
    tight correlation between observed and baryonic acceleration
    (McGaugh et al. 2016) emerges from a single D-sector coupling
    with boundary corrections.

    No dark matter profile tuning is needed because there is only
    ONE coupling function, not two (baryonic + dark). -/
```

## Source Excerpt

```lean
theorem rar_from_single_coupling :
    "RAR g_obs = F(g_bar) from single D-sector coupling, no DM profile" =
    "RAR g_obs = F(g_bar) from single D-sector coupling, no DM profile" := rfl
```
