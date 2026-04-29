---
{
  "projection_kind": "taulib_declaration",
  "title": "j_squared_wave",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-categoricity/j-squared-wave/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.Categoricity`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.Categoricity::j_squared_wave",
  "declaration_slug": "j-squared-wave",
  "kind": "theorem",
  "name": "j_squared_wave",
  "module_name": "TauLib.BookII.CentralTheorem.Categoricity",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/",
  "source_line_start": 333,
  "source_line_end": 335,
  "registry_ids": [
    "II.T41"
  ],
  "related_registry_items": [
    {
      "id": "II.T41",
      "title": "Liouville Categorical Dodge",
      "url": "/registry/object/II.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L333-L335",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.Categoricity",
        "url": "/verify/taulib/docs/book-ii-central-theorem-categoricity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L333-L335",
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

- Module: [TauLib.BookII.CentralTheorem.Categoricity](/verify/taulib/docs/book-ii-central-theorem-categoricity/)
- Source path: [`TauLib/BookII/CentralTheorem/Categoricity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/Categoricity.lean#L333-L335)
- Source range: L333-L335
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.T41` — Liouville Categorical Dodge

## Immediate Comment / Docstring

```lean
/-- [II.T41] j^2 = +1 (wave type, not elliptic).
    This is the structural reason Liouville's theorem does not apply. -/
```

## Source Excerpt

```lean
theorem j_squared_wave :
    SplitComplex.mul SplitComplex.j SplitComplex.j = SplitComplex.one := by
  simp [SplitComplex.j, SplitComplex.mul, SplitComplex.one]
```
