---
{
  "projection_kind": "taulib_declaration",
  "title": "clopen_locality_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-positive-regularity/clopen-locality-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.PositiveRegularity`.",
  "declaration_id": "TauLib.BookIII.Physics.PositiveRegularity::clopen_locality_check",
  "declaration_slug": "clopen-locality-check",
  "kind": "def",
  "name": "clopen_locality_check",
  "module_name": "TauLib.BookIII.Physics.PositiveRegularity",
  "module_url": "/verify/taulib/docs/book-iii-physics-positive-regularity/",
  "source_line_start": 47,
  "source_line_end": 69,
  "registry_ids": [
    "III.T25"
  ],
  "related_registry_items": [
    {
      "id": "III.T25",
      "title": "Positive Regularity Theorem",
      "url": "/registry/object/III.T25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L47-L69",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.PositiveRegularity",
        "url": "/verify/taulib/docs/book-iii-physics-positive-regularity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L47-L69",
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

- Module: [TauLib.BookIII.Physics.PositiveRegularity](/verify/taulib/docs/book-iii-physics-positive-regularity/)
- Source path: [`TauLib/BookIII/Physics/PositiveRegularity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/PositiveRegularity.lean#L47-L69)
- Source range: L47-L69
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T25` — Positive Regularity Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T25] Clopen locality: each cylinder at level k is determined
    by finitely many residues. The BNF at (x mod Prim(k)) depends
    only on the residues at primes ≤ p_k. -/
```

## Source Excerpt

```lean
def clopen_locality_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x (k + 1) (fuel - 1)
      else
        -- Locality: BNF roundtrip recovers input (surjectivity)
        let nf := boundary_normal_form (x % pk) k
        let sum := (nf.b_part + nf.c_part + nf.x_part) % pk
        let surj := sum == x % pk
        -- Tower coherence: (x % pk) % pk1 == x % pk1
        -- (exercises Nat.mod_mod_of_dvd via primorial divisibility)
        let tower := if k > 1 then
          let pk1 := primorial (k - 1)
          if pk1 > 0 then (x % pk) % pk1 == x % pk1 else true
        else true
        surj && tower && go x (k + 1) (fuel - 1)
  termination_by fuel
```
