---
{
  "projection_kind": "taulib_declaration",
  "title": "boundary_restriction_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-topo/boundary-restriction-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationTopo`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationTopo::boundary_restriction_check",
  "declaration_slug": "boundary-restriction-check",
  "kind": "def",
  "name": "boundary_restriction_check",
  "module_name": "TauLib.BookIII.Bridge.TranslationTopo",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-topo/",
  "source_line_start": 158,
  "source_line_end": 188,
  "registry_ids": [
    "III.P37"
  ],
  "related_registry_items": [
    {
      "id": "III.P37",
      "title": "Boundary Restriction",
      "url": "/registry/object/III.P37/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L158-L188",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationTopo",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-topo/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L158-L188",
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

- Module: [TauLib.BookIII.Bridge.TranslationTopo](/verify/taulib/docs/book-iii-bridge-translation-topo/)
- Source path: [`TauLib/BookIII/Bridge/TranslationTopo.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L158-L188)
- Source range: L158-L188
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P37` — Boundary Restriction

## Immediate Comment / Docstring

```lean
/-- [III.P37] Boundary restriction: the fiber of π_k over a ∈ Z/M_k Z
    has exactly p_{k+1} elements in Z/M_{k+1} Z. -/
```

## Source Excerpt

```lean
def boundary_restriction_check (db : Nat) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      let pk1 := primorial (k + 1)
      let p_next := nth_prime (k + 1)
      if pk == 0 || pk1 == 0 || p_next == 0 then go (k + 1) (fuel - 1)
      else
        -- For each a in Z/M_k, count preimages in Z/M_{k+1}
        go_a 0 pk pk1 p_next k fuel && go (k + 1) (fuel - 1)
  termination_by fuel
  go_a (a pk pk1 p_next k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a >= pk then true
    else
      let fiber := count_fiber_size a k pk1
      (fiber == p_next) && go_a (a + 1) pk pk1 p_next k (fuel - 1)
  termination_by fuel
  count_fiber_size (a k pk1 : Nat) : Nat :=
    go_cf 0 pk1 0 a k
  termination_by 0
  go_cf (y bound acc a k : Nat) : Nat :=
    if y >= bound then acc
    else
      let hit := if reduce y k == a then 1 else 0
      go_cf (y + 1) bound (acc + hit) a k
  termination_by bound - y
```
