---
{
  "projection_kind": "taulib_declaration",
  "title": "eta_bar_candidate_conj",
  "permalink": "/corpus/taulib/docs/book-iv-particles-three-generations/eta-bar-candidate-conj/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::eta_bar_candidate_conj",
  "declaration_slug": "eta-bar-candidate-conj",
  "kind": "theorem",
  "name": "eta_bar_candidate_conj",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/corpus/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 1298,
  "source_line_end": 1302,
  "registry_ids": [
    "IV.P197"
  ],
  "related_registry_items": [
    {
      "id": "IV.P197",
      "title": "eta_bar from CP Phase Structure: Best tau-Candidate sqrt(5)/(2*pi)",
      "url": "/registry/object/IV.P197/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1298-L1302",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/corpus/taulib/docs/book-iv-particles-three-generations/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1298-L1302",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/corpus/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L1298-L1302)
- Source range: L1298-L1302
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.P197` — eta_bar from CP Phase Structure: Best tau-Candidate sqrt(5)/(2*pi)

## Immediate Comment / Docstring

```lean
/-- [IV.P197] Conjunction: √5 radicand, 2π period, large deviation. -/
```

## Source Excerpt

```lean
theorem eta_bar_candidate_conj :
    eta_bar_candidate_data.sqrt_radicand = 5 ∧
    eta_bar_candidate_data.omega_period_multiplier = 2 ∧
    eta_bar_candidate_data.deviation_ppm = 22647 :=
  ⟨rfl, rfl, rfl⟩
```
