---
{
  "projection_kind": "taulib_declaration",
  "title": "label_counts",
  "permalink": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/label-counts/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.BipolarClassifier`.",
  "declaration_id": "TauLib.BookIII.Spectral.BipolarClassifier::label_counts",
  "declaration_slug": "label-counts",
  "kind": "def",
  "name": "label_counts",
  "module_name": "TauLib.BookIII.Spectral.BipolarClassifier",
  "module_url": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/",
  "source_line_start": 81,
  "source_line_end": 93,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L81-L93",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L81-L93",
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
- Source path: [`TauLib/BookIII/Spectral/BipolarClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L81-L93)
- Source range: L81-L93
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D23` — Internal Bipolar Classifier

## Immediate Comment / Docstring

```lean
/-- [III.D23] Count B, C, X primes up to depth k. -/
```

## Source Excerpt

```lean
def label_counts (k : TauIdx) : (TauIdx × TauIdx × TauIdx) :=
  go 1 0 0 0 (k + 1)
where
  go (i b_ct c_ct x_ct fuel : Nat) : (TauIdx × TauIdx × TauIdx) :=
    if fuel = 0 then (b_ct, c_ct, x_ct)
    else if i > k then (b_ct, c_ct, x_ct)
    else
      let p := nth_prime i
      match label_direct p with
      | .B => go (i + 1) (b_ct + 1) c_ct x_ct (fuel - 1)
      | .C => go (i + 1) b_ct (c_ct + 1) x_ct (fuel - 1)
      | .X => go (i + 1) b_ct c_ct (x_ct + 1) (fuel - 1)
  termination_by fuel
```
