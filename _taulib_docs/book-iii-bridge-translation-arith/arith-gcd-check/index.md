---
{
  "projection_kind": "taulib_declaration",
  "title": "arith_gcd_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-arith/arith-gcd-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationArith`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationArith::arith_gcd_check",
  "declaration_slug": "arith-gcd-check",
  "kind": "def",
  "name": "arith_gcd_check",
  "module_name": "TauLib.BookIII.Bridge.TranslationArith",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-arith/",
  "source_line_start": 191,
  "source_line_end": 210,
  "registry_ids": [
    "III.P36"
  ],
  "related_registry_items": [
    {
      "id": "III.P36",
      "title": "Arithmetic Preserves Operations",
      "url": "/registry/object/III.P36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L191-L210",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationArith",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-arith/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L191-L210",
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

- Module: [TauLib.BookIII.Bridge.TranslationArith](/verify/taulib/docs/book-iii-bridge-translation-arith/)
- Source path: [`TauLib/BookIII/Bridge/TranslationArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L191-L210)
- Source range: L191-L210
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P36` — Arithmetic Preserves Operations

## Immediate Comment / Docstring

```lean
/-- [III.P36] Translation preserves GCD structure. -/
```

## Source Excerpt

```lean
def arith_gcd_check (bound db : Nat) : Bool :=
  go 1 1 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (x y k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 1 1 (fuel - 1)
    else if k > db then go x (y + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x y (k + 1) (fuel - 1)
      else
        let xr := x % pk
        let yr := y % pk
        -- τ-GCD: gcd in Z/M_k Z
        let tau_gcd := Nat.gcd xr yr
        -- Classical GCD: same (gcd commutes with mod for coprime moduli)
        let class_gcd := Nat.gcd (arith_translate xr k) (arith_translate yr k)
        (tau_gcd == class_gcd) && go x y (k + 1) (fuel - 1)
  termination_by fuel
```
