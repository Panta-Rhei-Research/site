---
{
  "projection_kind": "taulib_declaration",
  "title": "GaussianElliptic.i_squared",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/i-squared/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.H4UniquenessElliptic`.",
  "declaration_id": "TauLib.BookI.Polarity.H4UniquenessElliptic::GaussianElliptic.i_squared",
  "declaration_slug": "i-squared",
  "kind": "theorem",
  "name": "GaussianElliptic.i_squared",
  "module_name": "TauLib.BookI.Polarity.H4UniquenessElliptic",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/",
  "source_line_start": 228,
  "source_line_end": 231,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L228-L231",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.H4UniquenessElliptic",
        "url": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L228-L231",
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

- Module: [TauLib.BookI.Polarity.H4UniquenessElliptic](/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/)
- Source path: [`TauLib/BookI/Polarity/H4UniquenessElliptic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L228-L231)
- Source range: L228-L231
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **i² = -1** (the elliptic relation). -/
```

## Source Excerpt

```lean
theorem GaussianElliptic.i_squared :
    GaussianElliptic.mul GaussianElliptic.i GaussianElliptic.i = ⟨-1, 0⟩ := by
  unfold GaussianElliptic.mul GaussianElliptic.i
  simp
```
