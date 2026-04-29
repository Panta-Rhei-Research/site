---
{
  "projection_kind": "taulib_declaration",
  "title": "signature_rigidity_uniqueness",
  "permalink": "/verify/taulib/docs/book-vi-consumer-consumer-mixer/signature-rigidity-uniqueness/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Consumer.ConsumerMixer`.",
  "declaration_id": "TauLib.BookVI.Consumer.ConsumerMixer::signature_rigidity_uniqueness",
  "declaration_slug": "signature-rigidity-uniqueness",
  "kind": "theorem",
  "name": "signature_rigidity_uniqueness",
  "module_name": "TauLib.BookVI.Consumer.ConsumerMixer",
  "module_url": "/verify/taulib/docs/book-vi-consumer-consumer-mixer/",
  "source_line_start": 99,
  "source_line_end": 104,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L99-L104",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.ConsumerMixer",
        "url": "/verify/taulib/docs/book-vi-consumer-consumer-mixer/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L99-L104",
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

- Module: [TauLib.BookVI.Consumer.ConsumerMixer](/verify/taulib/docs/book-vi-consumer-consumer-mixer/)
- Source path: [`TauLib/BookVI/Consumer/ConsumerMixer.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L99-L104)
- Source range: L99-L104
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
theorem signature_rigidity_uniqueness :
    sig_rigid.fiber_fiber_stable = true ∧
    sig_rigid.base_base_stable = false ∧
    sig_rigid.base_fiber_stable = false ∧
    sig_rigid.stable_count = 1 :=
  ⟨rfl, rfl, rfl, rfl⟩
```
