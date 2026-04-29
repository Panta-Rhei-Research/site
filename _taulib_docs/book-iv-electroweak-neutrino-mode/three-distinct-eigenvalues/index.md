---
{
  "projection_kind": "taulib_declaration",
  "title": "three_distinct_eigenvalues",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/three-distinct-eigenvalues/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::three_distinct_eigenvalues",
  "declaration_slug": "three-distinct-eigenvalues",
  "kind": "theorem",
  "name": "three_distinct_eigenvalues",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 408,
  "source_line_end": 409,
  "registry_ids": [
    "V.T165"
  ],
  "related_registry_items": [
    {
      "id": "V.T165",
      "title": "Mass Eigenvalue Ratio Formula",
      "url": "/registry/object/V.T165/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L408-L409",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L408-L409",
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
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L408-L409)
- Source range: L408-L409
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T165` — Mass Eigenvalue Ratio Formula

## Immediate Comment / Docstring

```lean
/-- [V.T165] The sigma-polarity matrix has three distinct eigenvalues.
    Eigenvalue structure (Sprint 3):
    - λ₂ = a = ι_τ^p (sigma-odd, [1,0,-1]/√2, Majorana candidate)
    - λ₁ < a < λ₃ (two sigma-even modes, lighter and heavier)
    The sigma-odd eigenvalue equals a EXACTLY for all (p,q,r). -/
```

## Source Excerpt

```lean
theorem three_distinct_eigenvalues (m : SigmaPolarityMatrix) :
    True := trivial
```
