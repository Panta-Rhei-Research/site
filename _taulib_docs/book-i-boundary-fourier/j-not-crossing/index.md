---
{
  "projection_kind": "taulib_declaration",
  "title": "j_not_crossing",
  "permalink": "/corpus/taulib/docs/book-i-boundary-fourier/j-not-crossing/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Fourier`.",
  "declaration_id": "TauLib.BookI.Boundary.Fourier::j_not_crossing",
  "declaration_slug": "j-not-crossing",
  "kind": "theorem",
  "name": "j_not_crossing",
  "module_name": "TauLib.BookI.Boundary.Fourier",
  "module_url": "/corpus/taulib/docs/book-i-boundary-fourier/",
  "source_line_start": 70,
  "source_line_end": 71,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L70-L71",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Fourier",
        "url": "/corpus/taulib/docs/book-i-boundary-fourier/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L70-L71",
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

- Module: [TauLib.BookI.Boundary.Fourier](/corpus/taulib/docs/book-i-boundary-fourier/)
- Source path: [`TauLib/BookI/Boundary/Fourier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L70-L71)
- Source range: L70-L71
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The split-complex unit j is NOT at the crossing (sectors differ). -/
```

## Source Excerpt

```lean
theorem j_not_crossing : ¬is_crossing (spectral SplitComplex.j) := by
  simp [spectral, to_sectors, SplitComplex.j, is_crossing]
```
