---
{
  "projection_kind": "taulib_declaration",
  "title": "nno_from_d_witness_minus",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-scalar-bridges/nno-from-d-witness-minus/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.KernelFoundation.ScalarBridges`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.ScalarBridges::nno_from_d_witness_minus",
  "declaration_slug": "nno-from-d-witness-minus",
  "kind": "theorem",
  "name": "nno_from_d_witness_minus",
  "module_name": "TauLib.BookI.KernelFoundation.ScalarBridges",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-scalar-bridges/",
  "source_line_start": 157,
  "source_line_end": 161,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L157-L161",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.ScalarBridges",
        "url": "/verify/taulib/docs/book-i-kernel-foundation-scalar-bridges/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L157-L161",
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

- Module: [TauLib.BookI.KernelFoundation.ScalarBridges](/verify/taulib/docs/book-i-kernel-foundation-scalar-bridges/)
- Source path: [`TauLib/BookI/KernelFoundation/ScalarBridges.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L157-L161)
- Source range: L157-L161
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Companion: χ₋ ∘ embed_nat = id (Nat-level)**. -/
```

## Source Excerpt

```lean
theorem nno_from_d_witness_minus (n : Nat) :
    chi_minus_val (embed_nat_into_d n) = (n : Int) := by
  unfold embed_nat_into_d
  rw [chi_minus_embed_int]
  rfl
```
