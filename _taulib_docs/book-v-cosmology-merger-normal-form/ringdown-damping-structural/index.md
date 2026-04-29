---
{
  "projection_kind": "taulib_declaration",
  "title": "ringdown_damping_structural",
  "permalink": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/ringdown-damping-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Cosmology.MergerNormalForm`.",
  "declaration_id": "TauLib.BookV.Cosmology.MergerNormalForm::ringdown_damping_structural",
  "declaration_slug": "ringdown-damping-structural",
  "kind": "theorem",
  "name": "ringdown_damping_structural",
  "module_name": "TauLib.BookV.Cosmology.MergerNormalForm",
  "module_url": "/verify/taulib/docs/book-v-cosmology-merger-normal-form/",
  "source_line_start": 129,
  "source_line_end": 130,
  "registry_ids": [
    "V.P97"
  ],
  "related_registry_items": [
    {
      "id": "V.P97",
      "title": "Ringdown damping is structural",
      "url": "/registry/object/V.P97/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L129-L130",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L129-L130",
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
- Source path: [`TauLib/BookV/Cosmology/MergerNormalForm.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/MergerNormalForm.lean#L129-L130)
- Source range: L129-L130
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P97` — Ringdown damping is structural

## Immediate Comment / Docstring

```lean
/-- [V.P97] Ringdown damping is structural: every mode has σ_n > 0.
    The ringdown terminates in finite time. -/
```

## Source Excerpt

```lean
theorem ringdown_damping_structural (r : RingdownMode) :
    r.damping_rate > 0 := r.damping_pos
```
