---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_basis_off_diagonal",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/crt-basis-off-diagonal/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::crt_basis_off_diagonal",
  "declaration_slug": "crt-basis-off-diagonal",
  "kind": "theorem",
  "name": "crt_basis_off_diagonal",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 183,
  "source_line_end": 191,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L183-L191",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.CRTBasis",
        "url": "/verify/taulib/docs/book-i-polarity-crtbasis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L183-L191",
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

- Module: [TauLib.BookI.Polarity.CRTBasis](/verify/taulib/docs/book-i-polarity-crtbasis/)
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L183-L191)
- Source range: L183-L191
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- e_i ≡ 0 (mod p_{j+1}) for j ≠ i: off-diagonal case. -/
```

## Source Excerpt

```lean
theorem crt_basis_off_diagonal {k i j : TauIdx}
    (hi : i < k) (hj : j < k) (hne : i ≠ j) (hyp : CRTHyp k) :
    crt_basis k i % nth_prime (j + 1) = 0 := by
  simp only [crt_basis]
  -- Step 1: % M_k % pj = % pj
  rw [mod_mod_of_dvd _ _ _
    (nth_prime_dvd_primorial (show j + 1 ≤ k by simp only [TauIdx] at *; omega))]
  -- Step 2: pj | cofactor, so (cofactor * anything) % pj = 0
  exact mul_mod_eq_zero_of_dvd (other_prime_dvd_cofactor hi hj hne hyp)
```
