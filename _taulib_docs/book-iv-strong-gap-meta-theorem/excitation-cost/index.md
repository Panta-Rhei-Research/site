---
{
  "projection_kind": "taulib_declaration",
  "title": "ExcitationCost",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/excitation-cost/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::ExcitationCost",
  "declaration_slug": "excitation-cost",
  "kind": "structure",
  "name": "ExcitationCost",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 143,
  "source_line_end": 150,
  "registry_ids": [
    "IV.D166"
  ],
  "related_registry_items": [
    {
      "id": "IV.D166",
      "title": "Excitation cost",
      "url": "/registry/object/IV.D166/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L143-L150",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.GapMetaTheorem",
        "url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L143-L150",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Strong.GapMetaTheorem](/verify/taulib/docs/book-iv-strong-gap-meta-theorem/)
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L143-L150)
- Source range: L143-L150
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D166` — Excitation cost

## Immediate Comment / Docstring

```lean
/-- [IV.D166] Excitation cost lambda_n(p) := (Q_n(p,p), ||p||_n),
    the lexicographic pair of quadratic energy cost and NF-norm. -/
```

## Source Excerpt

```lean
structure ExcitationCost where
  /-- Quadratic component Q_n(p,p). -/
  quadratic_component : Bool := true
  /-- NF-norm component. -/
  nf_norm_component : Bool := true
  /-- Lexicographic ordering. -/
  lexicographic : Bool := true
  deriving Repr
```
