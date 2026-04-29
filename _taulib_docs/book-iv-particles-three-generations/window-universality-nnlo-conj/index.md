---
{
  "projection_kind": "taulib_declaration",
  "title": "window_universality_nnlo_conj",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/window-universality-nnlo-conj/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::window_universality_nnlo_conj",
  "declaration_slug": "window-universality-nnlo-conj",
  "kind": "theorem",
  "name": "window_universality_nnlo_conj",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1017,
  "source_line_end": 1021,
  "registry_ids": [
    "IV.P191"
  ],
  "related_registry_items": [
    {
      "id": "IV.P191",
      "title": "Window RG Period: W₃(4)^k Governs k-th Perturbative Order",
      "url": "/registry/object/IV.P191/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1017-L1021",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1017-L1021",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1017-L1021)
- Source range: L1017-L1021
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P191` — Window RG Period: W₃(4)^k Governs k-th Perturbative Order

## Immediate Comment / Docstring

```lean
/-- [IV.P191] Conjunction: NLO=5, NNLO=25, cross-check=21. -/
```

## Source Excerpt

```lean
theorem window_universality_nnlo_conj :
    window_universality_nnlo_data.nlo_window = 5 ∧
    window_universality_nnlo_data.nnlo_window = 25 ∧
    window_universality_nnlo_data.cross_check = 21 :=
  ⟨rfl, rfl, rfl⟩
```
