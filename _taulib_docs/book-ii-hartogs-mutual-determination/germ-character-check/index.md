---
{
  "projection_kind": "taulib_declaration",
  "title": "germ_character_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/germ-character-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.MutualDetermination`.",
  "declaration_id": "TauLib.BookII.Hartogs.MutualDetermination::germ_character_check",
  "declaration_slug": "germ-character-check",
  "kind": "def",
  "name": "germ_character_check",
  "module_name": "TauLib.BookII.Hartogs.MutualDetermination",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-mutual-determination/",
  "source_line_start": 224,
  "source_line_end": 225,
  "registry_ids": [
    "II.L04"
  ],
  "related_registry_items": [
    {
      "id": "II.L04",
      "title": "Germ-Character Equivalence",
      "url": "/registry/object/II.L04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L224-L225",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L224-L225",
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
- Source path: [`TauLib/BookII/Hartogs/MutualDetermination.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/MutualDetermination.lean#L224-L225)
- Source range: L224-L225
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L04` — Germ-Character Equivalence

## Immediate Comment / Docstring

```lean
/-- [II.L04] Omega-germ <-> Character:
    Germ data determines character data. The omega-germ carries
    the full profinite element, and the boundary character is
    extracted via the bipolar idempotent decomposition. -/
```

## Source Excerpt

```lean
def germ_character_check (bound db : TauIdx) : Bool :=
  omega_germ_check bound db && boundary_character_check bound db
```
