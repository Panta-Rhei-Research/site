---
{
  "projection_kind": "taulib_declaration",
  "title": "E4_iota4_near_one_lower",
  "permalink": "/verify/taulib/docs/book-iii-spectral-modular-forms/e4-iota4-near-one-lower/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.ModularForms`.",
  "declaration_id": "TauLib.BookIII.Spectral.ModularForms::E4_iota4_near_one_lower",
  "declaration_slug": "e4-iota4-near-one-lower",
  "kind": "theorem",
  "name": "E4_iota4_near_one_lower",
  "module_name": "TauLib.BookIII.Spectral.ModularForms",
  "module_url": "/verify/taulib/docs/book-iii-spectral-modular-forms/",
  "source_line_start": 120,
  "source_line_end": 121,
  "registry_ids": [
    "III.T50"
  ],
  "related_registry_items": [
    {
      "id": "III.T50",
      "title": "Global Cartesian Gluing Theorem",
      "url": "/registry/object/III.T50/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L120-L121",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.ModularForms",
        "url": "/verify/taulib/docs/book-iii-spectral-modular-forms/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L120-L121",
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

- Module: [TauLib.BookIII.Spectral.ModularForms](/verify/taulib/docs/book-iii-spectral-modular-forms/)
- Source path: [`TauLib/BookIII/Spectral/ModularForms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L120-L121)
- Source range: L120-L121
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T50` — Global Cartesian Gluing Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T50] E₄·ι_τ⁴ near-identity: the product E₄(iι_τ)·ι_τ⁴ is close to 1.

    With 7-digit E₄ and 6-digit ι_τ, the product E₄_numer · i4N / (E₄_denom · i4D)
    is within ~10 ppm of 1. We prove bounds (999990, 1000010) per million.

    Cross-multiplied: 999990 · E4_denom · i4D < E4_numer · i4N · 1000000
    and               E4_numer · i4N · 1000000 < 1000010 · E4_denom · i4D -/
```

## Source Excerpt

```lean
theorem E4_iota4_near_one_lower :
    E4_numer * i4N * 1000000 > 999990 * E4_denom * i4D := by native_decide
```
