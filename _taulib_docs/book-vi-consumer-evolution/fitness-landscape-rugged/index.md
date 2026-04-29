---
{
  "projection_kind": "taulib_declaration",
  "title": "fitness_landscape_rugged",
  "permalink": "/verify/taulib/docs/book-vi-consumer-evolution/fitness-landscape-rugged/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Consumer.Evolution`.",
  "declaration_id": "TauLib.BookVI.Consumer.Evolution::fitness_landscape_rugged",
  "declaration_slug": "fitness-landscape-rugged",
  "kind": "theorem",
  "name": "fitness_landscape_rugged",
  "module_name": "TauLib.BookVI.Consumer.Evolution",
  "module_url": "/verify/taulib/docs/book-vi-consumer-evolution/",
  "source_line_start": 107,
  "source_line_end": 113,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Evolution.lean#L107-L113",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Evolution",
        "url": "/verify/taulib/docs/book-vi-consumer-evolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Evolution.lean#L107-L113",
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

- Module: [TauLib.BookVI.Consumer.Evolution](/verify/taulib/docs/book-vi-consumer-evolution/)
- Source path: [`TauLib/BookVI/Consumer/Evolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Evolution.lean#L107-L113)
- Source range: L107-L113
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
theorem fitness_landscape_rugged :
    fitness_topo.epistatic = true ∧
    fitness_topo.nk_model = true ∧
    fitness_topo.attractor_basins = true :=
  ⟨rfl, rfl, rfl⟩

end Tau.BookVI.Evolution
```
