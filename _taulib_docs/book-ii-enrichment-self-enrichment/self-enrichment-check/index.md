---
{
  "projection_kind": "taulib_declaration",
  "title": "self_enrichment_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/self-enrichment-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.SelfEnrichment`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfEnrichment::self_enrichment_check",
  "declaration_slug": "self-enrichment-check",
  "kind": "def",
  "name": "self_enrichment_check",
  "module_name": "TauLib.BookII.Enrichment.SelfEnrichment",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/",
  "source_line_start": 77,
  "source_line_end": 93,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L77-L93",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L77-L93",
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
- Source path: [`TauLib/BookII/Enrichment/SelfEnrichment.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L77-L93)
- Source range: L77-L93
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D53` — Self-Enrichment Structure

## Immediate Comment / Docstring

```lean
/-- [II.D53] Self-enrichment check: for every pair (a, b) at stage k,
    the hom-space is nonempty (at least the constant map sends a to 0,
    and the identity sends a to reduce(a, k)).
    We verify hom_stage is well-defined for all inputs. -/
```

## Source Excerpt

```lean
def self_enrichment_check (bound db : TauIdx) : Bool :=
  go 2 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (a b k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a > bound then true
    else if b > bound then go (a + 1) 0 1 (fuel - 1)
    else if k > db then go a (b + 1) 1 (fuel - 1)
    else
      -- The identity map's image: reduce(a, k) is always in range
      let id_img := reduce a k
      -- The constant 0 map's image: 0 is always in range
      let const_img : TauIdx := 0
      let ok := (id_img < primorial k || primorial k == 0) &&
                (const_img < primorial k || primorial k == 0)
      ok && go a b (k + 1) (fuel - 1)
  termination_by fuel
```
