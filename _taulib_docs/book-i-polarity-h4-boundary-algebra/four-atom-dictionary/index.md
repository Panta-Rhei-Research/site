---
{
  "projection_kind": "taulib_declaration",
  "title": "four_atom_dictionary",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/four-atom-dictionary/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H4BoundaryAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.H4BoundaryAlgebra::four_atom_dictionary",
  "declaration_slug": "four-atom-dictionary",
  "kind": "theorem",
  "name": "four_atom_dictionary",
  "module_name": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/",
  "source_line_start": 193,
  "source_line_end": 206,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L193-L206",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
        "url": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L193-L206",
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

- Module: [TauLib.BookI.Polarity.H4BoundaryAlgebra](/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/)
- Source path: [`TauLib/BookI/Polarity/H4BoundaryAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L193-L206)
- Source range: L193-L206
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Lemma four-atoms**: the canonical σ-equivariant Boolean
    sublattice `B_σ(D)` has exactly four elements
    `{0, e_+, e_-, 1}` at the SectorPair level.

    The structural correspondence to TauLib's `Truth4` (Logic.Truth4)
    is direct: each Truth4 atom maps to one element of B_σ(D) via
    `Truth4.toSectorPair`.  This wave records the correspondence
    formally. -/
```

## Source Excerpt

```lean
theorem four_atom_dictionary (t : Truth4) :
    Truth4.toSectorPair t = match t with
      | Truth4.T => SectorPair.mk 1 1   -- α-total → 1 = e_+ + e_-
      | Truth4.F => SectorPair.mk 0 0   -- α-null → 0 = the zero
      | Truth4.B => e_plus_sector       -- γ → e_+ (B-lobe)
      | Truth4.N => e_minus_sector := by  -- η → e_- (C-lobe)
  cases t <;> rfl

/-- **The four atoms of B_σ(D) realised on Truth4**: each Truth4
    constructor maps to a specific SectorPair element. -/
@[simp] theorem four_atom_T : Truth4.toSectorPair Truth4.T = ⟨1, 1⟩ := rfl
@[simp] theorem four_atom_F : Truth4.toSectorPair Truth4.F = ⟨0, 0⟩ := rfl
@[simp] theorem four_atom_B : Truth4.toSectorPair Truth4.B = e_plus_sector := rfl
@[simp] theorem four_atom_N : Truth4.toSectorPair Truth4.N = e_minus_sector := rfl
```
