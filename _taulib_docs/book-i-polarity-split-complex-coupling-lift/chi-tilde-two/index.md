---
{
  "projection_kind": "taulib_declaration",
  "title": "chiTilde_two",
  "permalink": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/chi-tilde-two/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.SplitComplexCouplingLift`.",
  "declaration_id": "TauLib.BookI.Polarity.SplitComplexCouplingLift::chiTilde_two",
  "declaration_slug": "chi-tilde-two",
  "kind": "theorem",
  "name": "chiTilde_two",
  "module_name": "TauLib.BookI.Polarity.SplitComplexCouplingLift",
  "module_url": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/",
  "source_line_start": 335,
  "source_line_end": 359,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L335-L359",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.SplitComplexCouplingLift",
        "url": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L335-L359",
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

- Module: [TauLib.BookI.Polarity.SplitComplexCouplingLift](/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/)
- Source path: [`TauLib/BookI/Polarity/SplitComplexCouplingLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L335-L359)
- Source range: L335-L359
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Ramification triviality at p = 2** (paper Prop 7.7
    `prop:ramification-triviality` first part).

    `χ̃(2) = 0` in `D` because the ramified prime is excluded from
    both B and C classes.  At the Lean level: `nuB(2) = nuB(1) = 0`
    (since `2 % 2 = 0` triggers the recursion to `2/2 = 1`), and
    similarly `nuC(2) = 0`. -/
```

## Source Excerpt

```lean
theorem chiTilde_two (B_class : Nat → Bool) :
    chiTilde B_class 2 = ⟨0, 0⟩ := by
  unfold chiTilde
  show (⟨((nuB B_class 2 : Nat) : Int), ((nuC B_class 2 : Nat) : Int)⟩ : SectorPair) =
       ⟨0, 0⟩
  -- nuB B_class 2 = nuB B_class 1 = 0 by definition unfolding (recursion hits base case)
  rfl

/-
**Ramification triviality at higher primorial depths note**: powers
of 2 are still ramification-trivial — `χ̃(4) = 0`, `χ̃(8) = 0`,
`χ̃(16) = 0`, etc. — because the recursive definition of `nuB` keeps
dividing by 2 without contributing to either B or C counts.

Lean's `rfl` does not reduce through the well-founded recursion
(`decreasing_by` blocks unfolding); the equalities hold
computationally (verified via `#eval` below) and the structural-level
claim is captured by `chiTilde_two` plus the monoid-homomorphism
argument from paper Prop 7.6 (deferred to a future wave with the full
prime-factorisation infrastructure).
-/

/-- **Trace at zero**: `Tr_+(⟨0, 0⟩) = 0`. -/
@[simp] theorem SectorPair.trPlus_zero :
    SectorPair.trPlus ⟨0, 0⟩ = 0 := rfl
```
