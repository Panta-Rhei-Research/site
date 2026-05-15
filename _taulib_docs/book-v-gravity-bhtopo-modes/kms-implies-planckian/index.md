---
{
  "projection_kind": "taulib_declaration",
  "title": "kms_implies_planckian",
  "permalink": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/kms-implies-planckian/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Gravity.BHTopoModes`.",
  "declaration_id": "TauLib.BookV.Gravity.BHTopoModes::kms_implies_planckian",
  "declaration_slug": "kms-implies-planckian",
  "kind": "theorem",
  "name": "kms_implies_planckian",
  "module_name": "TauLib.BookV.Gravity.BHTopoModes",
  "module_url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/",
  "source_line_start": 611,
  "source_line_end": 615,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L611-L615",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.BHTopoModes",
        "url": "/corpus/taulib/docs/book-v-gravity-bhtopo-modes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L611-L615",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookV.Gravity.BHTopoModes](/corpus/taulib/docs/book-v-gravity-bhtopo-modes/)
- Source path: [`TauLib/BookV/Gravity/BHTopoModes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/BHTopoModes.lean#L611-L615)
- Source range: L611-L615
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- KMS implies Planckian: if boundary algebra is bosonic and KMS holds,
    the spectrum is uniquely Planckian. -/
```

## Source Excerpt

```lean
theorem kms_implies_planckian :
    kms_readout.boundary_algebra_bosonic = 1 ∧
    kms_readout.kms_condition_satisfied = 1 →
    kms_readout.is_planckian = 1 := by
  intro _; rfl
```
