---
{
  "projection_kind": "taulib_declaration",
  "title": "embed_int_into_d",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-scalar-bridges/embed-int-into-d/",
  "summary_short": "`def` declaration in `TauLib.BookI.KernelFoundation.ScalarBridges`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.ScalarBridges::embed_int_into_d",
  "declaration_slug": "embed-int-into-d",
  "kind": "def",
  "name": "embed_int_into_d",
  "module_name": "TauLib.BookI.KernelFoundation.ScalarBridges",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-scalar-bridges/",
  "source_line_start": 104,
  "source_line_end": 110,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L104-L110",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L104-L110",
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

- Module: [TauLib.BookI.KernelFoundation.ScalarBridges](/verify/taulib/docs/book-i-kernel-foundation-scalar-bridges/)
- Source path: [`TauLib/BookI/KernelFoundation/ScalarBridges.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/ScalarBridges.lean#L104-L110)
- Source range: L104-L110
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §H4 / Wave 37 canonical embedding ℤ → D**.

    Sends `n : Int` to `⟨n, 0⟩ : SplitComplex` — the canonical
    "real-axis" embedding into the boundary algebra D.

    This is the missing reverse direction of D's character machinery
    (D → ℤ via χ₊, χ₋ existed; ℤ → D was absent until Wave 37). -/
```

## Source Excerpt

```lean
def embed_int_into_d (n : Int) : SplitComplex := ⟨n, 0⟩

@[simp] theorem embed_int_re (n : Int) :
    (embed_int_into_d n).re = n := rfl

@[simp] theorem embed_int_im (n : Int) :
    (embed_int_into_d n).im = 0 := rfl
```
