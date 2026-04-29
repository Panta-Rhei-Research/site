---
{
  "projection_kind": "taulib_declaration",
  "title": "E4_in_range",
  "permalink": "/verify/taulib/docs/book-iii-spectral-modular-forms/e4-in-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.ModularForms`.",
  "declaration_id": "TauLib.BookIII.Spectral.ModularForms::E4_in_range",
  "declaration_slug": "e4-in-range",
  "kind": "theorem",
  "name": "E4_in_range",
  "module_name": "TauLib.BookIII.Spectral.ModularForms",
  "module_url": "/verify/taulib/docs/book-iii-spectral-modular-forms/",
  "source_line_start": 109,
  "source_line_end": 111,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L109-L111",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L109-L111",
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
- Source path: [`TauLib/BookIII/Spectral/ModularForms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ModularForms.lean#L109-L111)
- Source range: L109-L111
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- E₄(iι_τ) is between 73 and 74.
    Since E4_numer = 7369437 and E4_denom = 100000:
    73 * 100000 = 7300000 < 7369437 < 7400000 = 74 * 100000. -/
```

## Source Excerpt

```lean
theorem E4_in_range :
    E4_numer > 73 * E4_denom ∧ E4_numer < 74 * E4_denom := by
  constructor <;> simp [E4_numer, E4_denom]
```
