---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_artifacts",
  "permalink": "/verify/taulib/docs/book-v-orthodox-correspondence-map/canonical-artifacts/",
  "summary_short": "`def` declaration in `TauLib.BookV.Orthodox.CorrespondenceMap`.",
  "declaration_id": "TauLib.BookV.Orthodox.CorrespondenceMap::canonical_artifacts",
  "declaration_slug": "canonical-artifacts",
  "kind": "def",
  "name": "canonical_artifacts",
  "module_name": "TauLib.BookV.Orthodox.CorrespondenceMap",
  "module_url": "/verify/taulib/docs/book-v-orthodox-correspondence-map/",
  "source_line_start": 103,
  "source_line_end": 128,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L103-L128",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L103-L128",
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

- Module: [TauLib.BookV.Orthodox.CorrespondenceMap](/verify/taulib/docs/book-v-orthodox-correspondence-map/)
- Source path: [`TauLib/BookV/Orthodox/CorrespondenceMap.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/CorrespondenceMap.lean#L103-L128)
- Source range: L103-L128
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The five canonical structural artifacts. -/
```

## Source Excerpt

```lean
def canonical_artifacts : List StructuralArtifact :=
  [ { name := "UV divergences"
      framework := "QFT"
      status := .Artifact
      is_artifact := rfl
      reason := "profinite tower is finite at every depth" }
  , { name := "Cosmological constant problem"
      framework := "GR + QFT"
      status := .Artifact
      is_artifact := rfl
      reason := "Lambda = 0 in tau-Einstein; rho_vac = 0" }
  , { name := "Measurement problem"
      framework := "QM"
      status := .Artifact
      is_artifact := rfl
      reason := "address resolution, not wavefunction collapse" }
  , { name := "Dark matter"
      framework := "Lambda-CDM"
      status := .Artifact
      is_artifact := rfl
      reason := "5 sectors exhaust generator budget" }
  , { name := "Dark energy"
      framework := "Lambda-CDM"
      status := .Artifact
      is_artifact := rfl
      reason := "S_def -> S_ref transition artifact" } ]
```
