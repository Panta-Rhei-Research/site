---
{
  "projection_kind": "taulib_declaration",
  "title": "pi3_matches",
  "permalink": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/pi3-matches/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.MassDerivation.HolonomyDetail`.",
  "declaration_id": "TauLib.BookIV.MassDerivation.HolonomyDetail::pi3_matches",
  "declaration_slug": "pi3-matches",
  "kind": "theorem",
  "name": "pi3_matches",
  "module_name": "TauLib.BookIV.MassDerivation.HolonomyDetail",
  "module_url": "/verify/taulib/docs/book-iv-mass-derivation-holonomy-detail/",
  "source_line_start": 185,
  "source_line_end": 188,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L185-L188",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L185-L188",
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
- Source path: [`TauLib/BookIV/MassDerivation/HolonomyDetail.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/MassDerivation/HolonomyDetail.lean#L185-L188)
- Source range: L185-L188
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- π³ component matches the holonomy correction module. -/
```

## Source Excerpt

```lean
theorem pi3_matches :
    holonomy_detail.pi3_numer = pi_cubed_numer ∧
    holonomy_detail.pi3_denom = pi_cubed_denom :=
  ⟨rfl, rfl⟩
```
