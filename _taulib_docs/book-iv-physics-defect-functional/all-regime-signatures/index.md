---
{
  "projection_kind": "taulib_declaration",
  "title": "all_regime_signatures",
  "permalink": "/verify/taulib/docs/book-iv-physics-defect-functional/all-regime-signatures/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.DefectFunctional`.",
  "declaration_id": "TauLib.BookIV.Physics.DefectFunctional::all_regime_signatures",
  "declaration_slug": "all-regime-signatures",
  "kind": "def",
  "name": "all_regime_signatures",
  "module_name": "TauLib.BookIV.Physics.DefectFunctional",
  "module_url": "/verify/taulib/docs/book-iv-physics-defect-functional/",
  "source_line_start": 241,
  "source_line_end": 243,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L241-L243",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.DefectFunctional",
        "url": "/verify/taulib/docs/book-iv-physics-defect-functional/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L241-L243",
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

- Module: [TauLib.BookIV.Physics.DefectFunctional](/verify/taulib/docs/book-iv-physics-defect-functional/)
- Source path: [`TauLib/BookIV/Physics/DefectFunctional.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L241-L243)
- Source range: L241-L243
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- All 8 canonical regime signatures. -/
```

## Source Excerpt

```lean
def all_regime_signatures : List RegimeSignature :=
  [crystal_signature, glass_signature, euler_signature, ns_signature,
   mhd_signature, plasma_signature, superfluid_signature, superconductor_signature]
```
