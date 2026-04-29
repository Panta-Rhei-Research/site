---
{
  "projection_kind": "taulib_declaration",
  "title": "gap_pos_3",
  "permalink": "/verify/taulib/docs/book-iii-physics-gap-theorem/gap-pos-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.GapTheorem`.",
  "declaration_id": "TauLib.BookIII.Physics.GapTheorem::gap_pos_3",
  "declaration_slug": "gap-pos-3",
  "kind": "theorem",
  "name": "gap_pos_3",
  "module_name": "TauLib.BookIII.Physics.GapTheorem",
  "module_url": "/verify/taulib/docs/book-iii-physics-gap-theorem/",
  "source_line_start": 229,
  "source_line_end": 230,
  "registry_ids": [
    "III.T26"
  ],
  "related_registry_items": [
    {
      "id": "III.T26",
      "title": "τ-Gap Meta-Theorem",
      "url": "/registry/object/III.T26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L229-L230",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L229-L230",
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
- Source path: [`TauLib/BookIII/Physics/GapTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L229-L230)
- Source range: L229-L230
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T26` — τ-Gap Meta-Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T26] Structural: gap at depth 3 is positive. -/
```

## Source Excerpt

```lean
theorem gap_pos_3 :
    tau_gap_at_level 3 > 0 := by native_decide
```
