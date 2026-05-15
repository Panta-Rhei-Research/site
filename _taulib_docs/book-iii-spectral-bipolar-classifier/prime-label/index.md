---
{
  "projection_kind": "taulib_declaration",
  "title": "PrimeLabel",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-bipolar-classifier/prime-label/",
  "summary_short": "`inductive` declaration in `TauLib.BookIII.Spectral.BipolarClassifier`.",
  "declaration_id": "TauLib.BookIII.Spectral.BipolarClassifier::PrimeLabel",
  "declaration_slug": "prime-label",
  "kind": "inductive",
  "name": "PrimeLabel",
  "module_name": "TauLib.BookIII.Spectral.BipolarClassifier",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-bipolar-classifier/",
  "source_line_start": 40,
  "source_line_end": 44,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L40-L44",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.BipolarClassifier",
        "url": "/corpus/taulib/docs/book-iii-spectral-bipolar-classifier/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L40-L44",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIII.Spectral.BipolarClassifier](/corpus/taulib/docs/book-iii-spectral-bipolar-classifier/)
- Source path: [`TauLib/BookIII/Spectral/BipolarClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L40-L44)
- Source range: L40-L44
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `III.D23` — Internal Bipolar Classifier

## Immediate Comment / Docstring

```lean
/-- [III.D23] Prime labels: B-type (multiplicative/Galois dominant),
    C-type (additive/automorphic dominant), X-type (balanced). -/
```

## Source Excerpt

```lean
inductive PrimeLabel where
  | B : PrimeLabel    -- exponent-dominant (B-lobe, multiplicative)
  | C : PrimeLabel    -- tetration-dominant (C-lobe, additive)
  | X : PrimeLabel    -- balanced (crossing type)
  deriving Repr, DecidableEq, BEq, Inhabited
```
