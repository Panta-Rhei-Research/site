---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_eq_implies_agree",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/spectral-eq-implies-agree/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.SpectralCoefficients`.",
  "declaration_id": "TauLib.BookI.Holomorphy.SpectralCoefficients::spectral_eq_implies_agree",
  "declaration_slug": "spectral-eq-implies-agree",
  "kind": "theorem",
  "name": "spectral_eq_implies_agree",
  "module_name": "TauLib.BookI.Holomorphy.SpectralCoefficients",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/",
  "source_line_start": 48,
  "source_line_end": 55,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L48-L55",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.SpectralCoefficients",
        "url": "/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L48-L55",
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

- Module: [TauLib.BookI.Holomorphy.SpectralCoefficients](/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/)
- Source path: [`TauLib/BookI/Holomorphy/SpectralCoefficients.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L48-L55)
- Source range: L48-L55
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Two functions with the same spectral coefficients agree at that point. -/
```

## Source Excerpt

```lean
theorem spectral_eq_implies_agree (f₁ f₂ : StageFun) (n k : TauIdx)
    (h : spectral_of f₁ n k = spectral_of f₂ n k) :
    f₁.b_fun n k = f₂.b_fun n k ∧ f₁.c_fun n k = f₂.c_fun n k := by
  have hb : (spectral_of f₁ n k).b_coeff = (spectral_of f₂ n k).b_coeff :=
    congrArg SpectralCoeff.b_coeff h
  have hc : (spectral_of f₁ n k).c_coeff = (spectral_of f₂ n k).c_coeff :=
    congrArg SpectralCoeff.c_coeff h
  exact ⟨hb, hc⟩
```
