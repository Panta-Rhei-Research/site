---
{
  "projection_kind": "taulib_declaration",
  "title": "chiTilde",
  "permalink": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/chi-tilde/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.SplitComplexCouplingLift`.",
  "declaration_id": "TauLib.BookI.Polarity.SplitComplexCouplingLift::chiTilde",
  "declaration_slug": "chi-tilde",
  "kind": "def",
  "name": "chiTilde",
  "module_name": "TauLib.BookI.Polarity.SplitComplexCouplingLift",
  "module_url": "/verify/taulib/docs/book-i-polarity-split-complex-coupling-lift/",
  "source_line_start": 307,
  "source_line_end": 322,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L307-L322",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L307-L322",
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
- Source path: [`TauLib/BookI/Polarity/SplitComplexCouplingLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L307-L322)
- Source range: L307-L322
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Split-complex prime polarity lift** (paper Def 7.5
    `def:chi-tilde`):

      `χ̃(n) := ν_B(n) · e_+ + ν_C(n) · e_-`

    rendered as `SectorPair ⟨ν_B(n), ν_C(n)⟩`.  At the abstract
    structural level we keep the B/C classification a parameter;
    Wave 18 will instantiate with the Legendre(2/p) classifier. -/
```

## Source Excerpt

```lean
def chiTilde (B_class : Nat → Bool) (n : Nat) : SectorPair :=
  ⟨(nuB B_class n : Int), (nuC B_class n : Int)⟩

@[simp] theorem chiTilde_zero (B_class : Nat → Bool) :
    chiTilde B_class 0 = ⟨0, 0⟩ := by
  unfold chiTilde
  show (⟨((nuB B_class 0 : Nat) : Int), ((nuC B_class 0 : Nat) : Int)⟩ : SectorPair) =
       ⟨0, 0⟩
  rfl

@[simp] theorem chiTilde_one (B_class : Nat → Bool) :
    chiTilde B_class 1 = ⟨0, 0⟩ := by
  unfold chiTilde
  show (⟨((nuB B_class 1 : Nat) : Int), ((nuC B_class 1 : Nat) : Int)⟩ : SectorPair) =
       ⟨0, 0⟩
  rfl
```
