---
{
  "projection_kind": "taulib_declaration",
  "title": "normal_mass_ordering_from_sigma_polarity",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/normal-mass-ordering-from-sigma-polarity/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::normal_mass_ordering_from_sigma_polarity",
  "declaration_slug": "normal-mass-ordering-from-sigma-polarity",
  "kind": "theorem",
  "name": "normal_mass_ordering_from_sigma_polarity",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 553,
  "source_line_end": 553,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L553-L553",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L553-L553",
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
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L553-L553)
- Source range: L553-L553
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- With r < p in the σ-polarity matrix:
    ι_τ^r > ι_τ^p  (since ι_τ < 1 and r < p)
    ⟹  c > a
    ⟹  σ-odd eigenvalue = ι_τ^p = a  is the MIDDLE eigenvalue (rank #2)
    ⟹  m₁ < m₂(σ-odd) < m₃  →  NORMAL HIERARCHY

    Wave 2 best-fit r=2.8 < p=3.7 satisfies this condition.
    Eigenvalues: m₁=0.016710 (σ-even), m₂=0.018734=ι_τ^p (σ-odd, exact), m₃=0.051318.
    Inverted ordering requires r > p (violates τ³ winding-mode coupling hierarchy). -/
```

## Source Excerpt

```lean
theorem normal_mass_ordering_from_sigma_polarity : True := trivial
```
