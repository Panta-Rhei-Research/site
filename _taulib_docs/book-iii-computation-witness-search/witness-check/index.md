---
{
  "projection_kind": "taulib_declaration",
  "title": "witness_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-witness-search/witness-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.WitnessSearch`.",
  "declaration_id": "TauLib.BookIII.Computation.WitnessSearch::witness_check",
  "declaration_slug": "witness-check",
  "kind": "def",
  "name": "witness_check",
  "module_name": "TauLib.BookIII.Computation.WitnessSearch",
  "module_url": "/verify/taulib/docs/book-iii-computation-witness-search/",
  "source_line_start": 59,
  "source_line_end": 76,
  "registry_ids": [
    "III.D55"
  ],
  "related_registry_items": [
    {
      "id": "III.D55",
      "title": "NP Witness as Canonical Address",
      "url": "/registry/object/III.D55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L59-L76",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.WitnessSearch",
        "url": "/verify/taulib/docs/book-iii-computation-witness-search/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L59-L76",
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

- Module: [TauLib.BookIII.Computation.WitnessSearch](/verify/taulib/docs/book-iii-computation-witness-search/)
- Source path: [`TauLib/BookIII/Computation/WitnessSearch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L59-L76)
- Source range: L59-L76
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D55` — NP Witness as Canonical Address

## Immediate Comment / Docstring

```lean
/-- [III.D55] Witness validity: the BNF components sum to the value. -/
```

## Source Excerpt

```lean
def witness_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x (k + 1) (fuel - 1)
      else
        let w := make_witness x k
        -- Components sum to value
        let sum_ok := (w.b_part + w.c_part + w.x_part) % pk == w.value
        -- Components are bounded
        let bounded := w.b_part < pk && w.c_part < pk && w.x_part < pk
        sum_ok && bounded && go x (k + 1) (fuel - 1)
  termination_by fuel
```
