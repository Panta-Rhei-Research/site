---
{
  "projection_kind": "taulib_declaration",
  "title": "MassIndex.toFloat",
  "permalink": "/corpus/taulib/docs/book-iv-physics-mass-energy/to-float/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.MassEnergy`.",
  "declaration_id": "TauLib.BookIV.Physics.MassEnergy::MassIndex.toFloat",
  "declaration_slug": "to-float",
  "kind": "def",
  "name": "MassIndex.toFloat",
  "module_name": "TauLib.BookIV.Physics.MassEnergy",
  "module_url": "/corpus/taulib/docs/book-iv-physics-mass-energy/",
  "source_line_start": 89,
  "source_line_end": 90,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L89-L90",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.MassEnergy",
        "url": "/corpus/taulib/docs/book-iv-physics-mass-energy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L89-L90",
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

- Module: [TauLib.BookIV.Physics.MassEnergy](/corpus/taulib/docs/book-iv-physics-mass-energy/)
- Source path: [`TauLib/BookIV/Physics/MassEnergy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/MassEnergy.lean#L89-L90)
- Source range: L89-L90
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Float display for mass index. -/
```

## Source Excerpt

```lean
def MassIndex.toFloat (m : MassIndex) : Float :=
  Float.ofNat m.numer / Float.ofNat m.denom
```
