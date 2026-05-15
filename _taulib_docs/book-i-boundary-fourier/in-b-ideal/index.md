---
{
  "projection_kind": "taulib_declaration",
  "title": "in_b_ideal",
  "permalink": "/corpus/taulib/docs/book-i-boundary-fourier/in-b-ideal/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Fourier`.",
  "declaration_id": "TauLib.BookI.Boundary.Fourier::in_b_ideal",
  "declaration_slug": "in-b-ideal",
  "kind": "def",
  "name": "in_b_ideal",
  "module_name": "TauLib.BookI.Boundary.Fourier",
  "module_url": "/corpus/taulib/docs/book-i-boundary-fourier/",
  "source_line_start": 79,
  "source_line_end": 80,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L79-L80",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L79-L80",
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

- Module: [TauLib.BookI.Boundary.Fourier](/corpus/taulib/docs/book-i-boundary-fourier/)
- Source path: [`TauLib/BookI/Boundary/Fourier.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Fourier.lean#L79-L80)
- Source range: L79-L80
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- An element is in the B-ideal iff its C-sector vanishes.
    The B-ideal = ker(χ₋) = {z : z.re = z.im}. -/
```

## Source Excerpt

```lean
def in_b_ideal (z : SplitComplex) : Prop :=
  (spectral z).c_sector = 0
```
