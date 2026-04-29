---
{
  "projection_kind": "taulib_declaration",
  "title": "nnlo_exponent_catalog",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/nnlo-exponent-catalog/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::nnlo_exponent_catalog",
  "declaration_slug": "nnlo-exponent-catalog",
  "kind": "def",
  "name": "nnlo_exponent_catalog",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2125,
  "source_line_end": 2128,
  "registry_ids": [
    "IV.D367"
  ],
  "related_registry_items": [
    {
      "id": "IV.D367",
      "title": "NNLO Exponent Catalog: 7 Window-Universal Corrections",
      "url": "/registry/object/IV.D367/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2125-L2128",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2125-L2128",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2125-L2128)
- Source range: L2125-L2128
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D367` — NNLO Exponent Catalog: 7 Window-Universal Corrections

## Immediate Comment / Docstring

```lean
/-- [IV.D367] NNLO Exponent Catalog (7 entries).
    All decompose via {W₃(3)=17, W₃(4)=5, dim=3, lobes=2, sectors=3, N_c=3}. -/
```

## Source Excerpt

```lean
def nnlo_exponent_catalog : String :=
  "7 NNLO exponents, all Window-universal: " ++
  "23/3, 15/2, 3/16, 3/20, 5/7, 1/5, 17/5. " ++
  "W₃(4)=5 in all 7. k₁−k₂ = 1/6 = 1/(lobes·sectors)."
```
