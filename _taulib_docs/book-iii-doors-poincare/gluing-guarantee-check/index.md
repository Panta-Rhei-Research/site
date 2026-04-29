---
{
  "projection_kind": "taulib_declaration",
  "title": "gluing_guarantee_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-poincare/gluing-guarantee-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.Poincare`.",
  "declaration_id": "TauLib.BookIII.Doors.Poincare::gluing_guarantee_check",
  "declaration_slug": "gluing-guarantee-check",
  "kind": "def",
  "name": "gluing_guarantee_check",
  "module_name": "TauLib.BookIII.Doors.Poincare",
  "module_url": "/verify/taulib/docs/book-iii-doors-poincare/",
  "source_line_start": 96,
  "source_line_end": 117,
  "registry_ids": [
    "III.P13"
  ],
  "related_registry_items": [
    {
      "id": "III.P13",
      "title": "Poincaré as Gluing Guarantee",
      "url": "/registry/object/III.P13/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L96-L117",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.Poincare",
        "url": "/verify/taulib/docs/book-iii-doors-poincare/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L96-L117",
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

- Module: [TauLib.BookIII.Doors.Poincare](/verify/taulib/docs/book-iii-doors-poincare/)
- Source path: [`TauLib/BookIII/Doors/Poincare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L96-L117)
- Source range: L96-L117
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P13` — Poincaré as Gluing Guarantee

## Immediate Comment / Docstring

```lean
/-- [III.P13] Gluing guarantee: local Hartogs bulk projections glue
    coherently when fundamental group is trivial.
    In τ-terms: the CRT local-to-global reconstruction is exact,
    and the bipolar decomposition respects the gluing. -/
```

## Source Excerpt

```lean
def gluing_guarantee_check (bound db : TauIdx) : Bool :=
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
        let xr := x % pk
        -- Local: CRT residues at each prime
        let residues := crt_decompose xr k
        -- Gluing: reconstruct from local data
        let global := crt_reconstruct residues k
        -- Bipolar: BNF respects the gluing
        let nf := boundary_normal_form global k
        let sum := (nf.b_part + nf.c_part + nf.x_part) % pk
        -- Complete coherence: local → global → bipolar → sum = original
        global == xr && sum == xr && go x (k + 1) (fuel - 1)
  termination_by fuel
```
