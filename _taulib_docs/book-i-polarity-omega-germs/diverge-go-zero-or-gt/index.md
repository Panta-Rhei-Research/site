---
{
  "projection_kind": "taulib_declaration",
  "title": "diverge_go_zero_or_gt",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-germs/diverge-go-zero-or-gt/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.OmegaGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaGerms::diverge_go_zero_or_gt",
  "declaration_slug": "diverge-go-zero-or-gt",
  "kind": "theorem",
  "name": "diverge_go_zero_or_gt",
  "module_name": "TauLib.BookI.Polarity.OmegaGerms",
  "module_url": "/verify/taulib/docs/book-i-polarity-omega-germs/",
  "source_line_start": 270,
  "source_line_end": 288,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L270-L288",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.OmegaGerms",
        "url": "/verify/taulib/docs/book-i-polarity-omega-germs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L270-L288",
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

- Module: [TauLib.BookI.Polarity.OmegaGerms](/verify/taulib/docs/book-i-polarity-omega-germs/)
- Source path: [`TauLib/BookI/Polarity/OmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L270-L288)
- Source range: L270-L288
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: diverge_go returns 0 or a value > i (the starting index). -/
```

## Source Excerpt

```lean
private theorem diverge_go_zero_or_gt (c1 c2 : List TauIdx) (d i fuel : Nat) :
    diverge_go c1 c2 d i fuel = 0 ∨ diverge_go c1 c2 d i fuel > i := by
  induction fuel generalizing i with
  | zero => left; unfold diverge_go; rfl
  | succ n ih =>
    unfold diverge_go
    simp only [Nat.succ_ne_zero, ↓reduceIte]
    split -- i ≥ d?
    · left; rfl
    · by_cases heq : c1.getD i 0 = c2.getD i 0
      · -- Equal: bne false, recurse
        have hne : c1.getD i 0 ≠ c2.getD i 0 → False := fun h => h heq
        simp_all
        rcases ih (i + 1) with h | h
        · left; exact h
        · right; exact Nat.lt_trans (Nat.lt_add_one i) h
      · -- Unequal: bne true, return i + 1
        have heq' : c2.getD i 0 ≠ c1.getD i 0 := Ne.symm heq
        simp_all
```
