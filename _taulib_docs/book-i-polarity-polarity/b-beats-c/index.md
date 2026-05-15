---
{
  "projection_kind": "taulib_declaration",
  "title": "b_beats_c",
  "permalink": "/corpus/taulib/docs/book-i-polarity-polarity/b-beats-c/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.Polarity`.",
  "declaration_id": "TauLib.BookI.Polarity.Polarity::b_beats_c",
  "declaration_slug": "b-beats-c",
  "kind": "theorem",
  "name": "b_beats_c",
  "module_name": "TauLib.BookI.Polarity.Polarity",
  "module_url": "/corpus/taulib/docs/book-i-polarity-polarity/",
  "source_line_start": 239,
  "source_line_end": 244,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L239-L244",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.Polarity",
        "url": "/corpus/taulib/docs/book-i-polarity-polarity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L239-L244",
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

- Module: [TauLib.BookI.Polarity.Polarity](/corpus/taulib/docs/book-i-polarity-polarity/)
- Source path: [`TauLib/BookI/Polarity/Polarity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Polarity.lean#L239-L244)
- Source range: L239-L244
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- For a ≥ 2, the exponentiation channel can match any tetration level:
    ∀ C, ∃ B, a^B > a↑↑C. -/
```

## Source Excerpt

```lean
theorem b_beats_c (a : Nat) (ha : a ≥ 2) (C : Nat) :
    ∃ B, a ^ B > tetration a C := by
  have htet := tetration_ge_arg a ha C
  -- a↑↑C ≥ C, so a^(a↑↑C) ≥ a^C ≥ ... but we just need a^B > a↑↑C
  -- Use b_channel_unbounded: ∃ B, a^B > a↑↑C
  exact b_channel_unbounded a ha (tetration a C)
```
