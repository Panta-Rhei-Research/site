---
{
  "projection_kind": "taulib_declaration",
  "title": "mordell_weil_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-rational-points/mordell-weil-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.RationalPoints`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.RationalPoints::mordell_weil_check",
  "declaration_slug": "mordell-weil-check",
  "kind": "def",
  "name": "mordell_weil_check",
  "module_name": "TauLib.BookIII.Arithmetic.RationalPoints",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-rational-points/",
  "source_line_start": 109,
  "source_line_end": 128,
  "registry_ids": [
    "III.P25"
  ],
  "related_registry_items": [
    {
      "id": "III.P25",
      "title": "Mordell-Weil Analogue",
      "url": "/registry/object/III.P25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L109-L128",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.RationalPoints",
        "url": "/verify/taulib/docs/book-iii-arithmetic-rational-points/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L109-L128",
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

- Module: [TauLib.BookIII.Arithmetic.RationalPoints](/verify/taulib/docs/book-iii-arithmetic-rational-points/)
- Source path: [`TauLib/BookIII/Arithmetic/RationalPoints.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L109-L128)
- Source range: L109-L128
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P25` — Mordell-Weil Analogue

## Immediate Comment / Docstring

```lean
/-- [III.P25] Mordell-Weil analogue: the rational point group at level k
    is finitely generated. Count: the number of rational points at each
    level equals Prim(k) (all elements are rational in the canonical tower). -/
```

## Source Excerpt

```lean
def mordell_weil_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      if pk == 0 || pk > 100 then go (k + 1) (fuel - 1)
      else
        -- Count rational points at level k
        let rational_ct := count_rational 0 pk k
        -- All Prim(k) elements are rational (finitely generated)
        rational_ct == pk && go (k + 1) (fuel - 1)
  termination_by fuel
  count_rational (x pk k : Nat) : Nat :=
    if x >= pk then 0
    else
      let ct := if is_rational_at x k then 1 else 0
      ct + count_rational (x + 1) pk k
```
