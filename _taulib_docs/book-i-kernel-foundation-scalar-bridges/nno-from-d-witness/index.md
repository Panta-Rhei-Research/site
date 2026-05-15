---
{
  "projection_kind": "taulib_declaration",
  "title": "nno_from_d_witness",
  "permalink": "/corpus/taulib/docs/book-i-kernel-foundation-scalar-bridges/nno-from-d-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.KernelFoundation.ScalarBridges`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.ScalarBridges::nno_from_d_witness",
  "declaration_slug": "nno-from-d-witness",
  "kind": "theorem",
  "name": "nno_from_d_witness",
  "module_name": "TauLib.BookI.KernelFoundation.ScalarBridges",
  "module_url": "/corpus/taulib/docs/book-i-kernel-foundation-scalar-bridges/",
  "source_line_start": 150,
  "source_line_end": 154,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L150-L154",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.ScalarBridges",
        "url": "/corpus/taulib/docs/book-i-kernel-foundation-scalar-bridges/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L150-L154",
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

- Module: [TauLib.BookI.KernelFoundation.ScalarBridges](/corpus/taulib/docs/book-i-kernel-foundation-scalar-bridges/)
- Source path: [`TauLib/BookI/KernelFoundation/ScalarBridges.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L150-L154)
- Source range: L150-L154
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **NNO-style witness via embed_nat (KEYSTONE)**: the natural-number
    embedding into D round-trips through χ₊ to the original Nat.

    This is the bidirectional ℕ ↔ D bridge that the discovery review
    identified as the missing piece. -/
```

## Source Excerpt

```lean
theorem nno_from_d_witness (n : Nat) :
    chi_plus_val (embed_nat_into_d n) = (n : Int) := by
  unfold embed_nat_into_d
  rw [chi_plus_embed_int]
  rfl
```
