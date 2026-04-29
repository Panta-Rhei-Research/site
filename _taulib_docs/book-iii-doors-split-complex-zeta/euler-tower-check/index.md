---
{
  "projection_kind": "taulib_declaration",
  "title": "euler_tower_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/euler-tower-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SplitComplexZeta`.",
  "declaration_id": "TauLib.BookIII.Doors.SplitComplexZeta::euler_tower_check",
  "declaration_slug": "euler-tower-check",
  "kind": "def",
  "name": "euler_tower_check",
  "module_name": "TauLib.BookIII.Doors.SplitComplexZeta",
  "module_url": "/verify/taulib/docs/book-iii-doors-split-complex-zeta/",
  "source_line_start": 129,
  "source_line_end": 143,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L129-L143",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L129-L143",
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
- Source path: [`TauLib/BookIII/Doors/SplitComplexZeta.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SplitComplexZeta.lean#L129-L143)
- Source range: L129-L143
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T16` — Bipolar Euler Product

## Immediate Comment / Docstring

```lean
/-- [III.T16] Tower coherence: products at depth k+1 extend depth k. -/
```

## Source Excerpt

```lean
def euler_tower_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else
      let b_k := split_zeta_b k
      let b_k1 := split_zeta_b (k + 1)
      let b_extend := if b_k > 0 then b_k1 % b_k == 0 else true
      let c_k := split_zeta_c k
      let c_k1 := split_zeta_c (k + 1)
      let c_extend := if c_k > 0 then c_k1 % c_k == 0 else true
      b_extend && c_extend && go (k + 1) (fuel - 1)
  termination_by fuel
```
