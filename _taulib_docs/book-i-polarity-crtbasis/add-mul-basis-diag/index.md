---
{
  "projection_kind": "taulib_declaration",
  "title": "add_mul_basis_diag",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/add-mul-basis-diag/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::add_mul_basis_diag",
  "declaration_slug": "add-mul-basis-diag",
  "kind": "theorem",
  "name": "add_mul_basis_diag",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 347,
  "source_line_end": 352,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L347-L352",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L347-L352",
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
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L347-L352)
- Source range: L347-L352
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Diagonal: adding r * e_i changes result mod p_{i+1} by r. -/
```

## Source Excerpt

```lean
private theorem add_mul_basis_diag {acc r k i : TauIdx}
    (hi : i < k) (hyp : CRTHyp k) :
    (acc + r * crt_basis k i) % nth_prime (i + 1) = (acc + r) % nth_prime (i + 1) := by
  have h1 : crt_basis k i % nth_prime (i + 1) = 1 := crt_basis_diagonal hi hyp
  rw [Nat.add_mod acc (r * _), Nat.mul_mod, h1, Nat.mul_one,
    mod_mod_of_dvd _ _ _ ⟨1, (Nat.mul_one _).symm⟩, ← Nat.add_mod]
```
