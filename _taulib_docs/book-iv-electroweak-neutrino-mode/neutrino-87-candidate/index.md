---
{
  "projection_kind": "taulib_declaration",
  "title": "neutrino_87_candidate",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-87-candidate/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::neutrino_87_candidate",
  "declaration_slug": "neutrino-87-candidate",
  "kind": "theorem",
  "name": "neutrino_87_candidate",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 718,
  "source_line_end": 724,
  "registry_ids": [
    "V.T177"
  ],
  "related_registry_items": [
    {
      "id": "V.T177",
      "title": "(8/7, 6/7) Candidate: Neutrino Mass Ratio from Lemniscate n=7",
      "url": "/registry/object/V.T177/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L718-L724",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L718-L724",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L718-L724)
- Source range: L718-L724
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T177` — (8/7, 6/7) Candidate: Neutrino Mass Ratio from Lemniscate n=7

## Immediate Comment / Docstring

```lean
/-- [V.T177] Conjunction: 8/7 numerator, 4/3 ratio, span=lobes. -/
```

## Source Excerpt

```lean
theorem neutrino_87_candidate :
    neutrino_87_data.numerator = 8 ∧
    neutrino_87_data.denominator = 7 ∧
    neutrino_87_data.numerator_pr = 6 ∧
    neutrino_87_data.ratio_exact_43 = true ∧
    neutrino_87_data.span_eq_lobes = true :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩
```
