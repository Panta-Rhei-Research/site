---
{
  "projection_kind": "taulib_declaration",
  "title": "mod_sub_eq_zero",
  "permalink": "/verify/taulib/docs/book-i-polarity-crtbasis/mod-sub-eq-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.CRTBasis`.",
  "declaration_id": "TauLib.BookI.Polarity.CRTBasis::mod_sub_eq_zero",
  "declaration_slug": "mod-sub-eq-zero",
  "kind": "theorem",
  "name": "mod_sub_eq_zero",
  "module_name": "TauLib.BookI.Polarity.CRTBasis",
  "module_url": "/verify/taulib/docs/book-i-polarity-crtbasis/",
  "source_line_start": 235,
  "source_line_end": 248,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L235-L248",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L235-L248",
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
- Source path: [`TauLib/BookI/Polarity/CRTBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/CRTBasis.lean#L235-L248)
- Source range: L235-L248
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- a ≥ b and a%m = b%m implies (a-b)%m = 0. -/
```

## Source Excerpt

```lean
private theorem mod_sub_eq_zero {a b m : Nat} (hab : a ≥ b) (h : a % m = b % m) :
    (a - b) % m = 0 := by
  by_cases hm : m = 0
  · subst hm; simp at h; omega
  · have hm_pos : m > 0 := Nat.pos_of_ne_zero hm
    have key : (b + (a - b)) % m = b % m := by rw [Nat.add_sub_cancel' hab, h]
    rw [Nat.add_mod] at key
    have hr := Nat.mod_lt b hm_pos
    have hd := Nat.mod_lt (a - b) hm_pos
    -- key : (b%m + (a-b)%m) % m = b%m, with b%m < m and (a-b)%m < m
    rcases Nat.lt_or_ge (b % m + (a - b) % m) m with h1 | h1
    · rw [Nat.mod_eq_of_lt h1] at key; omega
    · have h2 : b % m + (a - b) % m < m + m := by omega
      rw [Nat.mod_eq_sub_mod h1, Nat.mod_eq_of_lt (by omega)] at key; omega
```
