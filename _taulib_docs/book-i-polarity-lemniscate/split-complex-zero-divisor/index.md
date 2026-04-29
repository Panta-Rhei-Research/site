---
{
  "projection_kind": "taulib_declaration",
  "title": "split_complex_zero_divisor",
  "permalink": "/verify/taulib/docs/book-i-polarity-lemniscate/split-complex-zero-divisor/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.Lemniscate`.",
  "declaration_id": "TauLib.BookI.Polarity.Lemniscate::split_complex_zero_divisor",
  "declaration_slug": "split-complex-zero-divisor",
  "kind": "theorem",
  "name": "split_complex_zero_divisor",
  "module_name": "TauLib.BookI.Polarity.Lemniscate",
  "module_url": "/verify/taulib/docs/book-i-polarity-lemniscate/",
  "source_line_start": 120,
  "source_line_end": 122,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L120-L122",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.Lemniscate",
        "url": "/verify/taulib/docs/book-i-polarity-lemniscate/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L120-L122",
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

- Module: [TauLib.BookI.Polarity.Lemniscate](/verify/taulib/docs/book-i-polarity-lemniscate/)
- Source path: [`TauLib/BookI/Polarity/Lemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L120-L122)
- Source range: L120-L122
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The split-complex algebra has zero divisors: (1+j)(1-j) = 0. -/
```

## Source Excerpt

```lean
theorem split_complex_zero_divisor :
    SplitComplex.mul ⟨1, 1⟩ ⟨1, -1⟩ = SplitComplex.zero := by
  simp [SplitComplex.mul, SplitComplex.zero]
```
