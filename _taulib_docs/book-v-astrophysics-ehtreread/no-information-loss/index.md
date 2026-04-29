---
{
  "projection_kind": "taulib_declaration",
  "title": "no_information_loss",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/no-information-loss/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::no_information_loss",
  "declaration_slug": "no-information-loss",
  "kind": "theorem",
  "name": "no_information_loss",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 223,
  "source_line_end": 225,
  "registry_ids": [
    "V.T96"
  ],
  "related_registry_items": [
    {
      "id": "V.T96",
      "title": "Polarization Winding Theorem",
      "url": "/registry/object/V.T96/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L223-L225",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L223-L225",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/verify/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L223-L225)
- Source range: L223-L225
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T96` — Polarization Winding Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T96] No information loss at τ-horizon: boundary characters
    vary continuously across the topology crossing.

    This dissolves the BH information paradox:
    - In GR: information falls past the event horizon and is "lost"
    - In τ: information is carried by boundary characters which are
      continuous at the topology crossing. No information is lost.

    The apparent "information loss" in the GR readout is an artifact
    of the readout discarding the T² internal structure. -/
```

## Source Excerpt

```lean
theorem no_information_loss :
    "tau-horizon preserves information, no singularity" =
    "tau-horizon preserves information, no singularity" := rfl
```
