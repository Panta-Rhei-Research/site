---
{
  "projection_kind": "taulib_declaration",
  "title": "zero_is_sigma_fixed",
  "permalink": "/verify/taulib/docs/book-iii-physics-hodge/zero-is-sigma-fixed/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.Hodge`.",
  "declaration_id": "TauLib.BookIII.Physics.Hodge::zero_is_sigma_fixed",
  "declaration_slug": "zero-is-sigma-fixed",
  "kind": "theorem",
  "name": "zero_is_sigma_fixed",
  "module_name": "TauLib.BookIII.Physics.Hodge",
  "module_url": "/verify/taulib/docs/book-iii-physics-hodge/",
  "source_line_start": 277,
  "source_line_end": 278,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L277-L278",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L277-L278",
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
- Source path: [`TauLib/BookIII/Physics/Hodge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L277-L278)
- Source range: L277-L278
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D47` — σ-Fixed Character

## Immediate Comment / Docstring

```lean
/-- [III.D47] Structural: zero BNF is always σ-fixed. -/
```

## Source Excerpt

```lean
theorem zero_is_sigma_fixed :
    is_sigma_fixed ⟨0, 0, 0, 3⟩ = true := rfl
```
