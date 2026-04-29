---
{
  "projection_kind": "taulib_declaration",
  "title": "mod_eq_of_coprime_mod_eq",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/mod-eq-of-coprime-mod-eq/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::mod_eq_of_coprime_mod_eq",
  "declaration_slug": "mod-eq-of-coprime-mod-eq",
  "kind": "theorem",
  "name": "mod_eq_of_coprime_mod_eq",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 264,
  "source_line_end": 276,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L264-L276",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L264-L276",
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
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L264-L276)
- Source range: L264-L276
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Two-modulus CRT uniqueness step. -/
```

## Source Excerpt

```lean
private theorem mod_eq_of_coprime_mod_eq {a b p q : Nat}
    (hcop : Nat.Coprime p q)
    (hp : a % p = b % p) (hq : a % q = b % q) :
    a % (p * q) = b % (p * q) := by
  rcases Nat.le_total a b with hab | hba
  · exact (mod_eq_of_sub_eq_zero hab
      (mod_eq_zero_of_dvd' (coprime_mul_dvd hcop
        (dvd_of_mod_eq_zero (mod_sub_eq_zero hab hp.symm))
        (dvd_of_mod_eq_zero (mod_sub_eq_zero hab hq.symm))))).symm
  · exact mod_eq_of_sub_eq_zero hba
      (mod_eq_zero_of_dvd' (coprime_mul_dvd hcop
        (dvd_of_mod_eq_zero (mod_sub_eq_zero hba hp))
        (dvd_of_mod_eq_zero (mod_sub_eq_zero hba hq))))
```
