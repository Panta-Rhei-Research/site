---
{
  "projection_kind": "taulib_declaration",
  "title": "tetration_exceeds_primorial",
  "permalink": "/corpus/taulib/docs/book-i-denotation-growth-escape/tetration-exceeds-primorial/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.GrowthEscape`.",
  "declaration_id": "TauLib.BookI.Denotation.GrowthEscape::tetration_exceeds_primorial",
  "declaration_slug": "tetration-exceeds-primorial",
  "kind": "theorem",
  "name": "tetration_exceeds_primorial",
  "module_name": "TauLib.BookI.Denotation.GrowthEscape",
  "module_url": "/corpus/taulib/docs/book-i-denotation-growth-escape/",
  "source_line_start": 38,
  "source_line_end": 40,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L38-L40",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.GrowthEscape",
        "url": "/corpus/taulib/docs/book-i-denotation-growth-escape/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L38-L40",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Denotation.GrowthEscape](/corpus/taulib/docs/book-i-denotation-growth-escape/)
- Source path: [`TauLib/BookI/Denotation/GrowthEscape.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L38-L40)
- Source range: L38-L40
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- For any primorial depth d, tetration 2 eventually exceeds primorial d. -/
```

## Source Excerpt

```lean
theorem tetration_exceeds_primorial (d : TauIdx) :
    ∃ c, tetration 2 c > primorial d :=
  tetration_unbounded 2 (by omega) (primorial d)
```
