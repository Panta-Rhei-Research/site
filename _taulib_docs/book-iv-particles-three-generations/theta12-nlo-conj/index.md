---
{
  "projection_kind": "taulib_declaration",
  "title": "theta12_nlo_conj",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/theta12-nlo-conj/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::theta12_nlo_conj",
  "declaration_slug": "theta12-nlo-conj",
  "kind": "theorem",
  "name": "theta12_nlo_conj",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1907,
  "source_line_end": 1911,
  "registry_ids": [
    "IV.T175"
  ],
  "related_registry_items": [
    {
      "id": "IV.T175",
      "title": "θ₁₂ from QLC + Higgs NLO at +3106 ppm",
      "url": "/registry/object/IV.T175/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1907-L1911",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1907-L1911",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1907-L1911)
- Source range: L1907-L1911
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T175` — θ₁₂ from QLC + Higgs NLO at +3106 ppm

## Immediate Comment / Docstring

```lean
/-- [IV.T175] Conjunction: power=2, deviation, zero free params. -/
```

## Source Excerpt

```lean
theorem theta12_nlo_conj :
    theta12_nlo_data.higgs_correction_power = 2 ∧
    theta12_nlo_data.deviation_ppm = 3106 ∧
    theta12_nlo_data.free_params = 0 :=
  ⟨rfl, rfl, rfl⟩
```
