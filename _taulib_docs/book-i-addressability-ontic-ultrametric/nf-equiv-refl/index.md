---
{
  "projection_kind": "taulib_declaration",
  "title": "nfEquiv_refl",
  "permalink": "/verify/taulib/docs/book-i-addressability-ontic-ultrametric/nf-equiv-refl/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.OnticUltrametric`.",
  "declaration_id": "TauLib.BookI.Addressability.OnticUltrametric::nfEquiv_refl",
  "declaration_slug": "nf-equiv-refl",
  "kind": "theorem",
  "name": "nfEquiv_refl",
  "module_name": "TauLib.BookI.Addressability.OnticUltrametric",
  "module_url": "/verify/taulib/docs/book-i-addressability-ontic-ultrametric/",
  "source_line_start": 92,
  "source_line_end": 93,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L92-L93",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.OnticUltrametric",
        "url": "/verify/taulib/docs/book-i-addressability-ontic-ultrametric/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L92-L93",
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

- Module: [TauLib.BookI.Addressability.OnticUltrametric](/verify/taulib/docs/book-i-addressability-ontic-ultrametric/)
- Source path: [`TauLib/BookI/Addressability/OnticUltrametric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L92-L93)
- Source range: L92-L93
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem nfEquiv_refl (nf : NormalForm) : nfEquiv nf nf :=
  ⟨rfl, seedAgree_refl _⟩
```
