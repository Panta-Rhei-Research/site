---
{
  "projection_kind": "taulib_declaration",
  "title": "cylinder_preservation_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-topo/cylinder-preservation-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationTopo`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationTopo::cylinder_preservation_check",
  "declaration_slug": "cylinder-preservation-check",
  "kind": "def",
  "name": "cylinder_preservation_check",
  "module_name": "TauLib.BookIII.Bridge.TranslationTopo",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-topo/",
  "source_line_start": 118,
  "source_line_end": 145,
  "registry_ids": [
    "III.T60"
  ],
  "related_registry_items": [
    {
      "id": "III.T60",
      "title": "Topological Faithfulness",
      "url": "/registry/object/III.T60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L118-L145",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L118-L145",
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
- Source path: [`TauLib/BookIII/Bridge/TranslationTopo.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L118-L145)
- Source range: L118-L145
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T60` — Topological Faithfulness

## Immediate Comment / Docstring

```lean
/-- [III.T60] Cylinder preservation: cylinders at stage k (sets of the
    form {x : reduce(x,k) = a}) map to open balls in the ultrametric. -/
```

## Source Excerpt

```lean
def cylinder_preservation_check (bound db : Nat) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (a k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a > bound then true
    else if k > db then go (a + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      let pk1 := primorial (k + 1)
      if pk == 0 || pk1 == 0 then go a (k + 1) (fuel - 1)
      else
        let ar := a % pk
        -- Count preimages of ar at stage k+1
        let fiber_size := count_fiber ar k pk1
        -- Fiber should have exactly p_{k+1} elements
        let p_next := nth_prime (k + 1)
        (fiber_size == p_next) && go a (k + 1) (fuel - 1)
  termination_by fuel
  count_fiber (a k pk1 : Nat) : Nat :=
    go_cf 0 pk1 0 a k
  termination_by 0
  go_cf (y bound acc a k : Nat) : Nat :=
    if y >= bound then acc
    else
      let hit := if reduce y k == a then 1 else 0
      go_cf (y + 1) bound (acc + hit) a k
  termination_by bound - y
```
