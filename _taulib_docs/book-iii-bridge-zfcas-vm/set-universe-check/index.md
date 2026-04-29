---
{
  "projection_kind": "taulib_declaration",
  "title": "set_universe_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/set-universe-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ZFCasVM`.",
  "declaration_id": "TauLib.BookIII.Bridge.ZFCasVM::set_universe_check",
  "declaration_slug": "set-universe-check",
  "kind": "def",
  "name": "set_universe_check",
  "module_name": "TauLib.BookIII.Bridge.ZFCasVM",
  "module_url": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/",
  "source_line_start": 198,
  "source_line_end": 215,
  "registry_ids": [
    "III.D70"
  ],
  "related_registry_items": [
    {
      "id": "III.D70",
      "title": "Host-Level Property",
      "url": "/registry/object/III.D70/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L198-L215",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ZFCasVM",
        "url": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L198-L215",
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

- Module: [TauLib.BookIII.Bridge.ZFCasVM](/verify/taulib/docs/book-iii-bridge-zfcas-vm/)
- Source path: [`TauLib/BookIII/Bridge/ZFCasVM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L198-L215)
- Source range: L198-L215
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D70` — Host-Level Property

## Immediate Comment / Docstring

```lean
/-- [III.D70] Set-theoretic universe check: the cumulative hierarchy
    V_0 subset V_1 subset ... is modeled by the primorial tower. -/
```

## Source Excerpt

```lean
def set_universe_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      let vk := universe_rank k
      let vk1 := universe_rank (k + 1)
      -- V_k subset V_{k+1}: Prim(k) <= Prim(k+1)
      let subset_ok := vk <= vk1
      -- Membership preservation: x in V_k implies x in V_{k+1}
      let member_ok := if x < vk then x < vk1 else true
      -- Rank coherence: reduce preserves membership
      let reduce_ok := if vk > 0 then reduce x k < vk else true
      subset_ok && member_ok && reduce_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
