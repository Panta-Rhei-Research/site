---
{
  "projection_kind": "taulib_declaration",
  "title": "classifier_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/classifier-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.BipolarClassifier`.",
  "declaration_id": "TauLib.BookIII.Spectral.BipolarClassifier::classifier_check",
  "declaration_slug": "classifier-check",
  "kind": "def",
  "name": "classifier_check",
  "module_name": "TauLib.BookIII.Spectral.BipolarClassifier",
  "module_url": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/",
  "source_line_start": 97,
  "source_line_end": 112,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L97-L112",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L97-L112",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookIII/Spectral/BipolarClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L97-L112)
- Source range: L97-L112
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D23` — Internal Bipolar Classifier

## Immediate Comment / Docstring

```lean
/-- [III.D23] Classifier check: verify label assignment is consistent
    across methods for all primes up to bound. -/
```

## Source Excerpt

```lean
def classifier_check (bound : TauIdx) : Bool :=
  go 1 (bound + 1)
where
  go (i fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if i > bound then true
    else
      let p := nth_prime i
      if p > bound then true
      else
        let label := label_direct p
        -- Label-count consistency: B + C + X primes sum to total at depth i
        let (b_ct, c_ct, x_ct) := label_counts i
        let count_ok := b_ct + c_ct + x_ct == i
        count_ok && go (i + 1) (fuel - 1)
  termination_by fuel
```
