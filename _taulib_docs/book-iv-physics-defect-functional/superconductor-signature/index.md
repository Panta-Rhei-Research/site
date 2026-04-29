---
{
  "projection_kind": "taulib_declaration",
  "title": "superconductor_signature",
  "permalink": "/verify/taulib/docs/book-iv-physics-defect-functional/superconductor-signature/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Physics.DefectFunctional`.",
  "declaration_id": "TauLib.BookIV.Physics.DefectFunctional::superconductor_signature",
  "declaration_slug": "superconductor-signature",
  "kind": "def",
  "name": "superconductor_signature",
  "module_name": "TauLib.BookIV.Physics.DefectFunctional",
  "module_url": "/verify/taulib/docs/book-iv-physics-defect-functional/",
  "source_line_start": 231,
  "source_line_end": 238,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L231-L238",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L231-L238",
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
- Source path: [`TauLib/BookIV/Physics/DefectFunctional.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/DefectFunctional.lean#L231-L238)
- Source range: L231-L238
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Superconductor regime: EM-superfluid, quantized flux. -/
```

## Source Excerpt

```lean
def superconductor_signature : RegimeSignature where
  regime := .Superconductor
  mobility_bound := none
  kelvin_invariant := true
  dissipation := false                -- zero resistance
  em_coupled := true                  -- EM sector (Meissner effect)
  quantized_circulation := true       -- quantized flux tubes
  incompressible := true
```
