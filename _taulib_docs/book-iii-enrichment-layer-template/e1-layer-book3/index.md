---
{
  "projection_kind": "taulib_declaration",
  "title": "e1_layer_book3",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-layer-template/e1-layer-book3/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.LayerTemplate`.",
  "declaration_id": "TauLib.BookIII.Enrichment.LayerTemplate::e1_layer_book3",
  "declaration_slug": "e1-layer-book3",
  "kind": "def",
  "name": "e1_layer_book3",
  "module_name": "TauLib.BookIII.Enrichment.LayerTemplate",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-layer-template/",
  "source_line_start": 164,
  "source_line_end": 188,
  "registry_ids": [
    "III.D07"
  ],
  "related_registry_items": [
    {
      "id": "III.D07",
      "title": "E₁ Layer (Physics)",
      "url": "/registry/object/III.D07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L164-L188",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L164-L188",
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
- Source path: [`TauLib/BookIII/Enrichment/LayerTemplate.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/LayerTemplate.lean#L164-L188)
- Source range: L164-L188
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D07` — E₁ Layer (Physics)

## Immediate Comment / Docstring

```lean
/-- [III.D07] E₁ Layer: the physics layer (Books IV-V).
    - Carrier: H_τ-enriched objects (hom-stage well-defined)
    - Predicate: sector admissibility (bipolar decomposition exists)
    - Decoder: spectral projection (e₊/e₋ decomposition)
    - Invariant: sector coupling canonicality

    This EXTENDS Book II's E1Layer with sector structure. -/
```

## Source Excerpt

```lean
def e1_layer_book3 (bound db : TauIdx) : LayerTemplate :=
  { carrier_check := fun x k =>
      -- H_τ-enriched: hom_stage is well-defined AND reduce-stable
      let hs := hom_stage x 0 k
      (x < primorial k || k == 0) && (reduce hs k == hs)
  , predicate_check := fun x k =>
      -- Sector admissibility: bipolar decomposition exists
      let sp := interior_bipolar (from_tau_idx (reduce x k))
      let proj_b := SectorPair.mul e_plus_sector sp
      let proj_c := SectorPair.mul e_minus_sector sp
      let recombined := SectorPair.add proj_b proj_c
      recombined == sp
  , decoder := fun x k =>
      -- Spectral projection: extract B-channel value
      let sp := interior_bipolar (from_tau_idx (reduce x k))
      let proj_b := SectorPair.mul e_plus_sector sp
      proj_b.b_sector.toNat
  , invariant_check := fun x k =>
      -- Sector coupling: ω-readout is determined by bipolar decomposition
      let val := reduce x k
      let sp := interior_bipolar (from_tau_idx val)
      -- The coupling is canonical: e₊ * e₋ = 0 (orthogonality)
      let cross := SectorPair.mul e_plus_sector (SectorPair.mul e_minus_sector sp)
      cross == ⟨0, 0⟩
  }
```
