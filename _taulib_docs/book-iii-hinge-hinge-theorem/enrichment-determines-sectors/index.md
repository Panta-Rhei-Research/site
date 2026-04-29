---
{
  "projection_kind": "taulib_declaration",
  "title": "enrichment_determines_sectors",
  "permalink": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/enrichment-determines-sectors/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Hinge.HingeTheorem`.",
  "declaration_id": "TauLib.BookIII.Hinge.HingeTheorem::enrichment_determines_sectors",
  "declaration_slug": "enrichment-determines-sectors",
  "kind": "def",
  "name": "enrichment_determines_sectors",
  "module_name": "TauLib.BookIII.Hinge.HingeTheorem",
  "module_url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/",
  "source_line_start": 146,
  "source_line_end": 171,
  "registry_ids": [
    "III.T41"
  ],
  "related_registry_items": [
    {
      "id": "III.T41",
      "title": "Hinge Theorem",
      "url": "/registry/object/III.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L146-L171",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L146-L171",
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
- Source path: [`TauLib/BookIII/Hinge/HingeTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L146-L171)
- Source range: L146-L171
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T41` — Hinge Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T41] Enrichment determines sectors: at each level, the layer
    template's predicate selects exactly the admissible sector products. -/
```

## Source Excerpt

```lean
def enrichment_determines_sectors (bound db : TauIdx) : Bool :=
  go 0 1 bound db ((bound + 1) * (db + 1))
where
  go (x k bound db fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 bound db (fuel - 1)
    else
      -- At each (x, k): the BNF decomposition determines the sector
      let pk := primorial k
      if pk == 0 then go x (k + 1) bound db (fuel - 1)
      else
        let nf := boundary_normal_form x k
        -- BNF surjectivity: components recover input
        let surjective := (nf.b_part + nf.c_part + nf.x_part) % pk == x % pk
        -- Tower coherence: BNF at k agrees with projection from k+1
        let tower_ok := if k >= 2 then
          let pk_prev := primorial (k - 1)
          if pk_prev > 0 then
            let nf_prev := boundary_normal_form (x % pk_prev) (k - 1)
            let projected := (nf.b_part + nf.c_part + nf.x_part) % pk_prev
            projected == (nf_prev.b_part + nf_prev.c_part + nf_prev.x_part) % pk_prev
          else true
        else true
        surjective && tower_ok && go x (k + 1) bound db (fuel - 1)
  termination_by fuel
```
