---
{
  "projection_kind": "taulib_declaration",
  "title": "conservation_from_sectors",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-classical-illusion/conservation-from-sectors/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.ClassicalIllusion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.ClassicalIllusion::conservation_from_sectors",
  "declaration_slug": "conservation-from-sectors",
  "kind": "theorem",
  "name": "conservation_from_sectors",
  "module_name": "TauLib.BookV.Astrophysics.ClassicalIllusion",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-classical-illusion/",
  "source_line_start": 200,
  "source_line_end": 202,
  "registry_ids": [
    "V.P58"
  ],
  "related_registry_items": [
    {
      "id": "V.P58",
      "title": "Newton's First Law as Limit --- V.P22",
      "url": "/registry/object/V.P58/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L200-L202",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.ClassicalIllusion",
        "url": "/verify/taulib/docs/book-v-astrophysics-classical-illusion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L200-L202",
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

- Module: [TauLib.BookV.Astrophysics.ClassicalIllusion](/verify/taulib/docs/book-v-astrophysics-classical-illusion/)
- Source path: [`TauLib/BookV/Astrophysics/ClassicalIllusion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/ClassicalIllusion.lean#L200-L202)
- Source range: L200-L202
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P58` — Newton's First Law as Limit --- V.P22

## Immediate Comment / Docstring

```lean
/-- [V.P58] Conservation laws from sector symmetries: Noether's
    theorem in classical mechanics is a readout of τ-sector symmetries.

    Each conservation law corresponds to a sector automorphism:
    - Energy ↔ base circle τ¹ translation invariance
    - Momentum ↔ D-sector spatial homogeneity
    - Angular momentum ↔ D-sector isotropy -/
```

## Source Excerpt

```lean
theorem conservation_from_sectors :
    [ConservationLaw.Energy, ConservationLaw.Momentum,
     ConservationLaw.AngularMomentum].length = 3 := by native_decide
```
