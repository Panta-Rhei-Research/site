---
{
  "projection_kind": "taulib_declaration",
  "title": "readout_preserves_identities",
  "permalink": "/verify/taulib/docs/book-iv-physics-readout-functor/readout-preserves-identities/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.ReadoutFunctor`.",
  "declaration_id": "TauLib.BookIV.Physics.ReadoutFunctor::readout_preserves_identities",
  "declaration_slug": "readout-preserves-identities",
  "kind": "theorem",
  "name": "readout_preserves_identities",
  "module_name": "TauLib.BookIV.Physics.ReadoutFunctor",
  "module_url": "/verify/taulib/docs/book-iv-physics-readout-functor/",
  "source_line_start": 219,
  "source_line_end": 220,
  "registry_ids": [
    "IV.T128"
  ],
  "related_registry_items": [
    {
      "id": "IV.T128",
      "title": "Readout Preserves Identities",
      "url": "/registry/object/IV.T128/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L219-L220",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.ReadoutFunctor",
        "url": "/verify/taulib/docs/book-iv-physics-readout-functor/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L219-L220",
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

- Module: [TauLib.BookIV.Physics.ReadoutFunctor](/verify/taulib/docs/book-iv-physics-readout-functor/)
- Source path: [`TauLib/BookIV/Physics/ReadoutFunctor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/ReadoutFunctor.lean#L219-L220)
- Source range: L219-L220
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T128` — Readout Preserves Identities

## Immediate Comment / Docstring

```lean
/-- [IV.T128] The readout functor preserves internal identities:
    if two Layer 1 objects are equal (as internal morphisms),
    their R_μ images yield equal SI numbers. -/
```

## Source Excerpt

```lean
theorem readout_preserves_identities :
    readout.preserves_identities = true := rfl
```
