---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L170",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/eval-l170/",
  "summary_short": "`eval` declaration in `TauLib.BookI.Polarity.PrimePolarityClassifier`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimePolarityClassifier::#eval:170",
  "declaration_slug": "eval-l170",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookI.Polarity.PrimePolarityClassifier",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/",
  "source_line_start": 170,
  "source_line_end": 170,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L170-L170",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PrimePolarityClassifier",
        "url": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L170-L170",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.BookI.Polarity.PrimePolarityClassifier](/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/)
- Source path: [`TauLib/BookI/Polarity/PrimePolarityClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L170-L170)
- Source range: L170-L170
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Numerical sanity: spectral weights at depth 5 for primes p_1=2, p_2=3, ..., p_5=11
```

## Source Excerpt

```lean
#eval spectralWeight 5 0    -- 2 * e_0^{(5)} mod 30030 (= primorial 5 = 2·3·5·7·11)
```
