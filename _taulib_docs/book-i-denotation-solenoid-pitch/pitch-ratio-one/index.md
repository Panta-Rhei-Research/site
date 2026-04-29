---
{
  "projection_kind": "taulib_declaration",
  "title": "pitch_ratio_one",
  "permalink": "/verify/taulib/docs/book-i-denotation-solenoid-pitch/pitch-ratio-one/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.SolenoidPitch`.",
  "declaration_id": "TauLib.BookI.Denotation.SolenoidPitch::pitch_ratio_one",
  "declaration_slug": "pitch-ratio-one",
  "kind": "theorem",
  "name": "pitch_ratio_one",
  "module_name": "TauLib.BookI.Denotation.SolenoidPitch",
  "module_url": "/verify/taulib/docs/book-i-denotation-solenoid-pitch/",
  "source_line_start": 90,
  "source_line_end": 92,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L90-L92",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L90-L92",
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
- Source path: [`TauLib/BookI/Denotation/SolenoidPitch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L90-L92)
- Source range: L90-L92
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Pitch ratio one**: RT_α(n) and RT_π(n) have the same depth for all n.
    This is the α-to-π advance ratio = 1:

      dπ/dα = (dπ/dρ)/(dα/dρ) = 1/1 = 1.

    Each ρ-step advances α by 1 (K4_no_jump for α) and π by 1
    (K4_no_jump for π). The ratio is unity. -/
```

## Source Excerpt

```lean
theorem pitch_ratio_one (n : TauIdx) :
    (RT alpha n).depth = (RT pi n).depth := by
  rfl
```
