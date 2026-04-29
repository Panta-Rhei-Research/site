---
{
  "projection_kind": "taulib_declaration",
  "title": "window_universality_all_7",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/window-universality-all-7/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::window_universality_all_7",
  "declaration_slug": "window-universality-all-7",
  "kind": "def",
  "name": "window_universality_all_7",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 2182,
  "source_line_end": 2184,
  "registry_ids": [
    "IV.P205"
  ],
  "related_registry_items": [
    {
      "id": "IV.P205",
      "title": "Window Universality for All 7 NNLO Exponents",
      "url": "/registry/object/IV.P205/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2182-L2184",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2182-L2184",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L2182-L2184)
- Source range: L2182-L2184
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.P205` — Window Universality for All 7 NNLO Exponents

## Immediate Comment / Docstring

```lean
/-- [IV.P205] Window Universality for All 7 NNLO Exponents.
    All 7 decompose into {W₃(3), W₃(4), dim, lobes, sectors, N_c}. -/
```

## Source Excerpt

```lean
def window_universality_all_7 : String :=
  "All 7 NLO/NNLO exponents decompose via Window algebra building blocks. " ++
  "W₃(4)=5 universal. Two m_μ/m_e exponents differ by 1/(lobes·sectors) = 1/6."
```
