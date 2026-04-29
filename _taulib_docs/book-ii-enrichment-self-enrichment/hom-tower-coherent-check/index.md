---
{
  "projection_kind": "taulib_declaration",
  "title": "hom_tower_coherent_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/hom-tower-coherent-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.SelfEnrichment`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfEnrichment::hom_tower_coherent_check",
  "declaration_slug": "hom-tower-coherent-check",
  "kind": "def",
  "name": "hom_tower_coherent_check",
  "module_name": "TauLib.BookII.Enrichment.SelfEnrichment",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/",
  "source_line_start": 58,
  "source_line_end": 71,
  "registry_ids": [
    "II.D53"
  ],
  "related_registry_items": [
    {
      "id": "II.D53",
      "title": "Self-Enrichment Structure",
      "url": "/registry/object/II.D53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L58-L71",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.SelfEnrichment",
        "url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L58-L71",
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

- Module: [TauLib.BookII.Enrichment.SelfEnrichment](/verify/taulib/docs/book-ii-enrichment-self-enrichment/)
- Source path: [`TauLib/BookII/Enrichment/SelfEnrichment.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L58-L71)
- Source range: L58-L71
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D53` — Self-Enrichment Structure

## Immediate Comment / Docstring

```lean
/-- [II.D53] Hom tower coherence check:
    verify that hom_stage at stage k+1 reduces to hom_stage at stage k.
    reduce(hom_stage(a, b, k+1), k) = hom_stage(a, b, k).
    This ensures the hom-spaces form an inverse system. -/
```

## Source Excerpt

```lean
def hom_tower_coherent_check (bound db : TauIdx) : Bool :=
  go 2 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (a b k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a > bound then true
    else if b > bound then go (a + 1) 0 1 (fuel - 1)
    else if k >= db then go a (b + 1) 1 (fuel - 1)
    else
      let val_k1 := hom_stage a b (k + 1)
      let reduced := reduce val_k1 k
      let val_k := hom_stage a b k
      (reduced == val_k) && go a b (k + 1) (fuel - 1)
  termination_by fuel
```
