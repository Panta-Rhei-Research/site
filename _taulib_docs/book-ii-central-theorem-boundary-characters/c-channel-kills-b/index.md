---
{
  "projection_kind": "taulib_declaration",
  "title": "c_channel_kills_b",
  "permalink": "/corpus/taulib/docs/book-ii-central-theorem-boundary-characters/c-channel-kills-b/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.BoundaryCharacters`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.BoundaryCharacters::c_channel_kills_b",
  "declaration_slug": "c-channel-kills-b",
  "kind": "theorem",
  "name": "c_channel_kills_b",
  "module_name": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
  "module_url": "/corpus/taulib/docs/book-ii-central-theorem-boundary-characters/",
  "source_line_start": 322,
  "source_line_end": 324,
  "registry_ids": [
    "II.D59"
  ],
  "related_registry_items": [
    {
      "id": "II.D59",
      "title": "Idempotent-Supported Character",
      "url": "/registry/object/II.D59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L322-L324",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.BoundaryCharacters",
        "url": "/corpus/taulib/docs/book-ii-central-theorem-boundary-characters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L322-L324",
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

- Module: [TauLib.BookII.CentralTheorem.BoundaryCharacters](/corpus/taulib/docs/book-ii-central-theorem-boundary-characters/)
- Source path: [`TauLib/BookII/CentralTheorem/BoundaryCharacters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/BoundaryCharacters.lean#L322-L324)
- Source range: L322-L324
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `II.D59` — Idempotent-Supported Character

## Immediate Comment / Docstring

```lean
/-- [II.D59] The C-channel projection kills the B-sector. -/
```

## Source Excerpt

```lean
theorem c_channel_kills_b (sp : SectorPair) :
    (SectorPair.mul e_minus_sector sp).b_sector = 0 := by
  simp [SectorPair.mul, e_minus_sector]
```
