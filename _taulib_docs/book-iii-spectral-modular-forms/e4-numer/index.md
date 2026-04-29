---
{
  "projection_kind": "taulib_declaration",
  "title": "E4_numer",
  "permalink": "/verify/taulib/docs/book-iii-spectral-modular-forms/e4-numer/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.ModularForms`.",
  "declaration_id": "TauLib.BookIII.Spectral.ModularForms::E4_numer",
  "declaration_slug": "e4-numer",
  "kind": "def",
  "name": "E4_numer",
  "module_name": "TauLib.BookIII.Spectral.ModularForms",
  "module_url": "/verify/taulib/docs/book-iii-spectral-modular-forms/",
  "source_line_start": 59,
  "source_line_end": 59,
  "registry_ids": [
    "III.D80"
  ],
  "related_registry_items": [
    {
      "id": "III.D80",
      "title": "q-Expansion Coefficients",
      "url": "/registry/object/III.D80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L59-L59",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L59-L59",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookIII/Spectral/ModularForms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L59-L59)
- Source range: L59-L59
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D80` — q-Expansion Coefficients

## Immediate Comment / Docstring

```lean
/-- [III.D80] Rational approximation of E₄(iι_τ).
    E₄(iι_τ) = 73.69437260... ≈ 7369437/100000 (7 significant figures).

    Computed via q-expansion with 300 terms at 50-digit precision. -/
```

## Source Excerpt

```lean
def E4_numer : Nat := 7369437
```
