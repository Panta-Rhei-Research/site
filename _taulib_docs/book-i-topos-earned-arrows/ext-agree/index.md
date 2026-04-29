---
{
  "projection_kind": "taulib_declaration",
  "title": "TauArrow.ext_agree",
  "permalink": "/verify/taulib/docs/book-i-topos-earned-arrows/ext-agree/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.EarnedArrows`.",
  "declaration_id": "TauLib.BookI.Topos.EarnedArrows::TauArrow.ext_agree",
  "declaration_slug": "ext-agree",
  "kind": "def",
  "name": "TauArrow.ext_agree",
  "module_name": "TauLib.BookI.Topos.EarnedArrows",
  "module_url": "/verify/taulib/docs/book-i-topos-earned-arrows/",
  "source_line_start": 53,
  "source_line_end": 55,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L53-L55",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.EarnedArrows",
        "url": "/verify/taulib/docs/book-i-topos-earned-arrows/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L53-L55",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookI.Topos.EarnedArrows](/verify/taulib/docs/book-i-topos-earned-arrows/)
- Source path: [`TauLib/BookI/Topos/EarnedArrows.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedArrows.lean#L53-L55)
- Source range: L53-L55
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Two τ-arrows with the same source/target agree extensionally. -/
```

## Source Excerpt

```lean
def TauArrow.ext_agree (a₁ a₂ : TauArrow)
    (hs : a₁.source = a₂.source) (ht : a₁.target = a₂.target) :
    a₁.source = a₂.source ∧ a₁.target = a₂.target := ⟨hs, ht⟩
```
