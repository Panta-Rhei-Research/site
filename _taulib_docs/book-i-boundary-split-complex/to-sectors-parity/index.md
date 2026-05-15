---
{
  "projection_kind": "taulib_declaration",
  "title": "to_sectors_parity",
  "permalink": "/corpus/taulib/docs/book-i-boundary-split-complex/to-sectors-parity/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.SplitComplex`.",
  "declaration_id": "TauLib.BookI.Boundary.SplitComplex::to_sectors_parity",
  "declaration_slug": "to-sectors-parity",
  "kind": "theorem",
  "name": "to_sectors_parity",
  "module_name": "TauLib.BookI.Boundary.SplitComplex",
  "module_url": "/corpus/taulib/docs/book-i-boundary-split-complex/",
  "source_line_start": 227,
  "source_line_end": 233,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L227-L233",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.SplitComplex",
        "url": "/corpus/taulib/docs/book-i-boundary-split-complex/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L227-L233",
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

- Module: [TauLib.BookI.Boundary.SplitComplex](/corpus/taulib/docs/book-i-boundary-split-complex/)
- Source path: [`TauLib/BookI/Boundary/SplitComplex.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/SplitComplex.lean#L227-L233)
- Source range: L227-L233
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The image of to_sectors consists of pairs with equal parity. -/
```

## Source Excerpt

```lean
theorem to_sectors_parity (z : SplitComplex) :
    ((to_sectors z).b_sector + (to_sectors z).c_sector) % 2 = 0 := by
  simp only [to_sectors]
  -- b_sector + c_sector = (re + im) + (re - im) = 2 * re
  have : z.re + z.im + (z.re - z.im) = 2 * z.re := by ring
  rw [this]
  exact Int.mul_emod_right 2 z.re
```
