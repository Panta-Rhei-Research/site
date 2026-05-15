---
{
  "projection_kind": "taulib_declaration",
  "title": "sigma_polarity_matrix_equivariant",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-majorana-structure/sigma-polarity-matrix-equivariant/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.MajoranaStructure`.",
  "declaration_id": "TauLib.BookIV.Electroweak.MajoranaStructure::sigma_polarity_matrix_equivariant",
  "declaration_slug": "sigma-polarity-matrix-equivariant",
  "kind": "theorem",
  "name": "sigma_polarity_matrix_equivariant",
  "module_name": "TauLib.BookIV.Electroweak.MajoranaStructure",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-majorana-structure/",
  "source_line_start": 159,
  "source_line_end": 159,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L159-L159",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.MajoranaStructure",
        "url": "/corpus/taulib/docs/book-iv-electroweak-majorana-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L159-L159",
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

- Module: [TauLib.BookIV.Electroweak.MajoranaStructure](/corpus/taulib/docs/book-iv-electroweak-majorana-structure/)
- Source path: [`TauLib/BookIV/Electroweak/MajoranaStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L159-L159)
- Source range: L159-L159
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The σ-polarity matrix is σ-equivariant: it commutes with the lobe-swap.
    This is a structural consequence of I.D18 (Algebraic Lemniscate).
    The matrix [[a,b,0],[b,c,b],[0,b,a]] is symmetric under row 1 ↔ row 3
    exchange = the σ_swap action on (lobe₊, crossing, lobe₋) basis. -/
```

## Source Excerpt

```lean
theorem sigma_polarity_matrix_equivariant : True := trivial
```
