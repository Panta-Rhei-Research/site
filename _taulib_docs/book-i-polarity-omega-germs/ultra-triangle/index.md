---
{
  "projection_kind": "taulib_declaration",
  "title": "ultra_triangle",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-germs/ultra-triangle/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.OmegaGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaGerms::ultra_triangle",
  "declaration_slug": "ultra-triangle",
  "kind": "theorem",
  "name": "ultra_triangle",
  "module_name": "TauLib.BookI.Polarity.OmegaGerms",
  "module_url": "/verify/taulib/docs/book-i-polarity-omega-germs/",
  "source_line_start": 346,
  "source_line_end": 353,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L346-L353",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L346-L353",
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
- Source path: [`TauLib/BookI/Polarity/OmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L346-L353)
- Source range: L346-L353
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Ultrametric triangle inequality (formal, universal) for equal-depth tails.
    d(t1,t3) = 0 or d(t1,t3) ≥ min(d(t1,t2), d(t2,t3)). -/
```

## Source Excerpt

```lean
theorem ultra_triangle (t1 t2 t3 : OmegaTail)
    (h12 : t1.depth = t2.depth) (h13 : t1.depth = t3.depth) :
    ultra_dist t1 t3 = 0 ∨
    ultra_dist t1 t3 ≥ Nat.min (ultra_dist t1 t2) (ultra_dist t2 t3) := by
  rw [ultra_dist_eq_diverge t1 t3 t1.depth rfl (h13 ▸ rfl),
      ultra_dist_eq_diverge t1 t2 t1.depth rfl (h12 ▸ rfl),
      ultra_dist_eq_diverge t2 t3 t1.depth (h12 ▸ rfl) (h13 ▸ rfl)]
  exact diverge_go_triangle t1.components t2.components t3.components t1.depth 0 t1.depth
```
