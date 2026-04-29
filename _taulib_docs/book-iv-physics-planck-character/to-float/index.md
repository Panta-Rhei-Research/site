---
{
  "projection_kind": "taulib_declaration",
  "title": "PlanckCharacter.toFloat",
  "permalink": "/verify/taulib/docs/book-iv-physics-planck-character/to-float/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.PlanckCharacter`.",
  "declaration_id": "TauLib.BookIV.Physics.PlanckCharacter::PlanckCharacter.toFloat",
  "declaration_slug": "to-float",
  "kind": "def",
  "name": "PlanckCharacter.toFloat",
  "module_name": "TauLib.BookIV.Physics.PlanckCharacter",
  "module_url": "/verify/taulib/docs/book-iv-physics-planck-character/",
  "source_line_start": 84,
  "source_line_end": 85,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L84-L85",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.PlanckCharacter",
        "url": "/verify/taulib/docs/book-iv-physics-planck-character/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L84-L85",
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

- Module: [TauLib.BookIV.Physics.PlanckCharacter](/verify/taulib/docs/book-iv-physics-planck-character/)
- Source path: [`TauLib/BookIV/Physics/PlanckCharacter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L84-L85)
- Source range: L84-L85
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Float display for Planck character. -/
```

## Source Excerpt

```lean
def PlanckCharacter.toFloat (h : PlanckCharacter) : Float :=
  Float.ofNat h.numer / Float.ofNat h.denom
```
