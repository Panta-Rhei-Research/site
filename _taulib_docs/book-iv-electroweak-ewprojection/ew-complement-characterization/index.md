---
{
  "projection_kind": "taulib_declaration",
  "title": "ew_complement_characterization",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewprojection/ew-complement-characterization/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.EWProjection`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWProjection::ew_complement_characterization",
  "declaration_slug": "ew-complement-characterization",
  "kind": "theorem",
  "name": "ew_complement_characterization",
  "module_name": "TauLib.BookIV.Electroweak.EWProjection",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/",
  "source_line_start": 146,
  "source_line_end": 154,
  "registry_ids": [
    "IV.P182"
  ],
  "related_registry_items": [
    {
      "id": "IV.P182",
      "title": "Complement Characterization",
      "url": "/registry/object/IV.P182/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L146-L154",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWProjection",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L146-L154",
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

- Module: [TauLib.BookIV.Electroweak.EWProjection](/verify/taulib/docs/book-iv-electroweak-ewprojection/)
- Source path: [`TauLib/BookIV/Electroweak/EWProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L146-L154)
- Source range: L146-L154
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.P182` — Complement Characterization

## Immediate Comment / Docstring

```lean
/-- [IV.P182] The 7 complement modes are exactly α×3 + π×crossing(Z⁰) + ω×3.
    Physical interpretation: gravity (3) + neutral weak (1) + Higgs (3). -/
```

## Source Excerpt

```lean
theorem ew_complement_characterization :
    isEWComplement ⟨.alpha, .lobePos⟩ = true ∧
    isEWComplement ⟨.alpha, .lobeNeg⟩ = true ∧
    isEWComplement ⟨.alpha, .crossing⟩ = true ∧
    isEWComplement ⟨.pi_, .crossing⟩ = true ∧
    isEWComplement ⟨.omega, .lobePos⟩ = true ∧
    isEWComplement ⟨.omega, .lobeNeg⟩ = true ∧
    isEWComplement ⟨.omega, .crossing⟩ = true := by
  exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
```
