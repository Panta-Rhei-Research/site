---
{
  "projection_kind": "taulib_declaration",
  "title": "bc_exist_3",
  "permalink": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/bc-exist-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.BipolarClassifier`.",
  "declaration_id": "TauLib.BookIII.Spectral.BipolarClassifier::bc_exist_3",
  "declaration_slug": "bc-exist-3",
  "kind": "theorem",
  "name": "bc_exist_3",
  "module_name": "TauLib.BookIII.Spectral.BipolarClassifier",
  "module_url": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/",
  "source_line_start": 268,
  "source_line_end": 270,
  "registry_ids": [
    "III.T13"
  ],
  "related_registry_items": [
    {
      "id": "III.T13",
      "title": "Label Convergence",
      "url": "/registry/object/III.T13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L268-L270",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L268-L270",
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
- Source path: [`TauLib/BookIII/Spectral/BipolarClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L268-L270)
- Source range: L268-L270
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T13` — Label Convergence

## Immediate Comment / Docstring

```lean
/-- [III.T13] Structural: both B and C labels exist for first 3 primes. -/
```

## Source Excerpt

```lean
theorem bc_exist_3 : bc_balance_check 3 = true := by native_decide

end Tau.BookIII.Spectral
```
