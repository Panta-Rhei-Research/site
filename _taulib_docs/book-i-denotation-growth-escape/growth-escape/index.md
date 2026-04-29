---
{
  "projection_kind": "taulib_declaration",
  "title": "growth_escape",
  "permalink": "/verify/taulib/docs/book-i-denotation-growth-escape/growth-escape/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.GrowthEscape`.",
  "declaration_id": "TauLib.BookI.Denotation.GrowthEscape::growth_escape",
  "declaration_slug": "growth-escape",
  "kind": "theorem",
  "name": "growth_escape",
  "module_name": "TauLib.BookI.Denotation.GrowthEscape",
  "module_url": "/verify/taulib/docs/book-i-denotation-growth-escape/",
  "source_line_start": 62,
  "source_line_end": 65,
  "registry_ids": [
    "I.L02"
  ],
  "related_registry_items": [
    {
      "id": "I.L02",
      "title": "NF-Confluence",
      "url": "/registry/object/I.L02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L62-L65",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L62-L65",
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
- Source path: [`TauLib/BookI/Denotation/GrowthEscape.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/GrowthEscape.lean#L62-L65)
- Source range: L62-L65
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.L02` — NF-Confluence

## Immediate Comment / Docstring

```lean
/-- [I.L02] **Growth Escape**: Tetration escapes the primorial tower.

    For any tower depth d ≥ 1, there exists a tetration height c such that
    2↑↑c mod M_d ≠ 2↑↑c — the tetration value cannot be represented
    faithfully within the primorial modulus.

    This is the quantitative shadow of saturation: the 4th hyperoperation
    level produces values that outrun the finite primorial approximations,
    no matter how deep the tower extends. -/
```

## Source Excerpt

```lean
theorem growth_escape (d : TauIdx) :
    ∃ c, tetration 2 c % primorial d ≠ tetration 2 c := by
  obtain ⟨c, hc⟩ := tetration_exceeds_primorial d
  exact ⟨c, mod_ne_of_gt hc (primorial_pos d)⟩
```
