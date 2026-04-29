---
{
  "projection_kind": "taulib_declaration",
  "title": "applied_saturation_check",
  "permalink": "/verify/taulib/docs/book-iii-mirror-saturation/applied-saturation-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.Saturation`.",
  "declaration_id": "TauLib.BookIII.Mirror.Saturation::applied_saturation_check",
  "declaration_slug": "applied-saturation-check",
  "kind": "def",
  "name": "applied_saturation_check",
  "module_name": "TauLib.BookIII.Mirror.Saturation",
  "module_url": "/verify/taulib/docs/book-iii-mirror-saturation/",
  "source_line_start": 53,
  "source_line_end": 87,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L53-L87",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L53-L87",
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
- Source path: [`TauLib/BookIII/Mirror/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/Saturation.lean#L53-L87)
- Source range: L53-L87
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T49` — Applied Saturation

## Immediate Comment / Docstring

```lean
/-- [III.T49] Applied saturation: the E3 layer template is a fixpoint
    under self-application. For each x, k:
    - E3 decoder applied to E3 decoder output equals E3 decoder output
    - E3 carrier applied to E3 decoder output remains true
    - E3 invariant applied to E3 decoder output remains true

    This is the computational witness of E4 = E3. -/
```

## Source Excerpt

```lean
def applied_saturation_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let e2 := layer_of .E2 bound db
      let e3 := layer_of .E3 bound db
      -- E3 decoder output
      let d1 := e3.decoder x k
      -- E3 decoder applied to its own output (double application)
      let d2 := e3.decoder d1 k
      -- Idempotence: d2 = d1
      let idempotent := d2 == d1
      -- E3 carrier still accepts the double-decoded value
      let carrier_stable := e3.carrier_check d1 k
      -- E3 invariant still holds on the double-decoded value
      let invariant_stable := e3.invariant_check d1 k
      -- E3 predicate still holds on the double-decoded value
      let predicate_stable := e3.predicate_check d1 k
      -- E2 decoder idempotence (non-degenerate level)
      let e2_d1 := e2.decoder x k
      let e2_d2 := e2.decoder e2_d1 k
      let e2_idem := e2_d2 == e2_d1
      idempotent && carrier_stable && invariant_stable &&
        predicate_stable && e2_idem && go x (k + 1) (fuel - 1)
  termination_by fuel

/-! **Scope limitation (E3 collapse):** At finite primorial level, the E3
    predicate degenerates to E0 because `reduce` is idempotent. This check
    is vacuous but correctly models the mathematical structure. The E3 layer
    is correctly DEFINED but finite verification is vacuous.
    See audit DASHBOARD.md §E3 Collapse. -/
```
