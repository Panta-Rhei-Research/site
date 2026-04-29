---
{
  "projection_kind": "taulib_declaration",
  "title": "character_hartogs_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/character-hartogs-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.MutualDetermination`.",
  "declaration_id": "TauLib.BookII.Hartogs.MutualDetermination::character_hartogs_check",
  "declaration_slug": "character-hartogs-check",
  "kind": "def",
  "name": "character_hartogs_check",
  "module_name": "TauLib.BookII.Hartogs.MutualDetermination",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/",
  "source_line_start": 230,
  "source_line_end": 231,
  "registry_ids": [
    "II.L05"
  ],
  "related_registry_items": [
    {
      "id": "II.L05",
      "title": "Character-Hartogs Equivalence",
      "url": "/registry/object/II.L05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L230-L231",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.MutualDetermination",
        "url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L230-L231",
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

- Module: [TauLib.BookII.Hartogs.MutualDetermination](/verify/taulib/docs/book-ii-hartogs-mutual-determination/)
- Source path: [`TauLib/BookII/Hartogs/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L230-L231)
- Source range: L230-L231
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L05` — Character-Hartogs Equivalence

## Immediate Comment / Docstring

```lean
/-- [II.L05] Character <-> Hartogs:
    Character data determines Hartogs extension. The bipolar character
    assignment determines BndLift, and BndLift is tower-coherent. -/
```

## Source Excerpt

```lean
def character_hartogs_check (bound db : TauIdx) : Bool :=
  boundary_character_check bound db && hartogs_check bound db
```
