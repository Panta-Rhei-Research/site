---
{
  "projection_kind": "taulib_declaration",
  "title": "split_label_10_4",
  "permalink": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/split-label-10-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.BipolarClassifier`.",
  "declaration_id": "TauLib.BookIII.Spectral.BipolarClassifier::split_label_10_4",
  "declaration_slug": "split-label-10-4",
  "kind": "theorem",
  "name": "split_label_10_4",
  "module_name": "TauLib.BookIII.Spectral.BipolarClassifier",
  "module_url": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/",
  "source_line_start": 251,
  "source_line_end": 252,
  "registry_ids": [
    "III.P08"
  ],
  "related_registry_items": [
    {
      "id": "III.P08",
      "title": "Label-Idempotent Compatibility",
      "url": "/registry/object/III.P08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L251-L252",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.BipolarClassifier",
        "url": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L251-L252",
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

- Module: [TauLib.BookIII.Spectral.BipolarClassifier](/verify/taulib/docs/book-iii-spectral-bipolar-classifier/)
- Source path: [`TauLib/BookIII/Spectral/BipolarClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L251-L252)
- Source range: L251-L252
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P08` — Label-Idempotent Compatibility

## Immediate Comment / Docstring

```lean
-- Split-complex label [III.P08]
```

## Source Excerpt

```lean
theorem split_label_10_4 :
    split_complex_label_check 10 4 = true := by native_decide
```
