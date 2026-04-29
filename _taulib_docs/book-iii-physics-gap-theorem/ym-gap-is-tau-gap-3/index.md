---
{
  "projection_kind": "taulib_declaration",
  "title": "ym_gap_is_tau_gap_3",
  "permalink": "/verify/taulib/docs/book-iii-physics-gap-theorem/ym-gap-is-tau-gap-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Physics.GapTheorem`.",
  "declaration_id": "TauLib.BookIII.Physics.GapTheorem::ym_gap_is_tau_gap_3",
  "declaration_slug": "ym-gap-is-tau-gap-3",
  "kind": "theorem",
  "name": "ym_gap_is_tau_gap_3",
  "module_name": "TauLib.BookIII.Physics.GapTheorem",
  "module_url": "/verify/taulib/docs/book-iii-physics-gap-theorem/",
  "source_line_start": 241,
  "source_line_end": 242,
  "registry_ids": [
    "III.T27"
  ],
  "related_registry_items": [
    {
      "id": "III.T27",
      "title": "Yang-Mills Gap Theorem",
      "url": "/registry/object/III.T27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L241-L242",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L241-L242",
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
- Source path: [`TauLib/BookIII/Physics/GapTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L241-L242)
- Source range: L241-L242
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T27` — Yang-Mills Gap Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T27] Structural: YM gap at depth 3 coincides with τ-gap. -/
```

## Source Excerpt

```lean
theorem ym_gap_is_tau_gap_3 :
    gap_constant 3 = tau_gap_at_level 3 := rfl
```
