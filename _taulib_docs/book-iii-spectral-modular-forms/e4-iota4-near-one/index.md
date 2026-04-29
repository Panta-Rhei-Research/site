---
{
  "projection_kind": "taulib_declaration",
  "title": "E4_iota4_near_one",
  "permalink": "/verify/taulib/docs/book-iii-spectral-modular-forms/e4-iota4-near-one/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.ModularForms`.",
  "declaration_id": "TauLib.BookIII.Spectral.ModularForms::E4_iota4_near_one",
  "declaration_slug": "e4-iota4-near-one",
  "kind": "theorem",
  "name": "E4_iota4_near_one",
  "module_name": "TauLib.BookIII.Spectral.ModularForms",
  "module_url": "/verify/taulib/docs/book-iii-spectral-modular-forms/",
  "source_line_start": 128,
  "source_line_end": 131,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L128-L131",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L128-L131",
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
- Source path: [`TauLib/BookIII/Spectral/ModularForms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L128-L131)
- Source range: L128-L131
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T50` — Global Cartesian Gluing Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T50] Combined: E₄·ι_τ⁴ ∈ (0.999990, 1.000010), i.e., 1 ± ~10 ppm.
    (The true value is 1 + 2.4 ppm; the rational approximation widens to ±10 ppm.) -/
```

## Source Excerpt

```lean
theorem E4_iota4_near_one :
    E4_numer * i4N * 1000000 > 999990 * E4_denom * i4D ∧
    E4_numer * i4N * 1000000 < 1000010 * E4_denom * i4D :=
  ⟨E4_iota4_near_one_lower, E4_iota4_near_one_upper⟩
```
