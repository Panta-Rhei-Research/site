---
{
  "projection_kind": "taulib_declaration",
  "title": "lemniscate_sector_idem_check",
  "permalink": "/corpus/taulib/docs/book-ii-interior-omega-readout/lemniscate-sector-idem-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.OmegaReadout`.",
  "declaration_id": "TauLib.BookII.Interior.OmegaReadout::lemniscate_sector_idem_check",
  "declaration_slug": "lemniscate-sector-idem-check",
  "kind": "def",
  "name": "lemniscate_sector_idem_check",
  "module_name": "TauLib.BookII.Interior.OmegaReadout",
  "module_url": "/corpus/taulib/docs/book-ii-interior-omega-readout/",
  "source_line_start": 120,
  "source_line_end": 132,
  "registry_ids": [
    "II.P01"
  ],
  "related_registry_items": [
    {
      "id": "II.P01",
      "title": "Lemniscate as Coordinate Limit",
      "url": "/registry/object/II.P01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L120-L132",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.OmegaReadout",
        "url": "/corpus/taulib/docs/book-ii-interior-omega-readout/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L120-L132",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Interior.OmegaReadout](/corpus/taulib/docs/book-ii-interior-omega-readout/)
- Source path: [`TauLib/BookII/Interior/OmegaReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L120-L132)
- Source range: L120-L132
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `II.P01` — Lemniscate as Coordinate Limit

## Immediate Comment / Docstring

```lean
/-- [II.P01] The three fiber limit types correspond to the algebraic
    lemniscate structure:
    - B-dominant → e₊-lobe (I.D21 e₊ idempotent)
    - C-dominant → e₋-lobe (I.D21 e₋ idempotent)
    - Balanced   → crossing point (node where both sectors active)

    Verification: sector assignment is idempotent-compatible. -/
```

## Source Excerpt

```lean
def lemniscate_sector_idem_check : Bool :=
  -- e₊-sector assignment: e₊² = e₊
  SectorPair.mul (dominance_to_sector .b_dominant)
                 (dominance_to_sector .b_dominant) ==
    dominance_to_sector .b_dominant &&
  -- e₋-sector assignment: e₋² = e₋
  SectorPair.mul (dominance_to_sector .c_dominant)
                 (dominance_to_sector .c_dominant) ==
    dominance_to_sector .c_dominant &&
  -- orthogonality: e₊ · e₋ = 0
  SectorPair.mul (dominance_to_sector .b_dominant)
                 (dominance_to_sector .c_dominant) ==
    ⟨0, 0⟩
```
