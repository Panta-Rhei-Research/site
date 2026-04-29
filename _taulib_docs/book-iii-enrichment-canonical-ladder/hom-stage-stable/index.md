---
{
  "projection_kind": "taulib_declaration",
  "title": "hom_stage_stable",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/hom-stage-stable/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Enrichment.CanonicalLadder`.",
  "declaration_id": "TauLib.BookIII.Enrichment.CanonicalLadder::hom_stage_stable",
  "declaration_slug": "hom-stage-stable",
  "kind": "theorem",
  "name": "hom_stage_stable",
  "module_name": "TauLib.BookIII.Enrichment.CanonicalLadder",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/",
  "source_line_start": 262,
  "source_line_end": 265,
  "registry_ids": [
    "III.T02"
  ],
  "related_registry_items": [
    {
      "id": "III.T02",
      "title": "Strictness Theorem",
      "url": "/registry/object/III.T02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L262-L265",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Enrichment.CanonicalLadder",
        "url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L262-L265",
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

- Module: [TauLib.BookIII.Enrichment.CanonicalLadder](/verify/taulib/docs/book-iii-enrichment-canonical-ladder/)
- Source path: [`TauLib/BookIII/Enrichment/CanonicalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L262-L265)
- Source range: L262-L265
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T02` — Strictness Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T02] Structural strictness at E₀→E₁: the hom_stage value
    is reduce-stable, witnessing genuine E₁ structure. -/
```

## Source Excerpt

```lean
theorem hom_stage_stable (a b k : TauIdx) :
    reduce (hom_stage a b k) k = hom_stage a b k := by
  simp only [hom_stage, reduce]
  exact Nat.mod_mod_of_dvd _ (dvd_refl (primorial k))
```
