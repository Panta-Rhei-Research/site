---
{
  "projection_kind": "taulib_declaration",
  "title": "mod_ne_of_gt",
  "permalink": "/verify/taulib/docs/book-i-denotation-growth-escape/mod-ne-of-gt/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.GrowthEscape`.",
  "declaration_id": "TauLib.BookI.Denotation.GrowthEscape::mod_ne_of_gt",
  "declaration_slug": "mod-ne-of-gt",
  "kind": "theorem",
  "name": "mod_ne_of_gt",
  "module_name": "TauLib.BookI.Denotation.GrowthEscape",
  "module_url": "/verify/taulib/docs/book-i-denotation-growth-escape/",
  "source_line_start": 47,
  "source_line_end": 51,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L47-L51",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.GrowthEscape",
        "url": "/verify/taulib/docs/book-i-denotation-growth-escape/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L47-L51",
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

- Module: [TauLib.BookI.Denotation.GrowthEscape](/verify/taulib/docs/book-i-denotation-growth-escape/)
- Source path: [`TauLib/BookI/Denotation/GrowthEscape.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L47-L51)
- Source range: L47-L51
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: a % m ≠ a when a > m and m > 0. -/
```

## Source Excerpt

```lean
private theorem mod_ne_of_gt {a m : Nat} (ha : a > m) (hm : m > 0) :
    a % m ≠ a := by
  intro h
  have := Nat.mod_lt a hm
  omega
```
