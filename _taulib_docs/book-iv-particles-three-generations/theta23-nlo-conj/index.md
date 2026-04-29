---
{
  "projection_kind": "taulib_declaration",
  "title": "theta23_nlo_conj",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/theta23-nlo-conj/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::theta23_nlo_conj",
  "declaration_slug": "theta23-nlo-conj",
  "kind": "theorem",
  "name": "theta23_nlo_conj",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1871,
  "source_line_end": 1875,
  "registry_ids": [
    "IV.T174"
  ],
  "related_registry_items": [
    {
      "id": "IV.T174",
      "title": "θ₂₃ NLO via Window Algebra at +8604 ppm",
      "url": "/registry/object/IV.T174/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1871-L1875",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1871-L1875",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1871-L1875)
- Source range: L1871-L1875
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T174` — θ₂₃ NLO via Window Algebra at +8604 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T174] Conjunction: W₃(4)=5, NLO deviation, LO deviation. -/
```

## Source Excerpt

```lean
theorem theta23_nlo_conj :
    theta23_nlo_data.window_exp = 5 ∧
    theta23_nlo_data.deviation_ppm = 8604 ∧
    theta23_nlo_data.lo_deviation_ppm = 18012 :=
  ⟨rfl, rfl, rfl⟩
```
