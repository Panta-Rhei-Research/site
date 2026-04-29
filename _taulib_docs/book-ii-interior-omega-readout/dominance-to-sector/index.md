---
{
  "projection_kind": "taulib_declaration",
  "title": "dominance_to_sector",
  "permalink": "/verify/taulib/docs/book-ii-interior-omega-readout/dominance-to-sector/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.OmegaReadout`.",
  "declaration_id": "TauLib.BookII.Interior.OmegaReadout::dominance_to_sector",
  "declaration_slug": "dominance-to-sector",
  "kind": "def",
  "name": "dominance_to_sector",
  "module_name": "TauLib.BookII.Interior.OmegaReadout",
  "module_url": "/verify/taulib/docs/book-ii-interior-omega-readout/",
  "source_line_start": 69,
  "source_line_end": 73,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L69-L73",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.OmegaReadout",
        "url": "/verify/taulib/docs/book-ii-interior-omega-readout/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L69-L73",
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

- Module: [TauLib.BookII.Interior.OmegaReadout](/verify/taulib/docs/book-ii-interior-omega-readout/)
- Source path: [`TauLib/BookII/Interior/OmegaReadout.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/OmegaReadout.lean#L69-L73)
- Source range: L69-L73
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Sector assignment from fiber dominance:
    B-dominant → e₊-sector, C-dominant → e₋-sector, balanced → both. -/
```

## Source Excerpt

```lean
def dominance_to_sector (fd : FiberDominance) : SectorPair :=
  match fd with
  | .b_dominant => e_plus_sector   -- ⟨1, 0⟩
  | .c_dominant => e_minus_sector  -- ⟨0, 1⟩
  | .balanced   => ⟨1, 1⟩         -- both sectors active
```
