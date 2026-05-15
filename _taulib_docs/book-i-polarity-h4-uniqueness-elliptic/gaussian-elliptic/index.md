---
{
  "projection_kind": "taulib_declaration",
  "title": "GaussianElliptic",
  "permalink": "/corpus/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/gaussian-elliptic/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Polarity.H4UniquenessElliptic`.",
  "declaration_id": "TauLib.BookI.Polarity.H4UniquenessElliptic::GaussianElliptic",
  "declaration_slug": "gaussian-elliptic",
  "kind": "structure",
  "name": "GaussianElliptic",
  "module_name": "TauLib.BookI.Polarity.H4UniquenessElliptic",
  "module_url": "/corpus/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/",
  "source_line_start": 200,
  "source_line_end": 203,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L200-L203",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.H4UniquenessElliptic",
        "url": "/corpus/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L200-L203",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookI.Polarity.H4UniquenessElliptic](/corpus/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/)
- Source path: [`TauLib/BookI/Polarity/H4UniquenessElliptic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L200-L203)
- Source range: L200-L203
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The Gaussian / elliptic candidate algebra** `A = R[i]/(i² + 1)`,
    rendered abstractly as a struct with re/im components and an
    elliptic multiplication rule.

    Distinct from `SplitComplex` (which has `j² = +1`); here `i² = -1`
    is the elliptic relation. -/
```

## Source Excerpt

```lean
structure GaussianElliptic where
  re : Int
  im : Int
  deriving DecidableEq, Repr
```
