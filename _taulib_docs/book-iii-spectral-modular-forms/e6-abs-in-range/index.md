---
{
  "projection_kind": "taulib_declaration",
  "title": "E6_abs_in_range",
  "permalink": "/verify/taulib/docs/book-iii-spectral-modular-forms/e6-abs-in-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.ModularForms`.",
  "declaration_id": "TauLib.BookIII.Spectral.ModularForms::E6_abs_in_range",
  "declaration_slug": "e6-abs-in-range",
  "kind": "theorem",
  "name": "E6_abs_in_range",
  "module_name": "TauLib.BookIII.Spectral.ModularForms",
  "module_url": "/verify/taulib/docs/book-iii-spectral-modular-forms/",
  "source_line_start": 138,
  "source_line_end": 144,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L138-L144",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L138-L144",
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
- Source path: [`TauLib/BookIII/Spectral/ModularForms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L138-L144)
- Source range: L138-L144
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T51` — Physical Admissibility Theorem

## Immediate Comment / Docstring

```lean
/-- |E₆(iι_τ)| is between 632 and 633. -/
```

## Source Excerpt

```lean
theorem E6_abs_in_range :
    E6_abs_numer > 632 * E6_abs_denom ∧ E6_abs_numer < 633 * E6_abs_denom := by
  constructor <;> simp [E6_abs_numer, E6_abs_denom]

/-- [III.T51] |E₆|·ι_τ⁶ near-identity. -/
abbrev i6N : Nat := iota_sixth_numer
abbrev i6D : Nat := iota_sixth_denom
```
