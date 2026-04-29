---
{
  "projection_kind": "taulib_declaration",
  "title": "inference_from_kernel",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/inference-from-kernel/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::inference_from_kernel",
  "declaration_slug": "inference-from-kernel",
  "kind": "theorem",
  "name": "inference_from_kernel",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 712,
  "source_line_end": 715,
  "registry_ids": [
    "VII.T26"
  ],
  "related_registry_items": [
    {
      "id": "VII.T26",
      "title": "Inference from Kernel Structure",
      "url": "/registry/object/VII.T26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L712-L715",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L712-L715",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L712-L715)
- Source range: L712-L715
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T26` — Inference from Kernel Structure

## Immediate Comment / Docstring

```lean
/-- [VII.T26] Inference from Kernel Structure (ch41). Inductive
    inference is a structural feature of the kernel: continuation
    operators (analytic continuation) provide the bridge from
    local evidence to global prediction. Not Humean custom but
    structural necessity. -/
```

## Source Excerpt

```lean
theorem inference_from_kernel :
    internal_randomness.deterministic_kernel = true ∧
    boolean_micro.decidable = true :=
  ⟨rfl, rfl⟩
```
