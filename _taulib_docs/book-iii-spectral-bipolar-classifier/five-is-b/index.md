---
{
  "projection_kind": "taulib_declaration",
  "title": "five_is_b",
  "permalink": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/five-is-b/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.BipolarClassifier`.",
  "declaration_id": "TauLib.BookIII.Spectral.BipolarClassifier::five_is_b",
  "declaration_slug": "five-is-b",
  "kind": "theorem",
  "name": "five_is_b",
  "module_name": "TauLib.BookIII.Spectral.BipolarClassifier",
  "module_url": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/",
  "source_line_start": 262,
  "source_line_end": 262,
  "registry_ids": [
    "III.D23"
  ],
  "related_registry_items": [
    {
      "id": "III.D23",
      "title": "Internal Bipolar Classifier",
      "url": "/registry/object/III.D23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L262-L262",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L262-L262",
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
- Source path: [`TauLib/BookIII/Spectral/BipolarClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L262-L262)
- Source range: L262-L262
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.D23` — Internal Bipolar Classifier

## Immediate Comment / Docstring

```lean
/-- [III.D23] Structural: 5 is B-type (5 mod 4 = 1). -/
```

## Source Excerpt

```lean
theorem five_is_b : label_direct 5 = .B := rfl
```
