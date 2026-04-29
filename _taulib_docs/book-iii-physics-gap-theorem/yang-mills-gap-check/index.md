---
{
  "projection_kind": "taulib_declaration",
  "title": "yang_mills_gap_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-gap-theorem/yang-mills-gap-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.GapTheorem`.",
  "declaration_id": "TauLib.BookIII.Physics.GapTheorem::yang_mills_gap_check",
  "declaration_slug": "yang-mills-gap-check",
  "kind": "def",
  "name": "yang_mills_gap_check",
  "module_name": "TauLib.BookIII.Physics.GapTheorem",
  "module_url": "/verify/taulib/docs/book-iii-physics-gap-theorem/",
  "source_line_start": 140,
  "source_line_end": 158,
  "registry_ids": [
    "III.T27"
  ],
  "related_registry_items": [
    {
      "id": "III.T27",
      "title": "Yang-Mills Gap Theorem",
      "url": "/registry/object/III.T27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L140-L158",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.GapTheorem",
        "url": "/verify/taulib/docs/book-iii-physics-gap-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L140-L158",
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

- Module: [TauLib.BookIII.Physics.GapTheorem](/verify/taulib/docs/book-iii-physics-gap-theorem/)
- Source path: [`TauLib/BookIII/Physics/GapTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/GapTheorem.lean#L140-L158)
- Source range: L140-L158
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T27` — Yang-Mills Gap Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T27] Yang-Mills gap check: the YM mass gap is the τ-gap
    restricted to the gauge sector. The gauge structure comes from
    the B/C asymmetry of the split-complex zeta at E₁. -/
```

## Source Excerpt

```lean
def yang_mills_gap_check (db : TauIdx) : Bool :=
  go 3 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      -- Gap is positive
      let gc := gap_constant k
      let gap_ok := gc > 0
      -- Sector is strong (unambiguous B/C decomposition)
      let strong := strong_sector_at_level k
      -- B/C asymmetry (gauge content): B ≠ C products
      let bp := split_zeta_b k
      let cp := split_zeta_c k
      let (b_ct, c_ct, _) := label_counts k
      let asymm := if b_ct > 0 && c_ct > 0 then bp != cp else true
      gap_ok && strong && asymm && go (k + 1) (fuel - 1)
  termination_by fuel
```
