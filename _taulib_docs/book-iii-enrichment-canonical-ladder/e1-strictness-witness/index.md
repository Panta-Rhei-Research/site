---
{
  "projection_kind": "taulib_declaration",
  "title": "e1_strictness_witness",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/e1-strictness-witness/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.CanonicalLadder`.",
  "declaration_id": "TauLib.BookIII.Enrichment.CanonicalLadder::e1_strictness_witness",
  "declaration_slug": "e1-strictness-witness",
  "kind": "def",
  "name": "e1_strictness_witness",
  "module_name": "TauLib.BookIII.Enrichment.CanonicalLadder",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-canonical-ladder/",
  "source_line_start": 69,
  "source_line_end": 89,
  "registry_ids": [
    "III.P01"
  ],
  "related_registry_items": [
    {
      "id": "III.P01",
      "title": "E₁ Strictness Witness",
      "url": "/registry/object/III.P01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L69-L89",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L69-L89",
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

- Module: [TauLib.BookIII.Enrichment.CanonicalLadder](/verify/taulib/docs/book-iii-enrichment-canonical-ladder/)
- Source path: [`TauLib/BookIII/Enrichment/CanonicalLadder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/CanonicalLadder.lean#L69-L89)
- Source range: L69-L89
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P01` — E₁ Strictness Witness

## Immediate Comment / Docstring

```lean
/-- [III.P01] E₁ strictness witness: the bipolar Hom decomposition
    Hom(A,B) = e₊·Hom₊ + e₋·Hom₋ is a genuine E₁ structure.

    The witness is the hom_stage value with its bipolar decomposition.
    At E₀, hom_stage is just a number; at E₁, it carries bipolar structure
    (split-complex scalar action on morphism spaces). -/
```

## Source Excerpt

```lean
def e1_strictness_witness (bound db : TauIdx) : Bool :=
  go 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (a b k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a > bound then true
    else if b > bound then go (a + 1) 0 1 (fuel - 1)
    else if k > db then go a (b + 1) 1 (fuel - 1)
    else
      let val := hom_stage a b k
      let sp := interior_bipolar (from_tau_idx val)
      -- Bipolar decomposition exists and is complete
      let proj_b := SectorPair.mul e_plus_sector sp
      let proj_c := SectorPair.mul e_minus_sector sp
      let recombined := SectorPair.add proj_b proj_c
      let complete := recombined == sp
      -- Orthogonality: e₊(e₋(sp)) = 0
      let cross := SectorPair.mul e_plus_sector (SectorPair.mul e_minus_sector sp)
      let ortho := cross == ⟨0, 0⟩
      complete && ortho && go a b (k + 1) (fuel - 1)
  termination_by fuel
```
