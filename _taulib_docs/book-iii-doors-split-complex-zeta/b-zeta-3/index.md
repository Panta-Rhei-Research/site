---
{
  "projection_kind": "taulib_declaration",
  "title": "b_zeta_3",
  "permalink": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/b-zeta-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.SplitComplexZeta`.",
  "declaration_id": "TauLib.BookIII.Doors.SplitComplexZeta::b_zeta_3",
  "declaration_slug": "b-zeta-3",
  "kind": "theorem",
  "name": "b_zeta_3",
  "module_name": "TauLib.BookIII.Doors.SplitComplexZeta",
  "module_url": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/",
  "source_line_start": 182,
  "source_line_end": 182,
  "registry_ids": [
    "III.D26"
  ],
  "related_registry_items": [
    {
      "id": "III.D26",
      "title": "Split-Complex Zeta ζ_τ",
      "url": "/registry/object/III.D26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L182-L182",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SplitComplexZeta",
        "url": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L182-L182",
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

- Module: [TauLib.BookIII.Doors.SplitComplexZeta](/verify/taulib/docs/book-iii-doors-split-complex-zeta/)
- Source path: [`TauLib/BookIII/Doors/SplitComplexZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L182-L182)
- Source range: L182-L182
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D26` — Split-Complex Zeta ζ_τ

## Immediate Comment / Docstring

```lean
/-- [III.D26] Structural: B-zeta at depth 3 = 5 (only B-type prime ≤ p₃). -/
```

## Source Excerpt

```lean
theorem b_zeta_3 : split_zeta_b 3 = 5 := by native_decide
```
