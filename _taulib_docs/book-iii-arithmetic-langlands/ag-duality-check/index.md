---
{
  "projection_kind": "taulib_declaration",
  "title": "ag_duality_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-langlands/ag-duality-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.Langlands`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.Langlands::ag_duality_check",
  "declaration_slug": "ag-duality-check",
  "kind": "def",
  "name": "ag_duality_check",
  "module_name": "TauLib.BookIII.Arithmetic.Langlands",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-langlands/",
  "source_line_start": 50,
  "source_line_end": 71,
  "registry_ids": [
    "III.D63"
  ],
  "related_registry_items": [
    {
      "id": "III.D63",
      "title": "Automorphic-Galois Duality in τ",
      "url": "/registry/object/III.D63/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L50-L71",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.Langlands",
        "url": "/verify/taulib/docs/book-iii-arithmetic-langlands/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L50-L71",
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

- Module: [TauLib.BookIII.Arithmetic.Langlands](/verify/taulib/docs/book-iii-arithmetic-langlands/)
- Source path: [`TauLib/BookIII/Arithmetic/Langlands.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/Langlands.lean#L50-L71)
- Source range: L50-L71
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D63` — Automorphic-Galois Duality in τ

## Immediate Comment / Docstring

```lean
/-- [III.D63] Automorphic-Galois duality on ℤ² at finite level:
    m-axis (Galois) = B-part of BNF, n-axis (automorphic) = C-part.
    The duality maps m-data to n-data and vice versa. -/
```

## Source Excerpt

```lean
def ag_duality_check (bound db : TauIdx) : Bool :=
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
        let nf := boundary_normal_form xr k
        -- m-axis data (Galois = B-part)
        let m_data := nf.b_part
        -- n-axis data (automorphic = C-part)
        let n_data := nf.c_part
        -- Duality: both are bounded and their sum with X recovers the original
        let bounded := m_data < pk && n_data < pk
        let recovers := (m_data + n_data + nf.x_part) % pk == xr
        bounded && recovers && go x (k + 1) (fuel - 1)
  termination_by fuel
```
