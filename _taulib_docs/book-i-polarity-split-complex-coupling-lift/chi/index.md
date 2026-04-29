---
{
  "projection_kind": "taulib_declaration",
  "title": "chi",
  "permalink": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/chi/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.SplitComplexCouplingLift`.",
  "declaration_id": "TauLib.BookI.Polarity.SplitComplexCouplingLift::chi",
  "declaration_slug": "chi",
  "kind": "def",
  "name": "chi",
  "module_name": "TauLib.BookI.Polarity.SplitComplexCouplingLift",
  "module_url": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/",
  "source_line_start": 241,
  "source_line_end": 259,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L241-L259",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L241-L259",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookI/Polarity/SplitComplexCouplingLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L241-L259)
- Source range: L241-L259
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Prime polarity character** χ (paper Def 7.4
    `def:polarity-chi`).

    Parameterised over an abstract B-class predicate `B_class :
    Nat → Bool` (rendered concretely as `Legendre(2/p) = +1` in
    Wave 18 via the prime-polarity paper).  At the structural
    level:

      `χ_{B_class}(p) := if B_class p then 1 else if (p ≠ 2 ∧ ¬B_class p) then -1 else 0`.

    The `p = 2` case is hard-wired to 0 (ramification convention),
    matching paper's `ℙ_ram = {2}` partition.  Other primes are
    classified +1 (B) or -1 (C) by the `B_class` predicate. -/
```

## Source Excerpt

```lean
def chi (B_class : Nat → Bool) (p : Nat) : Int :=
  match p with
  | 0 => 0
  | 1 => 0
  | 2 => 0
  | _ => if B_class p then 1 else -1

/-- **Unit-glue**: χ(0) = 0. -/
@[simp] theorem chi_zero (B_class : Nat → Bool) : chi B_class 0 = 0 := rfl

/-- **Unit-glue**: χ(1) = 0 (paper Remark `unit-glue`).
    The multiplicative unit must map to the neutral mediator of
    the idempotent decomposition. -/
@[simp] theorem chi_one (B_class : Nat → Bool) : chi B_class 1 = 0 := rfl

/-- **Ramification at the prime level**: `χ(2) = 0`.  This is
    the paper's "ramified prime contributes identically zero"
    (paper Def 7.4 `ℙ_ram = {2}` clause). -/
@[simp] theorem chi_two (B_class : Nat → Bool) : chi B_class 2 = 0 := rfl
```
