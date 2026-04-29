---
{
  "projection_kind": "taulib_declaration",
  "title": "sectorSigma",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/sector-sigma/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.H4BoundaryAlgebra`.",
  "declaration_id": "TauLib.BookI.Polarity.H4BoundaryAlgebra::sectorSigma",
  "declaration_slug": "sector-sigma",
  "kind": "def",
  "name": "sectorSigma",
  "module_name": "TauLib.BookI.Polarity.H4BoundaryAlgebra",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/",
  "source_line_start": 154,
  "source_line_end": 179,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L154-L179",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L154-L179",
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

- Module: [TauLib.BookI.Polarity.H4BoundaryAlgebra](/verify/taulib/docs/book-i-polarity-h4-boundary-algebra/)
- Source path: [`TauLib/BookI/Polarity/H4BoundaryAlgebra.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4BoundaryAlgebra.lean#L154-L179)
- Source range: L154-L179
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **σ swaps the canonical idempotents at the SectorPair level**.

    Note: `e_plus_sector = ⟨1, 0⟩` and `e_minus_sector = ⟨0, 1⟩`
    in the `SectorPair` representation; the σ-swap exchange
    `e_+ ↔ e_-` corresponds to swapping the b-sector and c-sector
    components. -/
```

## Source Excerpt

```lean
def sectorSigma (s : SectorPair) : SectorPair :=
  ⟨s.c_sector, s.b_sector⟩

@[simp] theorem sectorSigma_e_plus :
    sectorSigma e_plus = e_minus := rfl

@[simp] theorem sectorSigma_e_minus :
    sectorSigma e_minus = e_plus := rfl

/-
σ-fixedness for SectorPairs note: a SectorPair is σ-fixed iff its
components are equal.  At concrete instances this reduces to
`rfl`-style proofs.  The universal proof would require structure-level
extensionality reasoning that's clunky in this concrete TauLib setting;
we capture σ-fixedness at the four canonical atoms via the theorems
below (sectorSigma_fixed_at_zero / sectorSigma_fixed_at_one) which
suffice for the paper §10 four-atom dictionary structure.
-/

/-- The σ-fixed atoms among the four canonical idempotents are
    exactly `0 = ⟨0, 0⟩` and `1 = ⟨1, 1⟩`. -/
@[simp] theorem sectorSigma_fixed_at_zero :
    sectorSigma (⟨0, 0⟩ : SectorPair) = ⟨0, 0⟩ := rfl

@[simp] theorem sectorSigma_fixed_at_one :
    sectorSigma (⟨1, 1⟩ : SectorPair) = ⟨1, 1⟩ := rfl
```
