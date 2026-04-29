---
{
  "projection_kind": "taulib_declaration",
  "title": "saturation_checker",
  "permalink": "/verify/taulib/docs/book-iii-enrichment-functor/saturation-checker/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Enrichment.Functor`.",
  "declaration_id": "TauLib.BookIII.Enrichment.Functor::saturation_checker",
  "declaration_slug": "saturation-checker",
  "kind": "def",
  "name": "saturation_checker",
  "module_name": "TauLib.BookIII.Enrichment.Functor",
  "module_url": "/verify/taulib/docs/book-iii-enrichment-functor/",
  "source_line_start": 172,
  "source_line_end": 194,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L172-L194",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L172-L194",
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
- Source path: [`TauLib/BookIII/Enrichment/Functor.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Enrichment/Functor.lean#L172-L194)
- Source range: L172-L194
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D10` — Ladder Checker

## Immediate Comment / Docstring

```lean
/-- [III.D10] Saturation checker: verify that [E_{k_max}^op, E_{k_max}] ⊆ E_{k_max}.
    At E₃, applying the enrichment functor again gives back E₃. -/
```

## Source Excerpt

```lean
def saturation_checker (bound db : TauIdx) : Bool :=
  -- E₃.succ = E₃ (definitional), so the layers are identical
  let e3 := layer_of .E3 bound db
  let e3_succ := layer_of EnrLevel.E3.succ bound db
  -- Verify that the two layer templates agree on all inputs
  let sat_ok := go e3 e3_succ 0 1 ((bound + 1) * (db + 1))
  -- Non-degenerate witness: E0 and E2 have genuinely different decoders
  -- (E0 extracts parity via x%2; E2 extracts reduce(x,k) — exercises enrichment gap)
  let nondegen := (layer_of .E0 bound db).decoder 3 2 !=
                  (layer_of .E2 bound db).decoder 3 2
  sat_ok && nondegen
where
  go (l1 l2 : LayerTemplate) (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go l1 l2 (x + 1) 1 (fuel - 1)
    else
      let c_eq := l1.carrier_check x k == l2.carrier_check x k
      let p_eq := l1.predicate_check x k == l2.predicate_check x k
      let d_eq := l1.decoder x k == l2.decoder x k
      let i_eq := l1.invariant_check x k == l2.invariant_check x k
      c_eq && p_eq && d_eq && i_eq && go l1 l2 x (k + 1) (fuel - 1)
  termination_by fuel
```
