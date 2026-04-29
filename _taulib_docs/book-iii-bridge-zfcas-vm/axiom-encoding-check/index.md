---
{
  "projection_kind": "taulib_declaration",
  "title": "axiom_encoding_check",
  "permalink": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/axiom-encoding-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ZFCasVM`.",
  "declaration_id": "TauLib.BookIII.Bridge.ZFCasVM::axiom_encoding_check",
  "declaration_slug": "axiom-encoding-check",
  "kind": "def",
  "name": "axiom_encoding_check",
  "module_name": "TauLib.BookIII.Bridge.ZFCasVM",
  "module_url": "/verify/taulib/docs/book-iii-bridge-zfcas-vm/",
  "source_line_start": 155,
  "source_line_end": 186,
  "registry_ids": [
    "III.D68"
  ],
  "related_registry_items": [
    {
      "id": "III.D68",
      "title": "Gödel Numbering as NF Address",
      "url": "/registry/object/III.D68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L155-L186",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L155-L186",
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
- Source path: [`TauLib/BookIII/Bridge/ZFCasVM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ZFCasVM.lean#L155-L186)
- Source range: L155-L186
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D68` — Gödel Numbering as NF Address

## Immediate Comment / Docstring

```lean
/-- [III.D68] Axiom encoding check: verify that each axiom is expressible
    at its minimum depth and all depths above it. -/
```

## Source Excerpt

```lean
def axiom_encoding_check (bound db : TauIdx) : Bool :=
  go_ax .extensionality 0 1 ((bound + 1) * (db + 1) * zfc_axiom_count)
where
  /-- All axioms to check. -/
  next_axiom (ax : ZFCAxiom) : Option ZFCAxiom :=
    match ax with
    | .extensionality => some .pairing
    | .pairing        => some .union
    | .union          => some .powerset
    | .powerset       => some .infinity
    | .infinity       => some .separation
    | .separation     => some .replacement
    | .replacement    => some .foundation
    | .foundation     => some .choice
    | .choice         => none
  go_ax (ax : ZFCAxiom) (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then
      match next_axiom ax with
      | some ax' => go_ax ax' 0 1 (fuel - 1)
      | none     => true
    else if k > db then go_ax ax (x + 1) 1 (fuel - 1)
    else
      let min_d := axiom_min_depth ax
      -- At depths >= min_depth, the operation is well-defined
      let ok := if k >= min_d then
        let pk := primorial k
        if pk == 0 then true
        else axiom_operation ax (x % pk) 0 k < pk
      else true
      ok && go_ax ax x (k + 1) (fuel - 1)
  termination_by fuel
```
