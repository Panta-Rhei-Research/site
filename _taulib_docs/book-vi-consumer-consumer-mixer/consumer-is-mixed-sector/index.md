---
{
  "projection_kind": "taulib_declaration",
  "title": "consumer_is_mixed_sector",
  "permalink": "/verify/taulib/docs/book-vi-consumer-consumer-mixer/consumer-is-mixed-sector/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Consumer.ConsumerMixer`.",
  "declaration_id": "TauLib.BookVI.Consumer.ConsumerMixer::consumer_is_mixed_sector",
  "declaration_slug": "consumer-is-mixed-sector",
  "kind": "theorem",
  "name": "consumer_is_mixed_sector",
  "module_name": "TauLib.BookVI.Consumer.ConsumerMixer",
  "module_url": "/verify/taulib/docs/book-vi-consumer-consumer-mixer/",
  "source_line_start": 59,
  "source_line_end": 62,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L59-L62",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L59-L62",
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
- Source path: [`TauLib/BookVI/Consumer/ConsumerMixer.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L59-L62)
- Source range: L59-L62
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Consumer is the mixed sector from FourPlusOne. -/
```

## Source Excerpt

```lean
theorem consumer_is_mixed_sector :
    consumer_sector.is_primitive = false ∧
    canonical_mixer.is_mixed = true :=
  ⟨rfl, rfl⟩
```
