---
{
  "projection_kind": "taulib_declaration",
  "title": "spectralWeight_mod_pj",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/spectral-weight-mod-pj/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.PrimePolarityClassifier`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimePolarityClassifier::spectralWeight_mod_pj",
  "declaration_slug": "spectral-weight-mod-pj",
  "kind": "theorem",
  "name": "spectralWeight_mod_pj",
  "module_name": "TauLib.BookI.Polarity.PrimePolarityClassifier",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/",
  "source_line_start": 197,
  "source_line_end": 205,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L197-L205",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L197-L205",
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

- Module: [TauLib.BookI.Polarity.PrimePolarityClassifier](/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/)
- Source path: [`TauLib/BookI/Polarity/PrimePolarityClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L197-L205)
- Source range: L197-L205
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Spectral weight CRT-component at p_j (j ≠ i)**: by
    `crt_basis_off_diagonal`, `e_i^{(n)} ≡ 0 (mod p_{j+1})`, so
    `w_n(p_i) ≡ 0 (mod p_{j+1})`. -/
```

## Source Excerpt

```lean
theorem spectralWeight_mod_pj {n i j : TauIdx}
    (hi : i < n) (hj : j < n) (hne : i ≠ j) (hyp : CRTHyp n) :
    spectralWeight n i % nth_prime (j + 1) = 0 := by
  unfold spectralWeight
  rw [Nat.mod_mod_of_dvd _
    (nth_prime_dvd_primorial (show j + 1 ≤ n by simp only [TauIdx] at *; omega))]
  rw [Nat.mul_mod, crt_basis_off_diagonal hi hj hne hyp]
  show (2 % nth_prime (j + 1) * 0) % nth_prime (j + 1) = 0
  rw [Nat.mul_zero]; exact Nat.zero_mod _
```
