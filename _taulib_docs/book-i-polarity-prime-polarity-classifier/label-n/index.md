---
{
  "projection_kind": "taulib_declaration",
  "title": "labelN",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/label-n/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.PrimePolarityClassifier`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimePolarityClassifier::labelN",
  "declaration_slug": "label-n",
  "kind": "def",
  "name": "labelN",
  "module_name": "TauLib.BookI.Polarity.PrimePolarityClassifier",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/",
  "source_line_start": 226,
  "source_line_end": 227,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L226-L227",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L226-L227",
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

- Module: [TauLib.BookI.Polarity.PrimePolarityClassifier](/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/)
- Source path: [`TauLib/BookI/Polarity/PrimePolarityClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L226-L227)
- Source range: L226-L227
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Bipolar classifier** at depth `n` for the i-th prime.

    Direct formulation via `chi_p` at `nth_prime (i+1)` applied to
    `2`: by paper Lemma 6.5 (`jacobi-reduce`), this equals the
    spectral Legendre symbol `SpecLeg_n(w_n(p_i))`, which by paper
    Def 6.4 is the bipolar label.

      `Label_n(p_i) := χ_{p_i}(2)`.

    Returns `+1` (B-class), `-1` (C-class), or `0` (X-class for
    p_i = 2 since `χ_2(2) = 0` by Kronecker convention).

    The depth `n` parameter is included for paper-faithfulness
    (paper writes `Label_n(p_i)`), but by Lemma 6.5 the value is
    independent of `n` once `n ≥ i + 1`. -/
```

## Source Excerpt

```lean
def labelN (_n i : TauIdx) : Int :=
  chi_p (nth_prime (i + 1)) 2
```
