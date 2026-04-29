---
{
  "projection_kind": "taulib_declaration",
  "title": "add_mul_basis_off_diag",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/add-mul-basis-off-diag/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::add_mul_basis_off_diag",
  "declaration_slug": "add-mul-basis-off-diag",
  "kind": "theorem",
  "name": "add_mul_basis_off_diag",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 337,
  "source_line_end": 344,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L337-L344",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L337-L344",
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
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L337-L344)
- Source range: L337-L344
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Off-diagonal: adding r * e_i doesn't change result mod p_{l+1}. -/
```

## Source Excerpt

```lean
private theorem add_mul_basis_off_diag {acc r k i l : TauIdx}
    (hi : i < k) (hl : l < k) (hne : i ≠ l) (hyp : CRTHyp k) :
    (acc + r * crt_basis k i) % nth_prime (l + 1) = acc % nth_prime (l + 1) := by
  have h0 : crt_basis k i % nth_prime (l + 1) = 0 := crt_basis_off_diagonal hi hl hne hyp
  have h1 : (r * crt_basis k i) % nth_prime (l + 1) = 0 := by
    rw [Nat.mul_mod, h0, Nat.mul_zero, Nat.zero_mod]
  rw [Nat.add_mod, h1, Nat.add_zero,
    mod_mod_of_dvd _ _ _ ⟨1, (Nat.mul_one _).symm⟩]
```
