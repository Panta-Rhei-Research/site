---
{
  "projection_kind": "taulib_declaration",
  "title": "consumer_is_mixed_sector",
  "permalink": "/corpus/taulib/docs/book-vi-consumer-consumer-mixer/consumer-is-mixed-sector/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Consumer.ConsumerMixer`.",
  "declaration_id": "TauLib.BookVI.Consumer.ConsumerMixer::consumer_is_mixed_sector",
  "declaration_slug": "consumer-is-mixed-sector",
  "kind": "theorem",
  "name": "consumer_is_mixed_sector",
  "module_name": "TauLib.BookVI.Consumer.ConsumerMixer",
  "module_url": "/corpus/taulib/docs/book-vi-consumer-consumer-mixer/",
  "source_line_start": 59,
  "source_line_end": 62,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L59-L62",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.ConsumerMixer",
        "url": "/corpus/taulib/docs/book-vi-consumer-consumer-mixer/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L59-L62",
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

- Module: [TauLib.BookVI.Consumer.ConsumerMixer](/corpus/taulib/docs/book-vi-consumer-consumer-mixer/)
- Source path: [`TauLib/BookVI/Consumer/ConsumerMixer.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/ConsumerMixer.lean#L59-L62)
- Source range: L59-L62
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

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
