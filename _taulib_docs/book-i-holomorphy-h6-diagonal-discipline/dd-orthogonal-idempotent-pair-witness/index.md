---
{
  "projection_kind": "taulib_declaration",
  "title": "dd_orthogonal_idempotent_pair_witness",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/dd-orthogonal-idempotent-pair-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6DiagonalDiscipline`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline::dd_orthogonal_idempotent_pair_witness",
  "declaration_slug": "dd-orthogonal-idempotent-pair-witness",
  "kind": "theorem",
  "name": "dd_orthogonal_idempotent_pair_witness",
  "module_name": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/",
  "source_line_start": 122,
  "source_line_end": 124,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L122-L124",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.H6DiagonalDiscipline",
        "url": "/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L122-L124",
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

- Module: [TauLib.BookI.Holomorphy.H6DiagonalDiscipline](/verify/taulib/docs/book-i-holomorphy-h6-diagonal-discipline/)
- Source path: [`TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6DiagonalDiscipline.lean#L122-L124)
- Source range: L122-L124
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §6 concrete witness — sector-orthogonality**:
    the canonical idempotent pair `(e_+, e_-)` of the boundary
    algebra `D = R[j]/(j²-1)` satisfies `e_+ · e_- = 0`.

    This IS the structural fact that the diagonal discipline
    protects: in elliptic `R[i]/(i²+1) ≅ ℂ`, no such pair
    exists — Wave 25's `elliptic_no_sigma_equivariant_idempotent_pair`.

    Repackaged from Wave 5-era `diagonal_free_protection` for
    paper-faithful Wave-27 H6 §6 synthesis. -/
```

## Source Excerpt

```lean
theorem dd_orthogonal_idempotent_pair_witness :
    SectorPair.mul e_plus_sector e_minus_sector = ⟨0, 0⟩ := by
  decide
```
