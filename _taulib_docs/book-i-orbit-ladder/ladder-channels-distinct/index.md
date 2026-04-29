---
{
  "projection_kind": "taulib_declaration",
  "title": "ladder_channels_distinct",
  "permalink": "/verify/taulib/docs/book-i-orbit-ladder/ladder-channels-distinct/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Ladder`.",
  "declaration_id": "TauLib.BookI.Orbit.Ladder::ladder_channels_distinct",
  "declaration_slug": "ladder-channels-distinct",
  "kind": "theorem",
  "name": "ladder_channels_distinct",
  "module_name": "TauLib.BookI.Orbit.Ladder",
  "module_url": "/verify/taulib/docs/book-i-orbit-ladder/",
  "source_line_start": 154,
  "source_line_end": 158,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L154-L158",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Ladder",
        "url": "/verify/taulib/docs/book-i-orbit-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L154-L158",
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

- Module: [TauLib.BookI.Orbit.Ladder](/verify/taulib/docs/book-i-orbit-ladder/)
- Source path: [`TauLib/BookI/Orbit/Ladder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L154-L158)
- Source range: L154-L158
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The assigned channels are pairwise distinct. -/
```

## Source Excerpt

```lean
theorem ladder_channels_distinct :
    pi ≠ gamma ∧ pi ≠ eta ∧ gamma ≠ eta := by
  exact ⟨by decide, by decide, by decide⟩

end Tau.Orbit
```
