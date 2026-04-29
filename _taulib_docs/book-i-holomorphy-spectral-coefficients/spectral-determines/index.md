---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_determines",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/spectral-determines/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.SpectralCoefficients`.",
  "declaration_id": "TauLib.BookI.Holomorphy.SpectralCoefficients::spectral_determines",
  "declaration_slug": "spectral-determines",
  "kind": "theorem",
  "name": "spectral_determines",
  "module_name": "TauLib.BookI.Holomorphy.SpectralCoefficients",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-spectral-coefficients/",
  "source_line_start": 92,
  "source_line_end": 99,
  "registry_ids": [
    "I.T29"
  ],
  "related_registry_items": [
    {
      "id": "I.T29",
      "title": "Spectral Determination",
      "url": "/registry/object/I.T29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L92-L99",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L92-L99",
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
- Source path: [`TauLib/BookI/Holomorphy/SpectralCoefficients.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/SpectralCoefficients.lean#L92-L99)
- Source range: L92-L99
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T29` — Spectral Determination

## Immediate Comment / Docstring

```lean
/-- [I.T29] Spectral Determination: if two tower-coherent StageFuns
    have the same spectral coefficients at all inputs and stages,
    they are equal.

    This is essentially the content of the Identity Theorem (I.T21)
    reformulated in spectral language. -/
```

## Source Excerpt

```lean
theorem spectral_determines (f₁ f₂ : StageFun)
    (h : ∀ n k, spectral_of f₁ n k = spectral_of f₂ n k) :
    f₁ = f₂ := by
  cases f₁; cases f₂
  simp only [StageFun.mk.injEq]
  constructor <;> funext n k
  · exact (spectral_eq_implies_agree _ _ n k (h n k)).1
  · exact (spectral_eq_implies_agree _ _ n k (h n k)).2
```
