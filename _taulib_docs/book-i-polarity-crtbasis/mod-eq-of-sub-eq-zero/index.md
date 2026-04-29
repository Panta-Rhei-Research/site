---
{
  "projection_kind": "taulib_declaration",
  "title": "mod_eq_of_sub_eq_zero",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/mod-eq-of-sub-eq-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::mod_eq_of_sub_eq_zero",
  "declaration_slug": "mod-eq-of-sub-eq-zero",
  "kind": "theorem",
  "name": "mod_eq_of_sub_eq_zero",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 251,
  "source_line_end": 261,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L251-L261",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L251-L261",
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
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L251-L261)
- Source range: L251-L261
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- (a-b)%m = 0 and a ≥ b implies a%m = b%m. -/
```

## Source Excerpt

```lean
private theorem mod_eq_of_sub_eq_zero {a b m : Nat} (hab : a ≥ b)
    (h : (a - b) % m = 0) : a % m = b % m := by
  by_cases hm : m = 0
  · subst hm; simp at h; omega
  · -- (a-b)%m = 0 → a-b = m*q → a = m*q + b → a%m = b%m
    have hk := Nat.div_add_mod (a - b) m
    rw [h, Nat.add_zero] at hk
    -- hk : m * ((a-b)/m) = a - b
    conv_lhs => rw [show a = m * ((a - b) / m) + b from by omega]
    rw [Nat.add_mod, Nat.mul_mod_right, Nat.zero_add,
      mod_mod_of_dvd _ _ _ ⟨1, (Nat.mul_one _).symm⟩]
```
