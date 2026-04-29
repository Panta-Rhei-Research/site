---
{
  "projection_kind": "taulib_declaration",
  "title": "primitive_winding_classes",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/primitive-winding-classes/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::primitive_winding_classes",
  "declaration_slug": "primitive-winding-classes",
  "kind": "def",
  "name": "primitive_winding_classes",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 644,
  "source_line_end": 645,
  "registry_ids": [
    "IV.D347"
  ],
  "related_registry_items": [
    {
      "id": "IV.D347",
      "title": "Three Primitive Winding Classes on T²",
      "url": "/registry/object/IV.D347/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L644-L645",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L644-L645",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L644-L645)
- Source range: L644-L645
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D347` — Three Primitive Winding Classes on T²

## Immediate Comment / Docstring

```lean
/-- The three primitive winding classes on T²: modes with the three
    lowest positive Laplacian eigenvalues among primitive (gcd=1) modes,
    given r/R = ι_τ. Eigenvalues (in 1/R²): (1,0)→1, (0,1)→ι_τ⁻²≈8.585,
    (1,1)→1+ι_τ⁻²≈9.585. Non-primitive (2,0) at λ=4 is excluded. [IV.D347] -/
```

## Source Excerpt

```lean
def primitive_winding_classes : List (Int × Int) :=
  [(1, 0), (0, 1), (1, 1)]
```
