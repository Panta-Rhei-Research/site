---
{
  "projection_kind": "taulib_declaration",
  "title": "char_pullback_witness",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/char-pullback-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7ToposClassifier`.",
  "declaration_id": "TauLib.BookI.Topos.H7ToposClassifier::char_pullback_witness",
  "declaration_slug": "char-pullback-witness",
  "kind": "theorem",
  "name": "char_pullback_witness",
  "module_name": "TauLib.BookI.Topos.H7ToposClassifier",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/",
  "source_line_start": 239,
  "source_line_end": 242,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L239-L242",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H7ToposClassifier",
        "url": "/verify/taulib/docs/book-i-topos-h7-topos-classifier/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L239-L242",
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

- Module: [TauLib.BookI.Topos.H7ToposClassifier](/verify/taulib/docs/book-i-topos-h7-topos-classifier/)
- Source path: [`TauLib/BookI/Topos/H7ToposClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ToposClassifier.lean#L239-L242)
- Source range: L239-L242
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §4 Pullback property witness — char_pullback_true**.

    When both B-sector and C-sector confirm membership, the
    characteristic morphism evaluates to T (full membership).
    Existing `char_pullback_true` with paper-faithful repackaging. -/
```

## Source Excerpt

```lean
theorem char_pullback_witness (b_mem c_mem : TauIdx → Bool) (x : TauIdx) :
    characteristic_morphism b_mem c_mem x = T ↔
      b_mem x = true ∧ c_mem x = true :=
  char_pullback_true b_mem c_mem x
```
