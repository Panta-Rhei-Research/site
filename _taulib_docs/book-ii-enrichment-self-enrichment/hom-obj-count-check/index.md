---
{
  "projection_kind": "taulib_declaration",
  "title": "hom_obj_count_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/hom-obj-count-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.SelfEnrichment`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfEnrichment::hom_obj_count_check",
  "declaration_slug": "hom-obj-count-check",
  "kind": "def",
  "name": "hom_obj_count_check",
  "module_name": "TauLib.BookII.Enrichment.SelfEnrichment",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/",
  "source_line_start": 175,
  "source_line_end": 184,
  "registry_ids": [
    "II.D54"
  ],
  "related_registry_items": [
    {
      "id": "II.D54",
      "title": "Hom Object",
      "url": "/registry/object/II.D54/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L175-L184",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L175-L184",
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
- Source path: [`TauLib/BookII/Enrichment/SelfEnrichment.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L175-L184)
- Source range: L175-L184
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D54` — Hom Object

## Immediate Comment / Docstring

```lean
/-- [II.D54] Hom object count check: at each stage k >= 1, the number of
    affine reduce-compatible endomorphisms is at least 2 (identity and constant).
    For k=1 (P_1=2): identity x↦x, constant x↦0 are both reduce-compatible. -/
```

## Source Excerpt

```lean
def hom_obj_count_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let c := hom_obj_count_affine k
      (c >= 2) && go (k + 1) (fuel - 1)
  termination_by fuel
```
