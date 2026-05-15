---
{
  "projection_kind": "taulib_declaration",
  "title": "labelN_eq_chi_p",
  "permalink": "/corpus/taulib/docs/book-i-polarity-prime-polarity-classifier/label-n-eq-chi-p/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.PrimePolarityClassifier`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimePolarityClassifier::labelN_eq_chi_p",
  "declaration_slug": "label-n-eq-chi-p",
  "kind": "theorem",
  "name": "labelN_eq_chi_p",
  "module_name": "TauLib.BookI.Polarity.PrimePolarityClassifier",
  "module_url": "/corpus/taulib/docs/book-i-polarity-prime-polarity-classifier/",
  "source_line_start": 250,
  "source_line_end": 251,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L250-L251",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PrimePolarityClassifier",
        "url": "/corpus/taulib/docs/book-i-polarity-prime-polarity-classifier/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L250-L251",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Polarity.PrimePolarityClassifier](/corpus/taulib/docs/book-i-polarity-prime-polarity-classifier/)
- Source path: [`TauLib/BookI/Polarity/PrimePolarityClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L250-L251)
- Source range: L250-L251
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Lemma 6.5 reduction (depth-independence form)**:
    `Label_n(p_i) = χ_{p_i}(2)` for every depth `n` (immediate
    by definition).

    The deeper paper-content claim — that
    `SpecLeg_n(w_n(p_i)) = χ_{p_i}(2)` — is implicit in our
    formulation: we *define* labelN via χ_{p_i}(2), and the
    structural Lemmas `spectralWeight_mod_pi` /
    `spectralWeight_mod_pj` witness that the spectral weight
    has CRT support exactly at the i-th component (where it equals
    2), justifying the definitional reduction. -/
```

## Source Excerpt

```lean
theorem labelN_eq_chi_p (n i : TauIdx) :
    labelN n i = chi_p (nth_prime (i + 1)) 2 := rfl
```
