---
{
  "projection_kind": "taulib_declaration",
  "title": "mod_inv_correct",
  "permalink": "/verify/taulib/docs/book-i-polarity-chinese-remainder/mod-inv-correct/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.ChineseRemainder`.",
  "declaration_id": "TauLib.BookI.Polarity.ChineseRemainder::mod_inv_correct",
  "declaration_slug": "mod-inv-correct",
  "kind": "theorem",
  "name": "mod_inv_correct",
  "module_name": "TauLib.BookI.Polarity.ChineseRemainder",
  "module_url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/",
  "source_line_start": 74,
  "source_line_end": 84,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ChineseRemainder.lean#L74-L84",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ChineseRemainder.lean#L74-L84",
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
- Source path: [`TauLib/BookI/Polarity/ChineseRemainder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ChineseRemainder.lean#L74-L84)
- Source range: L74-L84
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- mod_inv is correct for coprime inputs with m > 1. -/
```

## Source Excerpt

```lean
theorem mod_inv_correct (a m : Nat) (hcop : Nat.Coprime a m) (hm : m > 1) :
    (a * mod_inv a m) % m = 1 := by
  unfold mod_inv
  apply mod_inv_go_correct
  obtain ⟨x, hx_lt, hx_mod⟩ := mod_inv_exists a m hcop hm
  have hx1 : x ≥ 1 := by
    rcases x with _ | x
    · -- x = 0: (a * 0) % m = 0 % m = 0 ≠ 1
      simp at hx_mod
    · exact Nat.succ_le_succ (Nat.zero_le x)
  exact ⟨x, hx1, by omega, hx_mod⟩
```
