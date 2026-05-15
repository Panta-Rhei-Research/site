---
{
  "projection_kind": "taulib_declaration",
  "title": "bhs_matches_closing",
  "permalink": "/corpus/taulib/docs/book-v-gravity-field-bipolar-holonomy/bhs-matches-closing/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.BipolarHolonomy`.",
  "declaration_id": "TauLib.BookV.GravityField.BipolarHolonomy::bhs_matches_closing",
  "declaration_slug": "bhs-matches-closing",
  "kind": "theorem",
  "name": "bhs_matches_closing",
  "module_name": "TauLib.BookV.GravityField.BipolarHolonomy",
  "module_url": "/corpus/taulib/docs/book-v-gravity-field-bipolar-holonomy/",
  "source_line_start": 125,
  "source_line_end": 126,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L125-L126",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.BipolarHolonomy",
        "url": "/corpus/taulib/docs/book-v-gravity-field-bipolar-holonomy/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L125-L126",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookV.GravityField.BipolarHolonomy](/corpus/taulib/docs/book-v-gravity-field-bipolar-holonomy/)
- Source path: [`TauLib/BookV/GravityField/BipolarHolonomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/BipolarHolonomy.lean#L125-L126)
- Source range: L125-L126
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The BHS dimension matches the closing identity alpha exponent. -/
```

## Source Excerpt

```lean
theorem bhs_matches_closing :
    canonical_bhs.dim = closing_identity_canonical.alpha_exponent := by rfl
```
