---
{
  "projection_kind": "taulib_declaration",
  "title": "full_saturation_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-saturation/full-saturation-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.Saturation`.",
  "declaration_id": "TauLib.BookIII.Mirror.Saturation::full_saturation_check",
  "declaration_slug": "full-saturation-check",
  "kind": "def",
  "name": "full_saturation_check",
  "module_name": "TauLib.BookIII.Mirror.Saturation",
  "module_url": "/verify/taulib/docs/book-iii-mirror-saturation/",
  "source_line_start": 91,
  "source_line_end": 114,
  "registry_ids": [
    "III.T49"
  ],
  "related_registry_items": [
    {
      "id": "III.T49",
      "title": "Applied Saturation",
      "url": "/registry/object/III.T49/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L91-L114",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.Saturation",
        "url": "/verify/taulib/docs/book-iii-mirror-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L91-L114",
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

- Module: [TauLib.BookIII.Mirror.Saturation](/verify/taulib/docs/book-iii-mirror-saturation/)
- Source path: [`TauLib/BookIII/Mirror/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L91-L114)
- Source range: L91-L114
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T49` — Applied Saturation

## Immediate Comment / Docstring

```lean
/-- [III.T49] Saturation at all four components: carrier, predicate,
    decoder, and invariant are all fixpoints at E3. -/
```

## Source Excerpt

```lean
def full_saturation_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let e1 := layer_of .E1 bound db
      let e2 := layer_of .E2 bound db
      let e3 := layer_of .E3 bound db
      let e3_succ := layer_of EnrLevel.E3.succ bound db
      -- All four components of E3 and E3.succ agree
      let c_eq := e3.carrier_check x k == e3_succ.carrier_check x k
      let p_eq := e3.predicate_check x k == e3_succ.predicate_check x k
      let d_eq := e3.decoder x k == e3_succ.decoder x k
      let i_eq := e3.invariant_check x k == e3_succ.invariant_check x k
      -- Multi-step reachability on reduced value: E0→E1→E2→E3 chain
      let e0 := layer_of .E0 bound db
      let xr := e3.decoder x k  -- reduced value
      let chain_ok := e0.carrier_check xr k && e1.carrier_check xr k &&
                      e2.carrier_check xr k && e3.carrier_check xr k
      c_eq && p_eq && d_eq && i_eq && chain_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
