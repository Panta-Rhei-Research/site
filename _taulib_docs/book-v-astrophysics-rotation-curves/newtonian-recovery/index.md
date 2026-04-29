---
{
  "projection_kind": "taulib_declaration",
  "title": "newtonian_recovery",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/newtonian-recovery/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::newtonian_recovery",
  "declaration_slug": "newtonian-recovery",
  "kind": "theorem",
  "name": "newtonian_recovery",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 145,
  "source_line_end": 147,
  "registry_ids": [
    "V.P67"
  ],
  "related_registry_items": [
    {
      "id": "V.P67",
      "title": "Galaxy-by-Galaxy Concordance --- V.P31",
      "url": "/registry/object/V.P67/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L145-L147",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L145-L147",
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
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L145-L147)
- Source range: L145-L147
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P67` — Galaxy-by-Galaxy Concordance --- V.P31

## Immediate Comment / Docstring

```lean
/-- [V.P67] Newtonian regime recovery: at high accelerations (g >> a₀),
    the boundary holonomy correction vanishes and standard Newtonian
    gravity is recovered exactly. -/
```

## Source Excerpt

```lean
theorem newtonian_recovery (bhc : BoundaryHolonomyCorrection)
    (h : bhc.regime = .Newtonian) :
    bhc.g_effective = bhc.g_newtonian := bhc.newtonian_approx h
```
