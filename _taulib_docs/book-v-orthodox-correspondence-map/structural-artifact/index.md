---
{
  "projection_kind": "taulib_declaration",
  "title": "StructuralArtifact",
  "permalink": "/verify/taulib/docs/book-v-orthodox-correspondence-map/structural-artifact/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Orthodox.CorrespondenceMap`.",
  "declaration_id": "TauLib.BookV.Orthodox.CorrespondenceMap::StructuralArtifact",
  "declaration_slug": "structural-artifact",
  "kind": "structure",
  "name": "StructuralArtifact",
  "module_name": "TauLib.BookV.Orthodox.CorrespondenceMap",
  "module_url": "/verify/taulib/docs/book-v-orthodox-correspondence-map/",
  "source_line_start": 89,
  "source_line_end": 100,
  "registry_ids": [
    "V.D185"
  ],
  "related_registry_items": [
    {
      "id": "V.D185",
      "title": "Structural artifact",
      "url": "/registry/object/V.D185/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L89-L100",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.CorrespondenceMap",
        "url": "/verify/taulib/docs/book-v-orthodox-correspondence-map/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L89-L100",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookV.Orthodox.CorrespondenceMap](/verify/taulib/docs/book-v-orthodox-correspondence-map/)
- Source path: [`TauLib/BookV/Orthodox/CorrespondenceMap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L89-L100)
- Source range: L89-L100
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `V.D185` — Structural artifact

## Immediate Comment / Docstring

```lean
/-- [V.D185] A structural artifact of an orthodox framework F is a
    problem, divergence, or paradox that arises within F but has no
    ontic counterpart in H_partial[omega].

    Five canonical artifacts:
    1. UV divergences (no ontic short-distance singularity)
    2. Cosmological constant (Lambda = 0 in tau-Einstein)
    3. Measurement problem (address resolution, not collapse)
    4. Dark matter (sector exhaustion, no sixth sector)
    5. Dark energy (readout artifact from S_def -> S_ref) -/
```

## Source Excerpt

```lean
structure StructuralArtifact where
  /-- Name of the artifact. -/
  name : String
  /-- The orthodox framework where it arises. -/
  framework : String
  /-- Classification in the tau-framework. -/
  status : ArtifactStatus
  /-- Must be an artifact. -/
  is_artifact : status = .Artifact
  /-- Brief description of why no ontic counterpart exists. -/
  reason : String
  deriving Repr
```
