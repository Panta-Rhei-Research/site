---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_decomposition",
  "permalink": "/verify/taulib/docs/book-i-boundary-spectral/spectral-decomposition/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Spectral`.",
  "declaration_id": "TauLib.BookI.Boundary.Spectral::spectral_decomposition",
  "declaration_slug": "spectral-decomposition",
  "kind": "theorem",
  "name": "spectral_decomposition",
  "module_name": "TauLib.BookI.Boundary.Spectral",
  "module_url": "/verify/taulib/docs/book-i-boundary-spectral/",
  "source_line_start": 58,
  "source_line_end": 60,
  "registry_ids": [
    "I.T12"
  ],
  "related_registry_items": [
    {
      "id": "I.T12",
      "title": "Spectral Decomposition",
      "url": "/registry/object/I.T12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L58-L60",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Spectral",
        "url": "/verify/taulib/docs/book-i-boundary-spectral/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L58-L60",
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

- Module: [TauLib.BookI.Boundary.Spectral](/verify/taulib/docs/book-i-boundary-spectral/)
- Source path: [`TauLib/BookI/Boundary/Spectral.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Spectral.lean#L58-L60)
- Source range: L58-L60
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T12` — Spectral Decomposition

## Immediate Comment / Docstring

```lean
/-- [I.T12] Spectral decomposition: every element decomposes as the sum of its
    B-sector projection and C-sector projection.
    to_sectors(z) = χ₊(z) + χ₋(z) -/
```

## Source Excerpt

```lean
theorem spectral_decomposition (z : SplitComplex) :
    spectral z = SectorPair.add (chi_plus z) (chi_minus z) := by
  rw [spectral, ← chi_complete z]
```
