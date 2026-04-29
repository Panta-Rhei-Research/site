---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha2_matches",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/alpha2-matches/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.MassDerivation.HolonomyDetail`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.HolonomyDetail::alpha2_matches",
  "declaration_slug": "alpha2-matches",
  "kind": "theorem",
  "name": "alpha2_matches",
  "module_name": "TauLib.BookIV.MassDerivation.HolonomyDetail",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/",
  "source_line_start": 191,
  "source_line_end": 194,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L191-L194",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.MassDerivation.HolonomyDetail",
        "url": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L191-L194",
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

- Module: [TauLib.BookIV.MassDerivation.HolonomyDetail](/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/)
- Source path: [`TauLib/BookIV/MassDerivation/HolonomyDetail.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L191-L194)
- Source range: L191-L194
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- α² component matches the holonomy correction module. -/
```

## Source Excerpt

```lean
theorem alpha2_matches :
    holonomy_detail.alpha2_numer = alpha_sq_numer ∧
    holonomy_detail.alpha2_denom = alpha_sq_denom :=
  ⟨rfl, rfl⟩
```
