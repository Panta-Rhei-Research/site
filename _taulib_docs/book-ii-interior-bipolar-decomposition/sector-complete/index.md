---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_complete",
  "permalink": "/verify/taulib/docs/book-ii-interior-bipolar-decomposition/sector-complete/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Interior.BipolarDecomposition`.",
  "declaration_id": "TauLib.BookII.Interior.BipolarDecomposition::sector_complete",
  "declaration_slug": "sector-complete",
  "kind": "theorem",
  "name": "sector_complete",
  "module_name": "TauLib.BookII.Interior.BipolarDecomposition",
  "module_url": "/verify/taulib/docs/book-ii-interior-bipolar-decomposition/",
  "source_line_start": 83,
  "source_line_end": 89,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/BipolarDecomposition.lean#L83-L89",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.BipolarDecomposition",
        "url": "/verify/taulib/docs/book-ii-interior-bipolar-decomposition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/BipolarDecomposition.lean#L83-L89",
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

- Module: [TauLib.BookII.Interior.BipolarDecomposition](/verify/taulib/docs/book-ii-interior-bipolar-decomposition/)
- Source path: [`TauLib/BookII/Interior/BipolarDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/BipolarDecomposition.lean#L83-L89)
- Source range: L83-L89
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.P02, clause 2] Completeness:
    The interior bipolar decomposition recovers the full point data.
    s₊ + s₋ (in appropriate sense) gives back (B, C). -/
```

## Source Excerpt

```lean
theorem sector_complete (p : TauAdmissiblePoint) :
    SectorPair.add
      (SectorPair.mul e_plus_sector (interior_bipolar p))
      (SectorPair.mul e_minus_sector (interior_bipolar p)) =
    interior_bipolar p := by
  simp [SectorPair.add, SectorPair.mul, e_plus_sector, e_minus_sector,
        interior_bipolar]
```
