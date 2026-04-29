---
{
  "projection_kind": "taulib_declaration",
  "title": "sigma_fixed_swap_id",
  "permalink": "/verify/taulib/docs/book-iii-physics-hodge/sigma-fixed-swap-id/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.Hodge`.",
  "declaration_id": "TauLib.BookIII.Physics.Hodge::sigma_fixed_swap_id",
  "declaration_slug": "sigma-fixed-swap-id",
  "kind": "theorem",
  "name": "sigma_fixed_swap_id",
  "module_name": "TauLib.BookIII.Physics.Hodge",
  "module_url": "/verify/taulib/docs/book-iii-physics-hodge/",
  "source_line_start": 281,
  "source_line_end": 283,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L281-L283",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L281-L283",
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

- Module: [TauLib.BookIII.Physics.Hodge](/verify/taulib/docs/book-iii-physics-hodge/)
- Source path: [`TauLib/BookIII/Physics/Hodge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L281-L283)
- Source range: L281-L283
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D47` — σ-Fixed Character

## Immediate Comment / Docstring

```lean
/-- [III.D47] Structural: polarity swap of σ-fixed is identity. -/
```

## Source Excerpt

```lean
theorem sigma_fixed_swap_id (nf : BoundaryNF) (h : nf.b_part = nf.c_part) :
    polarity_swap nf = nf := by
  cases nf; simp_all [polarity_swap]
```
