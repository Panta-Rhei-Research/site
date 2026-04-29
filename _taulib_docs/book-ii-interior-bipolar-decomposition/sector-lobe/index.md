---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_lobe",
  "permalink": "/verify/taulib/docs/book-ii-interior-bipolar-decomposition/sector-lobe/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.BipolarDecomposition`.",
  "declaration_id": "TauLib.BookII.Interior.BipolarDecomposition::sector_lobe",
  "declaration_slug": "sector-lobe",
  "kind": "def",
  "name": "sector_lobe",
  "module_name": "TauLib.BookII.Interior.BipolarDecomposition",
  "module_url": "/verify/taulib/docs/book-ii-interior-bipolar-decomposition/",
  "source_line_start": 93,
  "source_line_end": 94,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/BipolarDecomposition.lean#L93-L94",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/BipolarDecomposition.lean#L93-L94",
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

- Module: [TauLib.BookII.Interior.BipolarDecomposition](/verify/taulib/docs/book-ii-interior-bipolar-decomposition/)
- Source path: [`TauLib/BookII/Interior/BipolarDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/BipolarDecomposition.lean#L93-L94)
- Source range: L93-L94
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.P02, clause 3] Fiber dominance recovery:
    Sector assignment determines which lobe of ℒ the point approaches. -/
```

## Source Excerpt

```lean
def sector_lobe (p : TauAdmissiblePoint) : FiberDominance :=
  p.fiber_dominance
```
