---
{
  "projection_kind": "taulib_declaration",
  "title": "enrichment_functor_faithful",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-functor/enrichment-functor-faithful/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.Functor`.",
  "declaration_id": "TauLib.BookIII.Enrichment.Functor::enrichment_functor_faithful",
  "declaration_slug": "enrichment-functor-faithful",
  "kind": "def",
  "name": "enrichment_functor_faithful",
  "module_name": "TauLib.BookIII.Enrichment.Functor",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-functor/",
  "source_line_start": 72,
  "source_line_end": 88,
  "registry_ids": [
    "III.D04"
  ],
  "related_registry_items": [
    {
      "id": "III.D04",
      "title": "Enrichment Functor",
      "url": "/registry/object/III.D04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L72-L88",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L72-L88",
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
- Source path: [`TauLib/BookIII/Enrichment/Functor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L72-L88)
- Source range: L72-L88
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D04` — Enrichment Functor

## Immediate Comment / Docstring

```lean
/-- [III.D04] Enrichment functor is faithful: the template structure is
    preserved. Specifically, if the source predicate holds, then the
    target predicate also holds (predicate monotonicity). -/
```

## Source Excerpt

```lean
def enrichment_functor_faithful (k : EnrLevel) (bound db : TauIdx) : Bool :=
  let src := layer_of k bound db
  let tgt := layer_of k.succ bound db
  go src tgt 0 1 ((bound + 1) * (db + 1))
where
  go (src tgt : LayerTemplate) (x k_stage fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k_stage > db then go src tgt (x + 1) 1 (fuel - 1)
    else
      -- If x is in src.carrier AND src.predicate holds,
      -- then tgt.invariant should hold (faithfulness)
      let ok := if src.carrier_check x k_stage && src.predicate_check x k_stage then
        tgt.invariant_check x k_stage
      else true
      ok && go src tgt x (k_stage + 1) (fuel - 1)
  termination_by fuel
```
