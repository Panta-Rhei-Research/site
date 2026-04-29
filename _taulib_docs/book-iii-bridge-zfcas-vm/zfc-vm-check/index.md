---
{
  "projection_kind": "taulib_declaration",
  "title": "zfc_vm_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/zfc-vm-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ZFCasVM`.",
  "declaration_id": "TauLib.BookIII.Bridge.ZFCasVM::zfc_vm_check",
  "declaration_slug": "zfc-vm-check",
  "kind": "def",
  "name": "zfc_vm_check",
  "module_name": "TauLib.BookIII.Bridge.ZFCasVM",
  "module_url": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/",
  "source_line_start": 120,
  "source_line_end": 147,
  "registry_ids": [
    "III.D67"
  ],
  "related_registry_items": [
    {
      "id": "III.D67",
      "title": "ZFC as E₂ VM",
      "url": "/registry/object/III.D67/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L120-L147",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L120-L147",
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
- Source path: [`TauLib/BookIII/Bridge/ZFCasVM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L120-L147)
- Source range: L120-L147
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D67` — ZFC as E₂ VM

## Immediate Comment / Docstring

```lean
/-- [III.D67] ZFC VM check: verify that the ZFC layer template is valid at E2.
    Each axiom operation produces a valid tau-address within primorial range. -/
```

## Source Excerpt

```lean
def zfc_vm_check (bound db : TauIdx) : Bool :=
  go 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (a b k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a > bound then true
    else if b > bound then go (a + 1) 0 1 (fuel - 1)
    else if k > db then go a (b + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go a b (k + 1) (fuel - 1)
      else
        let ar := a % pk
        let br := b % pk
        -- Each axiom produces a valid result
        let ext_ok := axiom_operation .extensionality ar br k < pk
        let pair_ok := axiom_operation .pairing ar br k < pk
        let union_ok := axiom_operation .union ar br k < pk
        let pow_ok := axiom_operation .powerset ar br k < pk
        let inf_ok := axiom_operation .infinity ar br k < pk
        let sep_ok := axiom_operation .separation ar br k < pk
        let rep_ok := axiom_operation .replacement ar br k < pk
        let found_ok := axiom_operation .foundation ar br k < pk
        let choice_ok := axiom_operation .choice ar br k < pk
        ext_ok && pair_ok && union_ok && pow_ok && inf_ok &&
        sep_ok && rep_ok && found_ok && choice_ok &&
        go a b (k + 1) (fuel - 1)
  termination_by fuel
```
