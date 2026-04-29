---
{
  "projection_kind": "taulib_declaration",
  "title": "interior_projection_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/interior-projection-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.JReplacesI`.",
  "declaration_id": "TauLib.BookII.Transcendentals.JReplacesI::interior_projection_check",
  "declaration_slug": "interior-projection-check",
  "kind": "def",
  "name": "interior_projection_check",
  "module_name": "TauLib.BookII.Transcendentals.JReplacesI",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/",
  "source_line_start": 80,
  "source_line_end": 87,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L80-L87",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.JReplacesI",
        "url": "/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L80-L87",
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

- Module: [TauLib.BookII.Transcendentals.JReplacesI](/verify/taulib/docs/book-ii-transcendentals-jreplaces-i/)
- Source path: [`TauLib/BookII/Transcendentals/JReplacesI.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/JReplacesI.lean#L80-L87)
- Source range: L80-L87
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Interior projection: idempotent action on interior bipolar pairs.
    e_+ * (b, c) = (b, 0): keeps B-sector, kills C-sector.
    e_- * (b, c) = (0, c): kills B-sector, keeps C-sector. -/
```

## Source Excerpt

```lean
def interior_projection_check : Bool :=
  -- e_+ * (3, 2) = (3, 0)
  SectorPair.mul e_plus_sector ⟨3, 2⟩ == ⟨3, 0⟩ &&
  -- e_- * (3, 2) = (0, 2)
  SectorPair.mul e_minus_sector ⟨3, 2⟩ == ⟨0, 2⟩ &&
  -- Sum recovers original: (3, 0) + (0, 2) = (3, 2)
  SectorPair.add (SectorPair.mul e_plus_sector ⟨3, 2⟩)
                 (SectorPair.mul e_minus_sector ⟨3, 2⟩) == ⟨3, 2⟩
```
