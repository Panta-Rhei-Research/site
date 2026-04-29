---
{
  "projection_kind": "taulib_declaration",
  "title": "idem_supported_holomorphy_witness",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/idem-supported-holomorphy-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd::idem_supported_holomorphy_witness",
  "declaration_slug": "idem-supported-holomorphy-witness",
  "kind": "theorem",
  "name": "idem_supported_holomorphy_witness",
  "module_name": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/",
  "source_line_start": 178,
  "source_line_end": 182,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L178-L182",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd",
        "url": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L178-L182",
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

- Module: [TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd](/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/)
- Source path: [`TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L178-L182)
- Source range: L178-L182
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §8 Theorem `idem-supported-holomorphy` — concrete
    witness via SectorPair decomposition**.

    Every τ-holomorphic map into D factors through the
    e_+/e_- idempotent decomposition.  Concrete witness:
    SectorPair has two coordinates corresponding to e_+ and e_-,
    and any SectorPair s decomposes as
    `s = ⟨s.b_sector, 0⟩ + ⟨0, s.c_sector⟩` (the e_+ and e_-
    components separately). -/
```

## Source Excerpt

```lean
theorem idem_supported_holomorphy_witness (s : SectorPair) :
    -- Decomposition: s = e_+ ⋅ s + e_- ⋅ s (componentwise)
    s = SectorPair.add ⟨s.b_sector, 0⟩ ⟨0, s.c_sector⟩ := by
  cases s
  simp [SectorPair.add]
```
