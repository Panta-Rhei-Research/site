---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_algebra_satisfies_C1_C4",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/boundary-algebra-satisfies-c1-c4/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H4UniquenessElliptic`.",
  "declaration_id": "TauLib.BookI.Polarity.H4UniquenessElliptic::boundary_algebra_satisfies_C1_C4",
  "declaration_slug": "boundary-algebra-satisfies-c1-c4",
  "kind": "theorem",
  "name": "boundary_algebra_satisfies_C1_C4",
  "module_name": "TauLib.BookI.Polarity.H4UniquenessElliptic",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/",
  "source_line_start": 143,
  "source_line_end": 158,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L143-L158",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.H4UniquenessElliptic",
        "url": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L143-L158",
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

- Module: [TauLib.BookI.Polarity.H4UniquenessElliptic](/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/)
- Source path: [`TauLib/BookI/Polarity/H4UniquenessElliptic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L143-L158)
- Source range: L143-L158
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The C1-C4 axioms verified for SplitComplex** (paper Def
    bd-axioms).

    Records the four structural constraints at the concrete
    SectorPair level:
    - (C1) Binary rank: SectorPair has b_sector + c_sector,
      decomposable into rank-1 factors.
    - (C2) Commutativity: SectorPair.mul is commutative
      (componentwise multiplication).
    - (C3) Idempotent pair: e_plus_sector + e_minus_sector
      = ⟨1, 1⟩ = 1, e_plus_sector * e_minus_sector = 0.
    - (C4) Involution swap: sectorSigma e_plus = e_minus.

    Each clause is verified by `decide` / `rfl` at the
    component level. -/
```

## Source Excerpt

```lean
theorem boundary_algebra_satisfies_C1_C4 :
    -- C2 (commutativity) on the canonical idempotents
    SectorPair.mul e_plus_sector e_minus_sector =
    SectorPair.mul e_minus_sector e_plus_sector ∧
    -- C3 (idempotent pair):
    -- (a) e_+ + e_- = 1
    SectorPair.add e_plus_sector e_minus_sector = ⟨1, 1⟩ ∧
    -- (b) e_+ · e_- = 0
    SectorPair.mul e_plus_sector e_minus_sector = ⟨0, 0⟩ ∧
    -- (c) e_+² = e_+ (idempotency)
    SectorPair.mul e_plus_sector e_plus_sector = e_plus_sector ∧
    -- (d) e_-² = e_-
    SectorPair.mul e_minus_sector e_minus_sector = e_minus_sector ∧
    -- C4 (involution swap)
    sectorSigma e_plus_sector = e_minus_sector := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;> rfl
```
