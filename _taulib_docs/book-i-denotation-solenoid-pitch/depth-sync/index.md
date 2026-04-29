---
{
  "projection_kind": "taulib_declaration",
  "title": "depth_sync",
  "permalink": "/verify/taulib/docs/book-i-denotation-solenoid-pitch/depth-sync/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.SolenoidPitch`.",
  "declaration_id": "TauLib.BookI.Denotation.SolenoidPitch::depth_sync",
  "declaration_slug": "depth-sync",
  "kind": "theorem",
  "name": "depth_sync",
  "module_name": "TauLib.BookI.Denotation.SolenoidPitch",
  "module_url": "/verify/taulib/docs/book-i-denotation-solenoid-pitch/",
  "source_line_start": 67,
  "source_line_end": 69,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L67-L69",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L67-L69",
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
- Source path: [`TauLib/BookI/Denotation/SolenoidPitch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L67-L69)
- Source range: L67-L69
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Depth synchronization**: For any two non-ω generators g and h,
    RT_g(n) and RT_h(n) have the same depth. In other words, ρ advances
    all orbit rays at exactly the same rate.

    This is the structural content of "all clocks tick at the same rate." -/
```

## Source Excerpt

```lean
theorem depth_sync (g h : Generator) (n : TauIdx) :
    (RT g n).depth = (RT h n).depth := by
  rfl
```
