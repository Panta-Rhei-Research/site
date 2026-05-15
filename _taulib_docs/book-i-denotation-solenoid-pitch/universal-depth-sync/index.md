---
{
  "projection_kind": "taulib_declaration",
  "title": "universal_depth_sync",
  "permalink": "/corpus/taulib/docs/book-i-denotation-solenoid-pitch/universal-depth-sync/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.SolenoidPitch`.",
  "declaration_id": "TauLib.BookI.Denotation.SolenoidPitch::universal_depth_sync",
  "declaration_slug": "universal-depth-sync",
  "kind": "theorem",
  "name": "universal_depth_sync",
  "module_name": "TauLib.BookI.Denotation.SolenoidPitch",
  "module_url": "/corpus/taulib/docs/book-i-denotation-solenoid-pitch/",
  "source_line_start": 148,
  "source_line_end": 151,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L148-L151",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.SolenoidPitch",
        "url": "/corpus/taulib/docs/book-i-denotation-solenoid-pitch/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L148-L151",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Denotation.SolenoidPitch](/corpus/taulib/docs/book-i-denotation-solenoid-pitch/)
- Source path: [`TauLib/BookI/Denotation/SolenoidPitch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L148-L151)
- Source range: L148-L151
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All four non-ω generators advance at the same rate under ρ.
    This extends depth_sync to the full generator set. -/
```

## Source Excerpt

```lean
theorem universal_depth_sync (g h : Generator)
    (_hg : g ≠ omega) (_hh : h ≠ omega) (n : TauIdx) :
    (RT g n).depth = (RT h n).depth := by
  rfl
```
