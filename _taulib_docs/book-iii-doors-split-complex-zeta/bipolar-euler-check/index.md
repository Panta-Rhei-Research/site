---
{
  "projection_kind": "taulib_declaration",
  "title": "bipolar_euler_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/bipolar-euler-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SplitComplexZeta`.",
  "declaration_id": "TauLib.BookIII.Doors.SplitComplexZeta::bipolar_euler_check",
  "declaration_slug": "bipolar-euler-check",
  "kind": "def",
  "name": "bipolar_euler_check",
  "module_name": "TauLib.BookIII.Doors.SplitComplexZeta",
  "module_url": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/",
  "source_line_start": 112,
  "source_line_end": 126,
  "registry_ids": [
    "III.T16"
  ],
  "related_registry_items": [
    {
      "id": "III.T16",
      "title": "Bipolar Euler Product",
      "url": "/registry/object/III.T16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L112-L126",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SplitComplexZeta",
        "url": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L112-L126",
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

- Module: [TauLib.BookIII.Doors.SplitComplexZeta](/verify/taulib/docs/book-iii-doors-split-complex-zeta/)
- Source path: [`TauLib/BookIII/Doors/SplitComplexZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L112-L126)
- Source range: L112-L126
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T16` — Bipolar Euler Product

## Immediate Comment / Docstring

```lean
/-- [III.T16] Bipolar Euler product: B · C · X = Prim(k) and B, C coprime. -/
```

## Source Excerpt

```lean
def bipolar_euler_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let b := split_zeta_b k
      let c := split_zeta_c k
      let x := split_zeta_x k
      let pk := primorial k
      let euler_ok := if pk > 0 then b * c * x == pk else true
      let coprime_ok := Nat.gcd b c == 1
      euler_ok && coprime_ok && go (k + 1) (fuel - 1)
  termination_by fuel
```
