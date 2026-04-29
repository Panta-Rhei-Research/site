---
{
  "projection_kind": "taulib_declaration",
  "title": "mod_inv_go_correct",
  "permalink": "/verify/taulib/docs/book-i-polarity-chinese-remainder/mod-inv-go-correct/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.ChineseRemainder`.",
  "declaration_id": "TauLib.BookI.Polarity.ChineseRemainder::mod_inv_go_correct",
  "declaration_slug": "mod-inv-go-correct",
  "kind": "theorem",
  "name": "mod_inv_go_correct",
  "module_name": "TauLib.BookI.Polarity.ChineseRemainder",
  "module_url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/",
  "source_line_start": 54,
  "source_line_end": 71,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ChineseRemainder.lean#L54-L71",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.ChineseRemainder",
        "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ChineseRemainder.lean#L54-L71",
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

- Module: [TauLib.BookI.Polarity.ChineseRemainder](/verify/taulib/docs/book-i-polarity-chinese-remainder/)
- Source path: [`TauLib/BookI/Polarity/ChineseRemainder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ChineseRemainder.lean#L54-L71)
- Source range: L54-L71
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- mod_inv_go finds a valid inverse when one exists in range. -/
```

## Source Excerpt

```lean
theorem mod_inv_go_correct (a m x fuel : Nat)
    (h_exists : ∃ y, x ≤ y ∧ y < x + fuel ∧ (a * y) % m = 1) :
    (a * mod_inv_go a m x fuel) % m = 1 := by
  induction fuel generalizing x with
  | zero =>
    obtain ⟨y, _, hy_lt, _⟩ := h_exists; omega
  | succ n ih =>
    unfold mod_inv_go
    simp only [Nat.succ_ne_zero, ↓reduceIte]
    split
    · rename_i heq; exact beq_iff_eq.mp heq
    · rename_i hne
      apply ih
      obtain ⟨y, hxy, hy_lt, hy_mod⟩ := h_exists
      refine ⟨y, ?_, by omega, hy_mod⟩
      rcases Nat.eq_or_lt_of_le hxy with rfl | hlt
      · exfalso; exact (beq_iff_eq.not.mp hne) hy_mod
      · omega
```
