---
{
  "projection_kind": "taulib_declaration",
  "title": "diagonal_channel_count",
  "permalink": "/verify/taulib/docs/book-i-kernel-diagonal/diagonal-channel-count/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.Diagonal`.",
  "declaration_id": "TauLib.BookI.Kernel.Diagonal::diagonal_channel_count",
  "declaration_slug": "diagonal-channel-count",
  "kind": "theorem",
  "name": "diagonal_channel_count",
  "module_name": "TauLib.BookI.Kernel.Diagonal",
  "module_url": "/verify/taulib/docs/book-i-kernel-diagonal/",
  "source_line_start": 38,
  "source_line_end": 39,
  "registry_ids": [
    "I.D03"
  ],
  "related_registry_items": [
    {
      "id": "I.D03",
      "title": "Diagonal Discipline",
      "url": "/registry/object/I.D03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L38-L39",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Diagonal",
        "url": "/verify/taulib/docs/book-i-kernel-diagonal/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L38-L39",
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

- Module: [TauLib.BookI.Kernel.Diagonal](/verify/taulib/docs/book-i-kernel-diagonal/)
- Source path: [`TauLib/BookI/Kernel/Diagonal.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Diagonal.lean#L38-L39)
- Source range: L38-L39
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.D03` — Diagonal Discipline

## Immediate Comment / Docstring

```lean
/-- [I.D03] There are exactly 4 non-omega generators.
    This is the source of the diagonal discipline:
    4 generators yield 3 rewiring levels. -/
```

## Source Excerpt

```lean
theorem diagonal_channel_count : nonOmegaGenerators.length = 4 := by
  rfl
```
