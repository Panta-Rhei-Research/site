---
{
  "projection_kind": "taulib_declaration",
  "title": "ultra_dist_eq_diverge",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-germs/ultra-dist-eq-diverge/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.OmegaGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaGerms::ultra_dist_eq_diverge",
  "declaration_slug": "ultra-dist-eq-diverge",
  "kind": "theorem",
  "name": "ultra_dist_eq_diverge",
  "module_name": "TauLib.BookI.Polarity.OmegaGerms",
  "module_url": "/verify/taulib/docs/book-i-polarity-omega-germs/",
  "source_line_start": 339,
  "source_line_end": 342,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L339-L342",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L339-L342",
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

- Module: [TauLib.BookI.Polarity.OmegaGerms](/verify/taulib/docs/book-i-polarity-omega-germs/)
- Source path: [`TauLib/BookI/Polarity/OmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L339-L342)
- Source range: L339-L342
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Ultrametric distance on same-depth tails reduces to diverge_go. -/
```

## Source Excerpt

```lean
private theorem ultra_dist_eq_diverge (t1 t2 : OmegaTail) (d : TauIdx)
    (h1 : t1.depth = d) (h2 : t2.depth = d) :
    ultra_dist t1 t2 = diverge_go t1.components t2.components d 0 d := by
  simp only [ultra_dist, divergence_depth, h1, h2, Nat.min_self]
```
