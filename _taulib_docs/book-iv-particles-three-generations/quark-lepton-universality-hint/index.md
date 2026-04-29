---
{
  "projection_kind": "taulib_declaration",
  "title": "quark_lepton_universality_hint",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/quark-lepton-universality-hint/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::quark_lepton_universality_hint",
  "declaration_slug": "quark-lepton-universality-hint",
  "kind": "theorem",
  "name": "quark_lepton_universality_hint",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 736,
  "source_line_end": 740,
  "registry_ids": [
    "IV.P187"
  ],
  "related_registry_items": [
    {
      "id": "IV.P187",
      "title": "Quark-Lepton Universality: Exponent Step ≈ −2.7",
      "url": "/registry/object/IV.P187/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L736-L740",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L736-L740",
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
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L736-L740)
- Source range: L736-L740
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P187` — Quark-Lepton Universality: Exponent Step ≈ −2.7

## Immediate Comment / Docstring

```lean
/-- [IV.P187] Conjunction: step ~2700, 2 sectors, diff 171 (>100 threshold). -/
```

## Source Excerpt

```lean
theorem quark_lepton_universality_hint :
    quark_lepton_universality_data.step_x1000 = 2700 ∧
    quark_lepton_universality_data.n_matching_sectors = 2 ∧
    quark_lepton_universality_data.step_diff_x1000 = 171 :=
  ⟨rfl, rfl, rfl⟩
```
