---
{
  "projection_kind": "taulib_declaration",
  "title": "ultra_triangle_check",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-germs/ultra-triangle-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.OmegaGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaGerms::ultra_triangle_check",
  "declaration_slug": "ultra-triangle-check",
  "kind": "def",
  "name": "ultra_triangle_check",
  "module_name": "TauLib.BookI.Polarity.OmegaGerms",
  "module_url": "/verify/taulib/docs/book-i-polarity-omega-germs/",
  "source_line_start": 260,
  "source_line_end": 263,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L260-L263",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.OmegaGerms",
        "url": "/verify/taulib/docs/book-i-polarity-omega-germs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L260-L263",
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

- Module: [TauLib.BookI.Polarity.OmegaGerms](/verify/taulib/docs/book-i-polarity-omega-germs/)
- Source path: [`TauLib/BookI/Polarity/OmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L260-L263)
- Source range: L260-L263
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Check ultrametric strong triangle inequality (divergence-depth convention).
    In the raw divergence-depth convention (0 = identical, k = first disagreement
    at position k-1), the standard ultrametric triangle d(x,z) ≤ max(d(x,y), d(y,z))
    translates to: the first disagreement of (t1,t3) is at least as deep as
    the minimum of the first disagreements of the other two pairs.
    This holds for all non-identical pairs; when ultra_dist = 0 (identical),
    the pair is transparent (d(t1,t3) = d(t2,t3) when t1 ≡ t2). -/
```

## Source Excerpt

```lean
def ultra_triangle_check (t1 t2 t3 : OmegaTail) : Bool :=
  -- For non-identical t1,t3: first-disagree(t1,t3) ≥ min of other two
  ultra_dist t1 t3 == 0 ||
  ultra_dist t1 t3 >= min (ultra_dist t1 t2) (ultra_dist t2 t3)
```
