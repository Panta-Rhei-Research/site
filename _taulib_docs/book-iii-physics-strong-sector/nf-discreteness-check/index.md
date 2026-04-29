---
{
  "projection_kind": "taulib_declaration",
  "title": "nf_discreteness_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-strong-sector/nf-discreteness-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.StrongSector`.",
  "declaration_id": "TauLib.BookIII.Physics.StrongSector::nf_discreteness_check",
  "declaration_slug": "nf-discreteness-check",
  "kind": "def",
  "name": "nf_discreteness_check",
  "module_name": "TauLib.BookIII.Physics.StrongSector",
  "module_url": "/verify/taulib/docs/book-iii-physics-strong-sector/",
  "source_line_start": 157,
  "source_line_end": 176,
  "registry_ids": [
    "III.P16"
  ],
  "related_registry_items": [
    {
      "id": "III.P16",
      "title": "NF Discreteness Lemma",
      "url": "/registry/object/III.P16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L157-L176",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.StrongSector",
        "url": "/verify/taulib/docs/book-iii-physics-strong-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L157-L176",
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

- Module: [TauLib.BookIII.Physics.StrongSector](/verify/taulib/docs/book-iii-physics-strong-sector/)
- Source path: [`TauLib/BookIII/Physics/StrongSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/StrongSector.lean#L157-L176)
- Source range: L157-L176
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P16` — NF Discreteness Lemma

## Immediate Comment / Docstring

```lean
/-- [III.P16] NF discreteness check: distinct residues mod Prim(k) have
    distinct BNFs. This means the BNF map is injective. -/
```

## Source Excerpt

```lean
def nf_discreteness_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      if pk == 0 || pk > 100 then go (k + 1) (fuel - 1)  -- skip large primorials
      else
        check_inj 0 1 pk k && go (k + 1) (fuel - 1)
  termination_by fuel
  check_inj (x y pk k : Nat) : Bool :=
    if x >= pk then true
    else if y >= pk then check_inj (x + 1) (x + 2) pk k
    else
      let nf_x := boundary_normal_form x k
      let nf_y := boundary_normal_form y k
      let ok := if nf_x == nf_y then x == y else true
      ok && check_inj x (y + 1) pk k
```
