---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L376",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-germs/example-l376/",
  "summary_short": "`example` declaration in `TauLib.BookI.Polarity.OmegaGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaGerms::#eval:376",
  "declaration_slug": "example-l376",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Polarity.OmegaGerms",
  "module_url": "/verify/taulib/docs/book-i-polarity-omega-germs/",
  "source_line_start": 376,
  "source_line_end": 377,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L376-L377",
  "formal_status": "example",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L376-L377",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "status": "example"
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
- Source path: [`TauLib/BookI/Polarity/OmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L376-L377)
- Source range: L376-L377
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- ULTRAMETRIC TRIANGLE (native_decide verifications, kept as regression tests)
-- ============================================================

-- The divergence-depth convention uses 0 = "identical" and k = "first
-- disagreement at position k-1". The standard ultrametric triangle
-- d(x,z) ≤ max(d(x,y), d(y,z)) uses d = 2^(-first_disagree), where
-- larger first_disagree → smaller d. Translated to our convention:
--
--   For non-identical pairs: ultra_dist(t1,t3) ≥ min(ultra_dist(t1,t2), ultra_dist(t2,t3))
--
-- Verified by native_decide for concrete omega-tails below.
```

## Source Excerpt

```lean
example : ultra_triangle_check (nat_to_tail 7 5) (nat_to_tail 42 5) (nat_to_tail 100 5)
    = true := by native_decide
```
