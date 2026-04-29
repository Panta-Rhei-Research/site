---
{
  "projection_kind": "taulib_declaration",
  "title": "bh_ab_phase",
  "permalink": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/bh-ab-phase/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.MergerNormalForm`.",
  "declaration_id": "TauLib.BookV.Cosmology.MergerNormalForm::bh_ab_phase",
  "declaration_slug": "bh-ab-phase",
  "kind": "theorem",
  "name": "bh_ab_phase",
  "module_name": "TauLib.BookV.Cosmology.MergerNormalForm",
  "module_url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/",
  "source_line_start": 255,
  "source_line_end": 256,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L255-L256",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.MergerNormalForm",
        "url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L255-L256",
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

- Module: [TauLib.BookV.Cosmology.MergerNormalForm](/verify/taulib/docs/book-v-cosmology-merger-normal-form/)
- Source path: [`TauLib/BookV/Cosmology/MergerNormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L255-L256)
- Source range: L255-L256
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- AB phase is proportional to mass. -/
```

## Source Excerpt

```lean
theorem bh_ab_phase (p : BHABPhase) (h : p.proportional_to_mass = true) :
    p.proportional_to_mass = true := h
```
