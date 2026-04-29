---
{
  "projection_kind": "taulib_declaration",
  "title": "interface_width",
  "permalink": "/verify/taulib/docs/book-iii-computation-admissibility/interface-width/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.Admissibility`.",
  "declaration_id": "TauLib.BookIII.Computation.Admissibility::interface_width",
  "declaration_slug": "interface-width",
  "kind": "def",
  "name": "interface_width",
  "module_name": "TauLib.BookIII.Computation.Admissibility",
  "module_url": "/verify/taulib/docs/book-iii-computation-admissibility/",
  "source_line_start": 46,
  "source_line_end": 62,
  "registry_ids": [
    "III.D53"
  ],
  "related_registry_items": [
    {
      "id": "III.D53",
      "title": "Interface Width",
      "url": "/registry/object/III.D53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L46-L62",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L46-L62",
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
- Source path: [`TauLib/BookIII/Computation/Admissibility.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/Admissibility.lean#L46-L62)
- Source range: L46-L62
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D53` — Interface Width

## Immediate Comment / Docstring

```lean
/-- [III.D53] Interface width at a single input: the depth at which
    the TTM computation stabilizes. Returns the first k where running
    4 steps gives the same register-A value as at depth k+1. -/
```

## Source Excerpt

```lean
def interface_width (x db : TauIdx) : TauIdx :=
  go x 1 (db + 1)
where
  go (x k fuel : Nat) : TauIdx :=
    if fuel = 0 then k
    else if k >= db then k
    else
      let pk := primorial k
      let pk1 := primorial (k + 1)
      if pk == 0 || pk1 == 0 then go x (k + 1) (fuel - 1)
      else
        let cfg_k := ttm_run (TTMConfig.mk 0 (x % pk) 1 k) 4
        let cfg_k1 := ttm_run (TTMConfig.mk 0 (x % pk1) 1 (k + 1)) 4
        -- Stable: result at level k and k+1 agree mod Prim(k)
        if cfg_k.reg_a == cfg_k1.reg_a % pk then k
        else go x (k + 1) (fuel - 1)
  termination_by fuel
```
