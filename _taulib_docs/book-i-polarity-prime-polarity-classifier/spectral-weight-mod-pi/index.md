---
{
  "projection_kind": "taulib_declaration",
  "title": "spectralWeight_mod_pi",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/spectral-weight-mod-pi/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.PrimePolarityClassifier`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimePolarityClassifier::spectralWeight_mod_pi",
  "declaration_slug": "spectral-weight-mod-pi",
  "kind": "theorem",
  "name": "spectralWeight_mod_pi",
  "module_name": "TauLib.BookI.Polarity.PrimePolarityClassifier",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-polarity-classifier/",
  "source_line_start": 178,
  "source_line_end": 192,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L178-L192",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L178-L192",
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
- Source path: [`TauLib/BookI/Polarity/PrimePolarityClassifier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityClassifier.lean#L178-L192)
- Source range: L178-L192
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Spectral weight CRT-component at p_i**: by `crt_basis_diagonal`,
    `e_i^{(n)} ≡ 1 (mod p_{i+1})`, so `w_n(p_i) ≡ 2 (mod p_{i+1})`. -/
```

## Source Excerpt

```lean
theorem spectralWeight_mod_pi {n i : TauIdx}
    (hi : i < n) (hyp : CRTHyp n) :
    spectralWeight n i % nth_prime (i + 1) = 2 % nth_prime (i + 1) := by
  unfold spectralWeight
  -- (2 * crt_basis n i) % primorial n % nth_prime (i+1)
  -- = (2 * crt_basis n i) % nth_prime (i+1)  [since p_{i+1} | primorial n]
  -- = (2 * (crt_basis n i % nth_prime (i+1))) % nth_prime (i+1)
  -- = (2 * 1) % nth_prime (i+1)  [crt_basis_diagonal]
  -- = 2 % nth_prime (i+1)
  rw [Nat.mod_mod_of_dvd _
    (nth_prime_dvd_primorial (show i + 1 ≤ n by simp only [TauIdx] at *; omega))]
  rw [Nat.mul_mod, crt_basis_diagonal hi hyp]
  show (2 % nth_prime (i + 1) * 1) % nth_prime (i + 1) = 2 % nth_prime (i + 1)
  rw [Nat.mul_one]
  exact Nat.mod_mod _ _
```
