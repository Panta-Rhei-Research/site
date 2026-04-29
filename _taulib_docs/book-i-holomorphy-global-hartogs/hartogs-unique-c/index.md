---
{
  "projection_kind": "taulib_declaration",
  "title": "hartogs_unique_c",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-global-hartogs/hartogs-unique-c/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.GlobalHartogs`.",
  "declaration_id": "TauLib.BookI.Holomorphy.GlobalHartogs::hartogs_unique_c",
  "declaration_slug": "hartogs-unique-c",
  "kind": "theorem",
  "name": "hartogs_unique_c",
  "module_name": "TauLib.BookI.Holomorphy.GlobalHartogs",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-global-hartogs/",
  "source_line_start": 77,
  "source_line_end": 79,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L77-L79",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.GlobalHartogs",
        "url": "/verify/taulib/docs/book-i-holomorphy-global-hartogs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L77-L79",
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

- Module: [TauLib.BookI.Holomorphy.GlobalHartogs](/verify/taulib/docs/book-i-holomorphy-global-hartogs/)
- Source path: [`TauLib/BookI/Holomorphy/GlobalHartogs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L77-L79)
- Source range: L77-L79
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Hartogs uniqueness for C-sector: extension is unique. -/
```

## Source Excerpt

```lean
theorem hartogs_unique_c (hd : HartogsData) :
    ∀ n k, k ≤ hd.depth → hd.f₁.c_fun n k = hd.f₂.c_fun n k :=
  fun n k hk => (global_hartogs hd n k hk).2
```
