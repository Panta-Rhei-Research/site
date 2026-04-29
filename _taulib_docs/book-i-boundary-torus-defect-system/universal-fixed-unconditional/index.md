---
{
  "projection_kind": "taulib_declaration",
  "title": "TorusIdentity.universal_fixed_unconditional",
  "permalink": "/verify/taulib/docs/book-i-boundary-torus-defect-system/universal-fixed-unconditional/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TorusDefectSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.TorusDefectSystem::TorusIdentity.universal_fixed_unconditional",
  "declaration_slug": "universal-fixed-unconditional",
  "kind": "theorem",
  "name": "TorusIdentity.universal_fixed_unconditional",
  "module_name": "TauLib.BookI.Boundary.TorusDefectSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-torus-defect-system/",
  "source_line_start": 344,
  "source_line_end": 348,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L344-L348",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TorusDefectSystem",
        "url": "/verify/taulib/docs/book-i-boundary-torus-defect-system/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L344-L348",
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

- Module: [TauLib.BookI.Boundary.TorusDefectSystem](/verify/taulib/docs/book-i-boundary-torus-defect-system/)
- Source path: [`TauLib/BookI/Boundary/TorusDefectSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L344-L348)
- Source range: L344-L348
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 13 universal_fixed_theorem applied unconditionally** on
    `TorusDefectSystem`.

    The conditional Wave 13 theorem required the
    `singleton_uniqueness` hypothesis; on this concrete instance we
    discharged that hypothesis via `torusSingletonUniqueness`
    (which exploits the concrete fact that `TorusDefect`'s σ-fixed
    points are exactly `{none}`).

    Plugging in, the Wave 13 theorem becomes an **unconditional
    structural result** on this instance: the identity HolEnd
    morphism fixes the (unique) crossing-point thread. -/
```

## Source Excerpt

```lean
theorem TorusIdentity.universal_fixed_unconditional
    (g : DefectInverseSystem.SigmaFixedThread TorusDefectSystem)
    (h_g : DefectInverseSystem.IsCrossingPoint torusAnchor torusMwd g) :
    TorusIdentityFull.toHolEndMorphism.actSigmaFixed g = g :=
  TorusIdentityFull.universal_fixed_theorem g h_g torusSingletonUniqueness
```
