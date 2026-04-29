---
{
  "projection_kind": "taulib_declaration",
  "title": "sleep_two_lobes",
  "permalink": "/verify/taulib/docs/book-vi-consumer-neural/sleep-two-lobes/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Consumer.Neural`.",
  "declaration_id": "TauLib.BookVI.Consumer.Neural::sleep_two_lobes",
  "declaration_slug": "sleep-two-lobes",
  "kind": "theorem",
  "name": "sleep_two_lobes",
  "module_name": "TauLib.BookVI.Consumer.Neural",
  "module_url": "/verify/taulib/docs/book-vi-consumer-neural/",
  "source_line_start": 97,
  "source_line_end": 102,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L97-L102",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Neural",
        "url": "/verify/taulib/docs/book-vi-consumer-neural/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L97-L102",
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

- Module: [TauLib.BookVI.Consumer.Neural](/verify/taulib/docs/book-vi-consumer-neural/)
- Source path: [`TauLib/BookVI/Consumer/Neural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Neural.lean#L97-L102)
- Source range: L97-L102
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
theorem sleep_two_lobes :
    sleep_lemn.lobe_count = 2 ∧
    sleep_lemn.wake_lobe = true ∧
    sleep_lemn.sleep_lobe = true ∧
    sleep_lemn.circadian_link = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
