---
{
  "projection_kind": "taulib_declaration",
  "title": "hom_channel_independence_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/hom-channel-independence-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.SelfEnrichment`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfEnrichment::hom_channel_independence_check",
  "declaration_slug": "hom-channel-independence-check",
  "kind": "def",
  "name": "hom_channel_independence_check",
  "module_name": "TauLib.BookII.Enrichment.SelfEnrichment",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/",
  "source_line_start": 225,
  "source_line_end": 246,
  "registry_ids": [
    "II.P12"
  ],
  "related_registry_items": [
    {
      "id": "II.P12",
      "title": "Enrichment Iteration",
      "url": "/registry/object/II.P12/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L225-L246",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L225-L246",
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
- Source path: [`TauLib/BookII/Enrichment/SelfEnrichment.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L225-L246)
- Source range: L225-L246
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P12` — Enrichment Iteration

## Immediate Comment / Docstring

```lean
/-- [II.P12] Bipolar channel independence check.
    The B-channel of the hom-element depends only on the B-data of the inputs,
    and similarly for the C-channel. Verified by checking that the sector
    projections are consistent with the input structure. -/
```

## Source Excerpt

```lean
def hom_channel_independence_check (bound db : TauIdx) : Bool :=
  go 2 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (a b k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a > bound then true
    else if b > bound then go (a + 1) 0 1 (fuel - 1)
    else if k > db then go a (b + 1) 1 (fuel - 1)
    else
      -- The hom-stage value's bipolar decomposition
      let val := hom_stage a b k
      let sp := interior_bipolar (from_tau_idx val)
      -- B-channel projection is idempotent: proj_B(proj_B(sp)) = proj_B(sp)
      let pb := SectorPair.mul e_plus_sector sp
      let pb2 := SectorPair.mul e_plus_sector pb
      let idem_b := pb2 == pb
      -- C-channel projection is idempotent: proj_C(proj_C(sp)) = proj_C(sp)
      let pc := SectorPair.mul e_minus_sector sp
      let pc2 := SectorPair.mul e_minus_sector pc
      let idem_c := pc2 == pc
      idem_b && idem_c && go a b (k + 1) (fuel - 1)
  termination_by fuel
```
