---
{
  "projection_kind": "taulib_declaration",
  "title": "para_complex_structure",
  "permalink": "/corpus/taulib/docs/book-ii-interior-abcdrigidity/para-complex-structure/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Interior.ABCDRigidity`.",
  "declaration_id": "TauLib.BookII.Interior.ABCDRigidity::para_complex_structure",
  "declaration_slug": "para-complex-structure",
  "kind": "theorem",
  "name": "para_complex_structure",
  "module_name": "TauLib.BookII.Interior.ABCDRigidity",
  "module_url": "/corpus/taulib/docs/book-ii-interior-abcdrigidity/",
  "source_line_start": 127,
  "source_line_end": 129,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L127-L129",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.ABCDRigidity",
        "url": "/corpus/taulib/docs/book-ii-interior-abcdrigidity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L127-L129",
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

- Module: [TauLib.BookII.Interior.ABCDRigidity](/corpus/taulib/docs/book-ii-interior-abcdrigidity/)
- Source path: [`TauLib/BookII/Interior/ABCDRigidity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L127-L129)
- Source range: L127-L129
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The ABCD chart induces a para-complex structure (j² = +id),
    not a complex structure (J² = -id).

    Para-complex: decomposes into two REAL eigenspaces (e₊ ⊕ e₋).
    Complex: rotates between two components (no real eigenspaces).

    Verification: j² = +1 in split-complex arithmetic. -/
```

## Source Excerpt

```lean
theorem para_complex_structure :
    SplitComplex.mul ⟨0, 1⟩ ⟨0, 1⟩ = ⟨1, 0⟩ := by
  unfold SplitComplex.mul; ext <;> simp
```
