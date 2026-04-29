---
{
  "projection_kind": "taulib_declaration",
  "title": "full_basis_3_20",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/full-basis-3-20/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Hartogs.CanonicalBasis`.",
  "declaration_id": "TauLib.BookII.Hartogs.CanonicalBasis::full_basis_3_20",
  "declaration_slug": "full-basis-3-20",
  "kind": "theorem",
  "name": "full_basis_3_20",
  "module_name": "TauLib.BookII.Hartogs.CanonicalBasis",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/",
  "source_line_start": 419,
  "source_line_end": 422,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L419-L422",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CanonicalBasis",
        "url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L419-L422",
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

- Module: [TauLib.BookII.Hartogs.CanonicalBasis](/verify/taulib/docs/book-ii-hartogs-canonical-basis/)
- Source path: [`TauLib/BookII/Hartogs/CanonicalBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L419-L422)
- Source range: L419-L422
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Full canonical basis check
```

## Source Excerpt

```lean
theorem full_basis_3_20 :
    full_canonical_basis_check 3 20 = true := by native_decide

end Tau.BookII.Hartogs
```
