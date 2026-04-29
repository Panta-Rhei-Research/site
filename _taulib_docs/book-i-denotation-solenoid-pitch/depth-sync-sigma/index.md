---
{
  "projection_kind": "taulib_declaration",
  "title": "depth_sync_sigma",
  "permalink": "/verify/taulib/docs/book-i-denotation-solenoid-pitch/depth-sync-sigma/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.SolenoidPitch`.",
  "declaration_id": "TauLib.BookI.Denotation.SolenoidPitch::depth_sync_sigma",
  "declaration_slug": "depth-sync-sigma",
  "kind": "theorem",
  "name": "depth_sync_sigma",
  "module_name": "TauLib.BookI.Denotation.SolenoidPitch",
  "module_url": "/verify/taulib/docs/book-i-denotation-solenoid-pitch/",
  "source_line_start": 74,
  "source_line_end": 77,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L74-L77",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.SolenoidPitch",
        "url": "/verify/taulib/docs/book-i-denotation-solenoid-pitch/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L74-L77",
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

- Module: [TauLib.BookI.Denotation.SolenoidPitch](/verify/taulib/docs/book-i-denotation-solenoid-pitch/)
- Source path: [`TauLib/BookI/Denotation/SolenoidPitch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L74-L77)
- Source range: L74-L77
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Depth synchronization via σ: cross-orbit transport σ_{g,h} maps
    RT_g(n) to RT_h(n), preserving depth. Combines RT_sigma with the
    observation that both rank transfers produce the same depth. -/
```

## Source Excerpt

```lean
theorem depth_sync_sigma (g h : Generator) (hgh : g ≠ h) (n : TauIdx) :
    (sigma g h (RT g n)).depth = (RT g n).depth := by
  rw [RT_sigma g h hgh n]
  rfl
```
