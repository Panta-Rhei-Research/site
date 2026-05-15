---
{
  "projection_kind": "taulib_declaration",
  "title": "ia_sn_products",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-supernovae/ia-sn-products/",
  "summary_short": "`def` declaration in `TauLib.BookV.Astrophysics.Supernovae`.",
  "declaration_id": "TauLib.BookV.Astrophysics.Supernovae::ia_sn_products",
  "declaration_slug": "ia-sn-products",
  "kind": "def",
  "name": "ia_sn_products",
  "module_name": "TauLib.BookV.Astrophysics.Supernovae",
  "module_url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/",
  "source_line_start": 218,
  "source_line_end": 221,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L218-L221",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.Supernovae",
        "url": "/corpus/taulib/docs/book-v-astrophysics-supernovae/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L218-L221",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookV.Astrophysics.Supernovae](/corpus/taulib/docs/book-v-astrophysics-supernovae/)
- Source path: [`TauLib/BookV/Astrophysics/Supernovae.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L218-L221)
- Source range: L218-L221
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Type Ia SNe mainly produce iron-peak elements. -/
```

## Source Excerpt

```lean
def ia_sn_products : NucleosynthesisProducts where
  sn_type := .TypeIa
  primary_products := [.IronPeak]
  products_nonempty := by native_decide
```
