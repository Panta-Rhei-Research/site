---
{
  "projection_kind": "taulib_declaration",
  "title": "enrichment_iteration_check",
  "permalink": "/verify/taulib/docs/book-ii-enrichment-two-categories/enrichment-iteration-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Enrichment.TwoCategories`.",
  "declaration_id": "TauLib.BookII.Enrichment.TwoCategories::enrichment_iteration_check",
  "declaration_slug": "enrichment-iteration-check",
  "kind": "def",
  "name": "enrichment_iteration_check",
  "module_name": "TauLib.BookII.Enrichment.TwoCategories",
  "module_url": "/verify/taulib/docs/book-ii-enrichment-two-categories/",
  "source_line_start": 233,
  "source_line_end": 253,
  "registry_ids": [
    "II.P13"
  ],
  "related_registry_items": [
    {
      "id": "II.P13",
      "title": "Character Decomposition",
      "url": "/registry/object/II.P13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L233-L253",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Enrichment.TwoCategories",
        "url": "/verify/taulib/docs/book-ii-enrichment-two-categories/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L233-L253",
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

- Module: [TauLib.BookII.Enrichment.TwoCategories](/verify/taulib/docs/book-ii-enrichment-two-categories/)
- Source path: [`TauLib/BookII/Enrichment/TwoCategories.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Enrichment/TwoCategories.lean#L233-L253)
- Source range: L233-L253
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P13` — Character Decomposition

## Immediate Comment / Docstring

```lean
/-- [II.P13] Enrichment iteration check:
    The hom-space between two 1-morphisms is a τ-object.
    For 1-cells f, g, the 2-cells mediating f => g form
    a set that is closed under reduce at each stage.

    Concretely: the hom-space Hom_2(one_id, one_id) at stage k
    contains at least the identity 2-cell. We verify that this
    hom-space is well-defined and nonempty at each stage. -/
```

## Source Excerpt

```lean
def enrichment_iteration_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      -- The identity 2-cell on one_id: id_two_cell(one_id(x, k), k) = one_id(x, k)
      -- Verify for x in [0, P_k)
      let ok := check_id k 0 pk (pk + 1)
      ok && go (k + 1) (fuel - 1)
  termination_by fuel
  check_id (k x pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= pk then true
    else
      let id_val := one_id x k
      let two_id_val := id_two_cell id_val k
      (two_id_val == id_val) && check_id k (x + 1) pk (fuel - 1)
  termination_by fuel
```
