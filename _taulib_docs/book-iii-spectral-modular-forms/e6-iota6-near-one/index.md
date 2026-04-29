---
{
  "projection_kind": "taulib_declaration",
  "title": "E6_iota6_near_one",
  "permalink": "/verify/taulib/docs/book-iii-spectral-modular-forms/e6-iota6-near-one/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.ModularForms`.",
  "declaration_id": "TauLib.BookIII.Spectral.ModularForms::E6_iota6_near_one",
  "declaration_slug": "e6-iota6-near-one",
  "kind": "theorem",
  "name": "E6_iota6_near_one",
  "module_name": "TauLib.BookIII.Spectral.ModularForms",
  "module_url": "/verify/taulib/docs/book-iii-spectral-modular-forms/",
  "source_line_start": 154,
  "source_line_end": 157,
  "registry_ids": [
    "III.T51"
  ],
  "related_registry_items": [
    {
      "id": "III.T51",
      "title": "Physical Admissibility Theorem",
      "url": "/registry/object/III.T51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L154-L157",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L154-L157",
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
- Source path: [`TauLib/BookIII/Spectral/ModularForms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L154-L157)
- Source range: L154-L157
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T51` — Physical Admissibility Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T51] Combined: |E₆|·ι_τ⁶ ∈ (0.999990, 1.000010), i.e., −1 ± ~10 ppm.
    (The true value is 1 − 5.1 ppm; the rational approximation widens to ±10 ppm.) -/
```

## Source Excerpt

```lean
theorem E6_iota6_near_one :
    E6_abs_numer * i6N * 1000000 > 999990 * E6_abs_denom * i6D ∧
    E6_abs_numer * i6N * 1000000 < 1000010 * E6_abs_denom * i6D :=
  ⟨E6_iota6_near_one_lower, E6_iota6_near_one_upper⟩
```
