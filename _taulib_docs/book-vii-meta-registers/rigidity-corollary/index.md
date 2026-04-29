---
{
  "projection_kind": "taulib_declaration",
  "title": "rigidity_corollary",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/rigidity-corollary/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::rigidity_corollary",
  "declaration_slug": "rigidity-corollary",
  "kind": "theorem",
  "name": "rigidity_corollary",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 409,
  "source_line_end": 413,
  "registry_ids": [
    "VII.T04"
  ],
  "related_registry_items": [
    {
      "id": "VII.T04",
      "title": "Rigidity Corollary",
      "url": "/registry/object/VII.T04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L409-L413",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L409-L413",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L409-L413)
- Source range: L409-L413
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T04` — Rigidity Corollary

## Immediate Comment / Docstring

```lean
/-- [VII.T04] Rigidity: each sector internally consistent; normaliser is rigid
    w.r.t. sector structure; re-typing content between sectors changes verdict.
    If c ∈ S_X \ S_L, then no w′ ∈ Wit_Y(c) with N_Y(c,w′) = accept for Y ≠ X. -/
```

## Source Excerpt

```lean
theorem rigidity_corollary :
    canonical_sector_decomp.sector_count = 5 ∧
    sector_logos.dc_coincidence = true ∧
    sector_logos.unique_mediator = true :=
  ⟨rfl, rfl, rfl⟩
```
