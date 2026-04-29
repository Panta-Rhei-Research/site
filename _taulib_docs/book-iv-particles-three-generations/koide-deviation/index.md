---
{
  "projection_kind": "taulib_declaration",
  "title": "koide_deviation",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/koide-deviation/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::koide_deviation",
  "declaration_slug": "koide-deviation",
  "kind": "def",
  "name": "koide_deviation",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 380,
  "source_line_end": 381,
  "registry_ids": [
    "IV.R116"
  ],
  "related_registry_items": [
    {
      "id": "IV.R116",
      "title": "Why 0.0009% and not exact",
      "url": "/registry/object/IV.R116/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L380-L381",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L380-L381",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L380-L381)
- Source range: L380-L381
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.R116` — Why 0.0009% and not exact

## Immediate Comment / Docstring

```lean
/-- [IV.R116] Q_exp − 2/3 = −6×10⁻⁶ is of order α² ≈ 5×10⁻⁵.
    Consistent with radiative correction from EM vacuum polarization. -/
```

## Source Excerpt

```lean
def koide_deviation : String :=
  "Q_exp - 2/3 = -6e-6, of order alpha^2 ~ 5e-5"
```
