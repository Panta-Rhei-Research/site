---
{
  "projection_kind": "taulib_declaration",
  "title": "bc_balance_check",
  "permalink": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/bc-balance-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.BipolarClassifier`.",
  "declaration_id": "TauLib.BookIII.Spectral.BipolarClassifier::bc_balance_check",
  "declaration_slug": "bc-balance-check",
  "kind": "def",
  "name": "bc_balance_check",
  "module_name": "TauLib.BookIII.Spectral.BipolarClassifier",
  "module_url": "/verify/taulib/docs/book-iii-spectral-bipolar-classifier/",
  "source_line_start": 145,
  "source_line_end": 147,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L145-L147",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L145-L147",
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
- Source path: [`TauLib/BookIII/Spectral/BipolarClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/BipolarClassifier.lean#L145-L147)
- Source range: L145-L147
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T13` — Label Convergence

## Immediate Comment / Docstring

```lean
/-- [III.T13] B-C balance: both B-type and C-type primes exist
    in every sufficiently large range. -/
```

## Source Excerpt

```lean
def bc_balance_check (bound : TauIdx) : Bool :=
  let (b, c, _x) := label_counts bound
  b > 0 && c > 0
```
