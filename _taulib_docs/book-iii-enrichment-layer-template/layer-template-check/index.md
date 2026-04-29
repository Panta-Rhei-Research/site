---
{
  "projection_kind": "taulib_declaration",
  "title": "layer_template_check",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-layer-template/layer-template-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.LayerTemplate`.",
  "declaration_id": "TauLib.BookIII.Enrichment.LayerTemplate::layer_template_check",
  "declaration_slug": "layer-template-check",
  "kind": "def",
  "name": "layer_template_check",
  "module_name": "TauLib.BookIII.Enrichment.LayerTemplate",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-layer-template/",
  "source_line_start": 110,
  "source_line_end": 130,
  "registry_ids": [
    "III.D05"
  ],
  "related_registry_items": [
    {
      "id": "III.D05",
      "title": "Layer Template",
      "url": "/registry/object/III.D05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L110-L130",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Enrichment.LayerTemplate",
        "url": "/verify/taulib/docs/book-iii-enrichment-layer-template/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L110-L130",
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

- Module: [TauLib.BookIII.Enrichment.LayerTemplate](/verify/taulib/docs/book-iii-enrichment-layer-template/)
- Source path: [`TauLib/BookIII/Enrichment/LayerTemplate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L110-L130)
- Source range: L110-L130
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D05` — Layer Template

## Immediate Comment / Docstring

```lean
/-- [III.D05] Layer template completeness: all four components present
    and consistent at given parameters. -/
```

## Source Excerpt

```lean
def layer_template_check (lt : LayerTemplate) (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let c := lt.carrier_check x k
      let p := lt.predicate_check x k
      -- If x is in the carrier, the predicate and invariant should be checkable
      let ok := if c then
        let d := lt.decoder x k
        let inv := lt.invariant_check x k
        -- Decoder output stays within carrier (endomorphism)
        let d_valid := lt.carrier_check d k
        -- Carrier elements should have valid predicate, invariant, and decoder
        p && inv && d_valid
      else true
      ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
