---
{
  "projection_kind": "taulib_declaration",
  "title": "width_principle_check",
  "permalink": "/verify/taulib/docs/book-iii-computation-admissibility/width-principle-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.Admissibility`.",
  "declaration_id": "TauLib.BookIII.Computation.Admissibility::width_principle_check",
  "declaration_slug": "width-principle-check",
  "kind": "def",
  "name": "width_principle_check",
  "module_name": "TauLib.BookIII.Computation.Admissibility",
  "module_url": "/verify/taulib/docs/book-iii-computation-admissibility/",
  "source_line_start": 114,
  "source_line_end": 132,
  "registry_ids": [
    "III.T31"
  ],
  "related_registry_items": [
    {
      "id": "III.T31",
      "title": "Interface Width Principle",
      "url": "/registry/object/III.T31/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L114-L132",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.Admissibility",
        "url": "/verify/taulib/docs/book-iii-computation-admissibility/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L114-L132",
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

- Module: [TauLib.BookIII.Computation.Admissibility](/verify/taulib/docs/book-iii-computation-admissibility/)
- Source path: [`TauLib/BookIII/Computation/Admissibility.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L114-L132)
- Source range: L114-L132
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T31` — Interface Width Principle

## Immediate Comment / Docstring

```lean
/-- [III.T31] Interface width principle: once stable, the computation at
    higher levels agrees with the stable level (one quotient suffices). -/
```

## Source Excerpt

```lean
def width_principle_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      let pk1 := primorial (k + 1)
      if pk == 0 || pk1 == 0 then go x (k + 1) (fuel - 1)
      else
        -- Compute at level k and k+1
        let cfg_k := ttm_run (TTMConfig.mk 0 (x % pk) 1 k) 4
        let cfg_k1 := ttm_run (TTMConfig.mk 0 (x % pk1) 1 (k + 1)) 4
        -- Tower coherence: result at k+1 reduces to result at k
        let coherent := cfg_k1.reg_a % pk == cfg_k.reg_a
        coherent && go x (k + 1) (fuel - 1)
  termination_by fuel
```
