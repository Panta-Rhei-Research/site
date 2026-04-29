---
{
  "projection_kind": "taulib_declaration",
  "title": "teich_list_length",
  "permalink": "/verify/taulib/docs/book-i-polarity-teichmueller-lift/teich-list-length/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.TeichmuellerLift`.",
  "declaration_id": "TauLib.BookI.Polarity.TeichmuellerLift::teich_list_length",
  "declaration_slug": "teich-list-length",
  "kind": "theorem",
  "name": "teich_list_length",
  "module_name": "TauLib.BookI.Polarity.TeichmuellerLift",
  "module_url": "/verify/taulib/docs/book-i-polarity-teichmueller-lift/",
  "source_line_start": 65,
  "source_line_end": 68,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L65-L68",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.TeichmuellerLift",
        "url": "/verify/taulib/docs/book-i-polarity-teichmueller-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L65-L68",
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

- Module: [TauLib.BookI.Polarity.TeichmuellerLift](/verify/taulib/docs/book-i-polarity-teichmueller-lift/)
- Source path: [`TauLib/BookI/Polarity/TeichmuellerLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/TeichmuellerLift.lean#L65-L68)
- Source range: L65-L68
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
private theorem teich_list_length (r i d : Nat) : (teich_list r i d).length = d := by
  induction d with
  | zero => rfl
  | succ d' ih => simp [teich_list, ih]
```
