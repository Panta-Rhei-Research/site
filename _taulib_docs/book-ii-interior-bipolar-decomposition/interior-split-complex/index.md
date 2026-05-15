---
{
  "projection_kind": "taulib_declaration",
  "title": "interior_split_complex",
  "permalink": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/interior-split-complex/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.BipolarDecomposition`.",
  "declaration_id": "TauLib.BookII.Interior.BipolarDecomposition::interior_split_complex",
  "declaration_slug": "interior-split-complex",
  "kind": "def",
  "name": "interior_split_complex",
  "module_name": "TauLib.BookII.Interior.BipolarDecomposition",
  "module_url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/",
  "source_line_start": 58,
  "source_line_end": 59,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/BipolarDecomposition.lean#L58-L59",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.BipolarDecomposition",
        "url": "/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/BipolarDecomposition.lean#L58-L59",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookII.Interior.BipolarDecomposition](/corpus/taulib/docs/book-ii-interior-bipolar-decomposition/)
- Source path: [`TauLib/BookII/Interior/BipolarDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/BipolarDecomposition.lean#L58-L59)
- Source range: L58-L59
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Full split-complex interior image via sector → split-complex conversion. -/
```

## Source Excerpt

```lean
def interior_split_complex (p : TauAdmissiblePoint) : SplitComplex :=
  from_sectors (interior_bipolar p)
```
