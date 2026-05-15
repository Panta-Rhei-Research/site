---
{
  "projection_kind": "taulib_declaration",
  "title": "ladder_saturation",
  "permalink": "/corpus/taulib/docs/book-i-orbit-ladder/ladder-saturation/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Ladder`.",
  "declaration_id": "TauLib.BookI.Orbit.Ladder::ladder_saturation",
  "declaration_slug": "ladder-saturation",
  "kind": "theorem",
  "name": "ladder_saturation",
  "module_name": "TauLib.BookI.Orbit.Ladder",
  "module_url": "/corpus/taulib/docs/book-i-orbit-ladder/",
  "source_line_start": 142,
  "source_line_end": 144,
  "registry_ids": [
    "I.T02"
  ],
  "related_registry_items": [
    {
      "id": "I.T02",
      "title": "Iterator Ladder Saturation",
      "url": "/registry/object/I.T02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L142-L144",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Ladder",
        "url": "/corpus/taulib/docs/book-i-orbit-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L142-L144",
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

- Module: [TauLib.BookI.Orbit.Ladder](/corpus/taulib/docs/book-i-orbit-ladder/)
- Source path: [`TauLib/BookI/Orbit/Ladder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L142-L144)
- Source range: L142-L144
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `I.T02` — Iterator Ladder Saturation

## Immediate Comment / Docstring

```lean
/-- [I.T02] The iterator ladder saturates at 4 levels:
    exactly 3 solenoidal generators exist (solenoidalGenerators.length = 3),
    so exactly 3 rewiring levels can be canonically assigned,
    giving 4 total operation levels (ρ + 3 rewirings).

    The 4th rewiring level (pentation/level 4) has no channel. -/
```

## Source Excerpt

```lean
theorem ladder_saturation :
    solenoidalGenerators.length = 3 ∧ ladderChannel .tet_level = none := by
  exact ⟨by rfl, by rfl⟩
```
