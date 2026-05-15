---
{
  "projection_kind": "taulib_declaration",
  "title": "kappa_unique",
  "permalink": "/corpus/taulib/docs/book-v-gravity-einstein-equation/kappa-unique/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Gravity.EinsteinEquation`.",
  "declaration_id": "TauLib.BookV.Gravity.EinsteinEquation::kappa_unique",
  "declaration_slug": "kappa-unique",
  "kind": "theorem",
  "name": "kappa_unique",
  "module_name": "TauLib.BookV.Gravity.EinsteinEquation",
  "module_url": "/corpus/taulib/docs/book-v-gravity-einstein-equation/",
  "source_line_start": 234,
  "source_line_end": 235,
  "registry_ids": [
    "V.T02"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L234-L235",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.EinsteinEquation",
        "url": "/corpus/taulib/docs/book-v-gravity-einstein-equation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L234-L235",
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

- Module: [TauLib.BookV.Gravity.EinsteinEquation](/corpus/taulib/docs/book-v-gravity-einstein-equation/)
- Source path: [`TauLib/BookV/Gravity/EinsteinEquation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/EinsteinEquation.lean#L234-L235)
- Source range: L234-L235
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.T02] κ_τ is unique: encoded as a field constraint.
    Any GRCoupling with is_unique = true satisfies uniqueness. -/
```

## Source Excerpt

```lean
theorem kappa_unique (g : GRCoupling) (h : g.is_unique = true) :
    g.is_unique = true := h
```
