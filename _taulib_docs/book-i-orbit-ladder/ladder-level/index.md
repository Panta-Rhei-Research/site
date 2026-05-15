---
{
  "projection_kind": "taulib_declaration",
  "title": "LadderLevel",
  "permalink": "/corpus/taulib/docs/book-i-orbit-ladder/ladder-level/",
  "summary_short": "`inductive` declaration in `TauLib.BookI.Orbit.Ladder`.",
  "declaration_id": "TauLib.BookI.Orbit.Ladder::LadderLevel",
  "declaration_slug": "ladder-level",
  "kind": "inductive",
  "name": "LadderLevel",
  "module_name": "TauLib.BookI.Orbit.Ladder",
  "module_url": "/corpus/taulib/docs/book-i-orbit-ladder/",
  "source_line_start": 43,
  "source_line_end": 49,
  "registry_ids": [
    "I.D06"
  ],
  "related_registry_items": [
    {
      "id": "I.D06",
      "title": "Iterator Ladder",
      "url": "/registry/object/I.D06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L43-L49",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L43-L49",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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
- Source path: [`TauLib/BookI/Orbit/Ladder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Ladder.lean#L43-L49)
- Source range: L43-L49
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `I.D06` — Iterator Ladder

## Immediate Comment / Docstring

```lean
/-- [I.D06] The 5 hyperoperation levels (ρ through tetration).
    Only levels 0-3 have canonical orbit channel assignments. -/
```

## Source Excerpt

```lean
inductive LadderLevel : Type where
  | rho_level    : LadderLevel  -- Level 0: ρ
  | add_level    : LadderLevel  -- Level 1: iterated ρ = addition
  | mul_level    : LadderLevel  -- Level 2: iterated addition = multiplication
  | exp_level    : LadderLevel  -- Level 3: iterated multiplication = exponentiation
  | tet_level    : LadderLevel  -- Level 4: iterated exponentiation = tetration
  deriving DecidableEq, Repr
```
