---
{
  "projection_kind": "taulib_declaration",
  "title": "E6_abs_numer",
  "permalink": "/verify/taulib/docs/book-iii-spectral-modular-forms/e6-abs-numer/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.ModularForms`.",
  "declaration_id": "TauLib.BookIII.Spectral.ModularForms::E6_abs_numer",
  "declaration_slug": "e6-abs-numer",
  "kind": "def",
  "name": "E6_abs_numer",
  "module_name": "TauLib.BookIII.Spectral.ModularForms",
  "module_url": "/verify/taulib/docs/book-iii-spectral-modular-forms/",
  "source_line_start": 77,
  "source_line_end": 77,
  "registry_ids": [
    "III.D81"
  ],
  "related_registry_items": [
    {
      "id": "III.D81",
      "title": "Spectral Projector",
      "url": "/registry/object/III.D81/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L77-L77",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L77-L77",
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
- Source path: [`TauLib/BookIII/Spectral/ModularForms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L77-L77)
- Source range: L77-L77
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D81` — Spectral Projector

## Immediate Comment / Docstring

```lean
/-- [III.D81] Rational approximation of |E₆(iι_τ)|.
    E₆(iι_τ) = −632.62695677... We store the absolute value:
    |E₆(iι_τ)| ≈ 6326270/10000 (7 significant figures).

    Note: E₆(iι_τ) is NEGATIVE (weight-6, q-expansion has −504 coefficient). -/
```

## Source Excerpt

```lean
def E6_abs_numer : Nat := 6326270
```
