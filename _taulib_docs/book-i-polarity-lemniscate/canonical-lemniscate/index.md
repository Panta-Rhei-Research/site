---
{
  "projection_kind": "taulib_declaration",
  "title": "canonical_lemniscate",
  "permalink": "/verify/taulib/docs/book-i-polarity-lemniscate/canonical-lemniscate/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.Lemniscate`.",
  "declaration_id": "TauLib.BookI.Polarity.Lemniscate::canonical_lemniscate",
  "declaration_slug": "canonical-lemniscate",
  "kind": "def",
  "name": "canonical_lemniscate",
  "module_name": "TauLib.BookI.Polarity.Lemniscate",
  "module_url": "/verify/taulib/docs/book-i-polarity-lemniscate/",
  "source_line_start": 65,
  "source_line_end": 72,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L65-L72",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L65-L72",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
- Source path: [`TauLib/BookI/Polarity/Lemniscate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Lemniscate.lean#L65-L72)
- Source range: L65-L72
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical algebraic lemniscate constructed from the split-complex algebra. -/
```

## Source Excerpt

```lean
def canonical_lemniscate : AlgebraicLemniscate :=
  { j_unit := SplitComplex.j
    j_sq := j_squared
    crossing_point := ⟨0, 0⟩
    crossing_balanced := rfl
    involution := polarity_inv
    involution_sq := polarity_inv_squared
    involution_j := polarity_inv_j }
```
