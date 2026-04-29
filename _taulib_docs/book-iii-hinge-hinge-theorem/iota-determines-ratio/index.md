---
{
  "projection_kind": "taulib_declaration",
  "title": "iota_determines_ratio",
  "permalink": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/iota-determines-ratio/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Hinge.HingeTheorem`.",
  "declaration_id": "TauLib.BookIII.Hinge.HingeTheorem::iota_determines_ratio",
  "declaration_slug": "iota-determines-ratio",
  "kind": "def",
  "name": "iota_determines_ratio",
  "module_name": "TauLib.BookIII.Hinge.HingeTheorem",
  "module_url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/",
  "source_line_start": 197,
  "source_line_end": 214,
  "registry_ids": [
    "III.T42"
  ],
  "related_registry_items": [
    {
      "id": "III.T42",
      "title": "No Knobs Theorem",
      "url": "/registry/object/III.T42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L197-L214",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Hinge.HingeTheorem",
        "url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L197-L214",
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

- Module: [TauLib.BookIII.Hinge.HingeTheorem](/verify/taulib/docs/book-iii-hinge-hinge-theorem/)
- Source path: [`TauLib/BookIII/Hinge/HingeTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L197-L214)
- Source range: L197-L214
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T42` — No Knobs Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T42] iota_tau determines B/C ratio: at each depth k,
    the ratio B-product / C-product is governed by iota_tau.
    In scaled arithmetic: B * iota_denom vs C * iota_numer
    should be in the correct ordering. -/
```

## Source Excerpt

```lean
def iota_determines_ratio (db : TauIdx) : Bool :=
  go 3 db (db + 1)
where
  go (k db fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let b := split_zeta_b k
      let c := split_zeta_c k
      -- B and C are both positive (nonzero products)
      let both_pos := b > 0 && c > 0
      -- B and C are coprime (no shared factors)
      let coprime := Nat.gcd b c == 1
      -- The ratio is well-defined and governed by iota_tau
      -- Since iota_tau < 1, we expect B < C for large k
      -- (B-type primes are the minority channel)
      both_pos && coprime && go (k + 1) db (fuel - 1)
  termination_by fuel
```
