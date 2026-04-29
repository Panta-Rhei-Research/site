---
{
  "projection_kind": "taulib_declaration",
  "title": "TorusIdentity.universal_fixed_scalar_unconditional",
  "permalink": "/verify/taulib/docs/book-i-boundary-torus-defect-system/universal-fixed-scalar-unconditional/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TorusDefectSystem`.",
  "declaration_id": "TauLib.BookI.Boundary.TorusDefectSystem::TorusIdentity.universal_fixed_scalar_unconditional",
  "declaration_slug": "universal-fixed-scalar-unconditional",
  "kind": "theorem",
  "name": "TorusIdentity.universal_fixed_scalar_unconditional",
  "module_name": "TauLib.BookI.Boundary.TorusDefectSystem",
  "module_url": "/verify/taulib/docs/book-i-boundary-torus-defect-system/",
  "source_line_start": 353,
  "source_line_end": 361,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L353-L361",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L353-L361",
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
- Source path: [`TauLib/BookI/Boundary/TorusDefectSystem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TorusDefectSystem.lean#L353-L361)
- Source range: L353-L361
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 13 universal_fixed_scalar applied unconditionally** on
    `TorusDefectSystem`.  The scalar-readout form of the
    universal-fixed theorem, with singleton_uniqueness discharged. -/
```

## Source Excerpt

```lean
theorem TorusIdentity.universal_fixed_scalar_unconditional
    (g : DefectInverseSystem.SigmaFixedThread TorusDefectSystem)
    (h_g : DefectInverseSystem.IsCrossingPoint torusAnchor torusMwd g)
    (readout_level : ∀ n, TorusDefectSystem.defect_level n → TauRat) :
    TorusDefectSystem.threadReadoutTauReal readout_level
      (TorusIdentityFull.toHolEndMorphism.actSigmaFixed g).toThread =
    TorusDefectSystem.threadReadoutTauReal readout_level g.toThread :=
  TorusIdentityFull.universal_fixed_scalar g h_g torusSingletonUniqueness
    readout_level
```
