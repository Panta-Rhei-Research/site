---
{
  "projection_kind": "taulib_declaration",
  "title": "existence_checker",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-functor/existence-checker/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.Functor`.",
  "declaration_id": "TauLib.BookIII.Enrichment.Functor::existence_checker",
  "declaration_slug": "existence-checker",
  "kind": "def",
  "name": "existence_checker",
  "module_name": "TauLib.BookIII.Enrichment.Functor",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-functor/",
  "source_line_start": 106,
  "source_line_end": 120,
  "registry_ids": [
    "III.D10"
  ],
  "related_registry_items": [
    {
      "id": "III.D10",
      "title": "Ladder Checker",
      "url": "/registry/object/III.D10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L106-L120",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Enrichment.Functor",
        "url": "/verify/taulib/docs/book-iii-enrichment-functor/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L106-L120",
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

- Module: [TauLib.BookIII.Enrichment.Functor](/verify/taulib/docs/book-iii-enrichment-functor/)
- Source path: [`TauLib/BookIII/Enrichment/Functor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L106-L120)
- Source range: L106-L120
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D10` — Ladder Checker

## Immediate Comment / Docstring

```lean
/-- [III.D10] Existence checker: verify that level k has at least one
    valid carrier element. Constructive witness required. -/
```

## Source Excerpt

```lean
def existence_checker (k : EnrLevel) (bound db : TauIdx) : Bool :=
  let lt := layer_of k bound db
  -- Try to find a witness: x=0 at stage k=1 should always work
  go lt 0 1 ((bound + 1) * (db + 1))
where
  go (lt : LayerTemplate) (x k_stage fuel : Nat) : Bool :=
    if fuel = 0 then false  -- no witness found = fail
    else if x > bound then false
    else if k_stage > db then go lt (x + 1) 1 (fuel - 1)
    else
      if lt.carrier_check x k_stage && lt.predicate_check x k_stage then
        true  -- found a witness
      else
        go lt x (k_stage + 1) (fuel - 1)
  termination_by fuel
```
