---
{
  "projection_kind": "taulib_declaration",
  "title": "is_sigma_fixed",
  "permalink": "/verify/taulib/docs/book-iii-physics-hodge/is-sigma-fixed/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.Hodge`.",
  "declaration_id": "TauLib.BookIII.Physics.Hodge::is_sigma_fixed",
  "declaration_slug": "is-sigma-fixed",
  "kind": "def",
  "name": "is_sigma_fixed",
  "module_name": "TauLib.BookIII.Physics.Hodge",
  "module_url": "/verify/taulib/docs/book-iii-physics-hodge/",
  "source_line_start": 56,
  "source_line_end": 57,
  "registry_ids": [
    "III.D47"
  ],
  "related_registry_items": [
    {
      "id": "III.D47",
      "title": "σ-Fixed Character",
      "url": "/registry/object/III.D47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L56-L57",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.Hodge",
        "url": "/verify/taulib/docs/book-iii-physics-hodge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L56-L57",
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

- Module: [TauLib.BookIII.Physics.Hodge](/verify/taulib/docs/book-iii-physics-hodge/)
- Source path: [`TauLib/BookIII/Physics/Hodge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L56-L57)
- Source range: L56-L57
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D47` — σ-Fixed Character

## Immediate Comment / Docstring

```lean
/-- [III.D47] A BNF is σ-fixed if polarity swap leaves it unchanged:
    b_part = c_part. These are the self-dual elements. -/
```

## Source Excerpt

```lean
def is_sigma_fixed (nf : BoundaryNF) : Bool :=
  nf.b_part == nf.c_part
```
