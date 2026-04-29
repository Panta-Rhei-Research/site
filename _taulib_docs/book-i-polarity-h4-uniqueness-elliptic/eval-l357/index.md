---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L357",
  "permalink": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/eval-l357/",
  "summary_short": "`eval` declaration in `TauLib.BookI.Polarity.H4UniquenessElliptic`.",
  "declaration_id": "TauLib.BookI.Polarity.H4UniquenessElliptic::#eval:357",
  "declaration_slug": "eval-l357",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookI.Polarity.H4UniquenessElliptic",
  "module_url": "/verify/taulib/docs/book-i-polarity-h4-uniqueness-elliptic/",
  "source_line_start": 357,
  "source_line_end": 362,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L357-L362",
  "formal_status": "computed",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L357-L362",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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
- Source path: [`TauLib/BookI/Polarity/H4UniquenessElliptic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/H4UniquenessElliptic.lean#L357-L362)
- Source range: L357-L362
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Split-complex contrast: (1+j)(1-j) = 0 in SplitComplex
```

## Source Excerpt

```lean
#eval SplitComplex.mul ⟨1, 1⟩ ⟨1, -1⟩                          -- ⟨0, 0⟩ — zero!

-- The structural difference visible at one #eval line:
-- Gaussian gives 2; split-complex gives 0.

end Tau.Polarity
```
