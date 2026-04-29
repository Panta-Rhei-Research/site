---
{
  "projection_kind": "taulib_declaration",
  "title": "algebraic_lemniscate_exists",
  "permalink": "/verify/taulib/docs/book-i-polarity-lemniscate/algebraic-lemniscate-exists/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.Lemniscate`.",
  "declaration_id": "TauLib.BookI.Polarity.Lemniscate::algebraic_lemniscate_exists",
  "declaration_slug": "algebraic-lemniscate-exists",
  "kind": "theorem",
  "name": "algebraic_lemniscate_exists",
  "module_name": "TauLib.BookI.Polarity.Lemniscate",
  "module_url": "/verify/taulib/docs/book-i-polarity-lemniscate/",
  "source_line_start": 75,
  "source_line_end": 76,
  "registry_ids": [
    "I.D18"
  ],
  "related_registry_items": [
    {
      "id": "I.D18",
      "title": "Algebraic Lemniscate",
      "url": "/registry/object/I.D18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L75-L76",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.Lemniscate",
        "url": "/verify/taulib/docs/book-i-polarity-lemniscate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L75-L76",
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

- Module: [TauLib.BookI.Polarity.Lemniscate](/verify/taulib/docs/book-i-polarity-lemniscate/)
- Source path: [`TauLib/BookI/Polarity/Lemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L75-L76)
- Source range: L75-L76
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.D18` — Algebraic Lemniscate

## Immediate Comment / Docstring

```lean
/-- [I.D18] The algebraic lemniscate exists. -/
```

## Source Excerpt

```lean
theorem algebraic_lemniscate_exists : Nonempty AlgebraicLemniscate :=
  ⟨canonical_lemniscate⟩
```
