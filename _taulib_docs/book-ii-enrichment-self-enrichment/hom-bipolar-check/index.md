---
{
  "projection_kind": "taulib_declaration",
  "title": "hom_bipolar_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/hom-bipolar-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.SelfEnrichment`.",
  "declaration_id": "TauLib.BookII.Enrichment.SelfEnrichment::hom_bipolar_check",
  "declaration_slug": "hom-bipolar-check",
  "kind": "def",
  "name": "hom_bipolar_check",
  "module_name": "TauLib.BookII.Enrichment.SelfEnrichment",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-self-enrichment/",
  "source_line_start": 198,
  "source_line_end": 219,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L198-L219",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L198-L219",
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
- Source path: [`TauLib/BookII/Enrichment/SelfEnrichment.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/SelfEnrichment.lean#L198-L219)
- Source range: L198-L219
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P12` — Enrichment Iteration

## Immediate Comment / Docstring

```lean
/-- [II.P12] Hom bipolar decomposition check.
    For each hom-element (encoded as hom_stage(a, b, k)), decompose
    the output via interior_bipolar and verify:
    1. e_plus projection + e_minus projection = full sector pair (completeness)
    2. e_plus(e_minus(x)) = 0 (orthogonality)

    This verifies that the hom-object inherits the bipolar structure
    from the codomain's sector decomposition. -/
```

## Source Excerpt

```lean
def hom_bipolar_check (bound db : TauIdx) : Bool :=
  go 2 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (a b k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a > bound then true
    else if b > bound then go (a + 1) 0 1 (fuel - 1)
    else if k > db then go a (b + 1) 1 (fuel - 1)
    else
      let val := hom_stage a b k
      let p := from_tau_idx val
      let sp := interior_bipolar p
      -- Completeness: e+ proj + e- proj = full
      let proj_b := SectorPair.mul e_plus_sector sp
      let proj_c := SectorPair.mul e_minus_sector sp
      let recombined := SectorPair.add proj_b proj_c
      let complete_ok := recombined == sp
      -- Orthogonality: e+(e-(sp)) = 0
      let cross := SectorPair.mul e_plus_sector (SectorPair.mul e_minus_sector sp)
      let ortho_ok := cross == ⟨0, 0⟩
      complete_ok && ortho_ok && go a b (k + 1) (fuel - 1)
  termination_by fuel
```
