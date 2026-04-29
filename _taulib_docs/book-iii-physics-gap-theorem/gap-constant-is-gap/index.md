---
{
  "projection_kind": "taulib_declaration",
  "title": "gap_constant_is_gap",
  "permalink": "/verify/taulib/docs/book-iii-physics-gap-theorem/gap-constant-is-gap/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.GapTheorem`.",
  "declaration_id": "TauLib.BookIII.Physics.GapTheorem::gap_constant_is_gap",
  "declaration_slug": "gap-constant-is-gap",
  "kind": "theorem",
  "name": "gap_constant_is_gap",
  "module_name": "TauLib.BookIII.Physics.GapTheorem",
  "module_url": "/verify/taulib/docs/book-iii-physics-gap-theorem/",
  "source_line_start": 237,
  "source_line_end": 238,
  "registry_ids": [
    "III.D45"
  ],
  "related_registry_items": [
    {
      "id": "III.D45",
      "title": "Gap Constant Γ*",
      "url": "/registry/object/III.D45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L237-L238",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.GapTheorem",
        "url": "/verify/taulib/docs/book-iii-physics-gap-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L237-L238",
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

- Module: [TauLib.BookIII.Physics.GapTheorem](/verify/taulib/docs/book-iii-physics-gap-theorem/)
- Source path: [`TauLib/BookIII/Physics/GapTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L237-L238)
- Source range: L237-L238
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D45` — Gap Constant Γ*

## Immediate Comment / Docstring

```lean
/-- [III.D45] Structural: gap constant equals tau_gap_at_level. -/
```

## Source Excerpt

```lean
theorem gap_constant_is_gap (k : TauIdx) :
    gap_constant k = tau_gap_at_level k := rfl
```
