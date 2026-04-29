---
{
  "projection_kind": "taulib_declaration",
  "title": "diverge_go_triangle",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-germs/diverge-go-triangle/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.OmegaGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaGerms::diverge_go_triangle",
  "declaration_slug": "diverge-go-triangle",
  "kind": "theorem",
  "name": "diverge_go_triangle",
  "module_name": "TauLib.BookI.Polarity.OmegaGerms",
  "module_url": "/verify/taulib/docs/book-i-polarity-omega-germs/",
  "source_line_start": 293,
  "source_line_end": 336,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L293-L336",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L293-L336",
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
- Source path: [`TauLib/BookI/Polarity/OmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L293-L336)
- Source range: L293-L336
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Ultrametric triangle inequality for diverge_go (formal, universal proof).
    The first disagreement of (c1,c3) is either 0 (identical) or at least as deep
    as the minimum of the first disagreements of (c1,c2) and (c2,c3). -/
```

## Source Excerpt

```lean
private theorem diverge_go_triangle (c1 c2 c3 : List TauIdx) (d i fuel : Nat) :
    diverge_go c1 c3 d i fuel = 0 ∨
    diverge_go c1 c3 d i fuel ≥
      Nat.min (diverge_go c1 c2 d i fuel) (diverge_go c2 c3 d i fuel) := by
  induction fuel generalizing i with
  | zero => left; unfold diverge_go; rfl
  | succ n ih =>
    unfold diverge_go
    simp only [Nat.succ_ne_zero, ↓reduceIte]
    split -- i ≥ d?
    · left; rfl
    · rename_i hid
      -- Nested by_cases: derive third equality from first two to avoid contradictions
      by_cases h13 : c1.getD i 0 = c3.getD i 0
      · -- c1[i] = c3[i]: d13 recurses
        by_cases h12 : c1.getD i 0 = c2.getD i 0
        · -- c1[i] = c2[i] → c2[i] = c3[i], all recurse → IH
          have h23 : c2.getD i 0 = c3.getD i 0 := h12.symm.trans h13
          have h23' : c3.getD i 0 ≠ c2.getD i 0 → False := fun h => h h23.symm
          simp_all
        · -- c1[i] ≠ c2[i] → c2[i] ≠ c3[i], d12=i+1, d23=i+1
          have h23 : c2.getD i 0 ≠ c3.getD i 0 := fun heq => h12 (h13.trans heq.symm)
          have h12' : c2.getD i 0 ≠ c1.getD i 0 := Ne.symm h12
          have h23' : c3.getD i 0 ≠ c2.getD i 0 := Ne.symm h23
          simp_all
          rcases diverge_go_zero_or_gt c1 c3 d (i + 1) n with h | h
          · left; exact h
          · right; exact Nat.le_of_lt h
      · -- c1[i] ≠ c3[i]: d13 = i+1
        have h13' : c3.getD i 0 ≠ c1.getD i 0 := Ne.symm h13
        by_cases h12 : c1.getD i 0 = c2.getD i 0
        · -- c1[i] = c2[i] → c2[i] ≠ c3[i], d12 recurses, d23=i+1
          have h23 : c2.getD i 0 ≠ c3.getD i 0 := fun heq => h13 (h12.trans heq)
          have h23' : c3.getD i 0 ≠ c2.getD i 0 := Ne.symm h23
          simp_all; exact Nat.min_le_right _ _
        · -- c1[i] ≠ c2[i]: d12 = i+1
          have h12' : c2.getD i 0 ≠ c1.getD i 0 := Ne.symm h12
          by_cases h23 : c2.getD i 0 = c3.getD i 0
          · -- c2[i] = c3[i]: d23 recurses
            have h23' : c3.getD i 0 ≠ c2.getD i 0 → False := fun h => h h23.symm
            simp_all; exact Nat.min_le_left _ _
          · -- c2[i] ≠ c3[i]: d23 = i+1
            have h23' : c3.getD i 0 ≠ c2.getD i 0 := Ne.symm h23
            simp_all
```
