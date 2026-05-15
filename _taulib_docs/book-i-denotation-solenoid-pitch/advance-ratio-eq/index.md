---
{
  "projection_kind": "taulib_declaration",
  "title": "advance_ratio_eq",
  "permalink": "/corpus/taulib/docs/book-i-denotation-solenoid-pitch/advance-ratio-eq/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.SolenoidPitch`.",
  "declaration_id": "TauLib.BookI.Denotation.SolenoidPitch::advance_ratio_eq",
  "declaration_slug": "advance-ratio-eq",
  "kind": "theorem",
  "name": "advance_ratio_eq",
  "module_name": "TauLib.BookI.Denotation.SolenoidPitch",
  "module_url": "/corpus/taulib/docs/book-i-denotation-solenoid-pitch/",
  "source_line_start": 105,
  "source_line_end": 108,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L105-L108",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L105-L108",
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
- Source path: [`TauLib/BookI/Denotation/SolenoidPitch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L105-L108)
- Source range: L105-L108
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The advances are equal: α and π gain the same depth per ρ-step. -/
```

## Source Excerpt

```lean
theorem advance_ratio_eq (n : TauIdx) :
    (RT alpha (n + 1)).depth - (RT alpha n).depth =
    (RT pi (n + 1)).depth - (RT pi n).depth := by
  rfl
```
