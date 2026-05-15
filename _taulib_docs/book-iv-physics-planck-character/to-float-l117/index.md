---
{
  "projection_kind": "taulib_declaration",
  "title": "SectorLift.toFloat",
  "permalink": "/corpus/taulib/docs/book-iv-physics-planck-character/to-float-l117/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.PlanckCharacter`.",
  "declaration_id": "TauLib.BookIV.Physics.PlanckCharacter::SectorLift.toFloat",
  "declaration_slug": "to-float-l117",
  "kind": "def",
  "name": "SectorLift.toFloat",
  "module_name": "TauLib.BookIV.Physics.PlanckCharacter",
  "module_url": "/corpus/taulib/docs/book-iv-physics-planck-character/",
  "source_line_start": 117,
  "source_line_end": 125,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L117-L125",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.PlanckCharacter",
        "url": "/corpus/taulib/docs/book-iv-physics-planck-character/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L117-L125",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIV.Physics.PlanckCharacter](/corpus/taulib/docs/book-iv-physics-planck-character/)
- Source path: [`TauLib/BookIV/Physics/PlanckCharacter.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/PlanckCharacter.lean#L117-L125)
- Source range: L117-L125
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Float display for sector lift. -/
```

## Source Excerpt

```lean
def SectorLift.toFloat (s : SectorLift) : Float :=
  Float.ofNat s.target_numer / Float.ofNat s.target_denom

-- ============================================================
-- LOCAL ABBREVIATIONS (private in CouplingFormulas)
-- ============================================================

private abbrev oneMinusIota' : Nat := iotaD - iota   -- 658541
private abbrev onePlusIota' : Nat := iotaD + iota    -- 1341304
```
